from model import Model
import numpy as np
import os
import json
import argparse
from reader import reader
import random
import tensorflow as tf
import nltk
import json
import pickle
from try_sqs_with_attension import Seq2SeqModel


def train(config):
	epoch = 1
	src_dict = config['src_dict']
	tgt_dict = config['tgt_dict']
	MAX_STEP = config['max_step']
	path = os.getcwd()

	model_dir = os.path.join(path, 'model_sport')
	config['model_dir'] = model_dir

	with open(src_dict) as f:
		source_dict = json.load(f)

	with open(tgt_dict) as f:
		target_dict = json.load(f)

	

	ques_id2word = dict(zip(list(source_dict.values()), list(source_dict.keys())))
	ans_id2word = dict(zip(list(target_dict.values()), list(target_dict.keys())))

	config['src_vocab_size'] = len(source_dict)
	config['tgt_vocab_size'] =  len(target_dict)

	reader_class = reader(config)

	print('train data ', reader_class.train_len)
	print('test data',reader_class.test_len)
	possible_batch_train = int(reader_class.train_len/config['batch_size'])
	total_loss = []


	g = tf.Graph()
	log_dir = os.path.join(path,'logdir')
	with g.as_default() as g:
		model = Seq2SeqModel(config, 'train')
		with tf.Session() as sess:
			sess.run(tf.global_variables_initializer())
			saver =  tf.train.Saver()
			writer = tf.summary.FileWriter(log_dir, sess.graph)
			print('possible batch in one epoch', possible_batch_train)
			for i in range(0,6):

				for _step in range(1,possible_batch_train):
					source, source_len, target, target_len = reader_class.get_without_fixed_len()
					step_loss, summary = model.train(sess, encoder_inputs=source, encoder_inputs_length=source_len, 
													 decoder_inputs=target, decoder_inputs_length=target_len)
					total_loss.append(step_loss)
					if _step%100==0:
						print('after {} steps average_loss is {} '.format(_step,np.mean(total_loss)))

				print('After {} epoch loss value is {}'.format(i,np.mean(total_loss)))


				if i%5 == 0:
					filename = os.path.join(config['model_dir'], "model_{}.ckpt".format(i))
					saver.save(sess, filename)
			writer.flush()

	'''
	#this graph is used for model class
	graph = tf.Graph()
	with graph.as_default() as g:
		model = Model(config,Train=True)
		with tf.Session() as sess:
			sess.run(tf.global_variables_initializer())
			saver = tf.train.Saver()
			global_step = max(sess.run(model.global_step), 1)

			for steps in range(global_step, MAX_STEP):

				train_data_feed = reader_class.get_train_data()
				feed_d ={
					model.encoder_inputs : train_data_feed['encoder_inputs'],
					model.target_labels :train_data_feed['target_labels'],
					model.decoder_inputs: train_data_feed['decoder_inputs'],
					model.decoder_lengths :train_data_feed['decoder_lengths']
					}
				_, loss_val = sess.run([model.train_op, model.loss], feed_dict=feed_d)
				
				total_loss.append(np.mean(loss_val))
				if steps%100 == 0:
					print('print loss value after {} th batch is {} '.format(steps,np.mean(total_loss)))
					loss_val = []
					evalute_bleu_score =  evalution_test_data(config , reader_class,model,sess, ans_id2word)
				
				#evalute_bleu_score =  evalution_test_data(config , reader_class,model,sess, ans_id2word)'''

def evalution_test_data(config, reader_class, model, sess,ans_id2word ):
	test_data_size = reader_class.test_len
	number_batches = int(test_data_size/ config['batch_size'])
	bleu_score = []
	print(number_batches)


	for i in range(0, number_batches):
		test = reader_class.get_test_data()
		test_feed_dict = {}
		test_feed_dict ={model.encoder_inputs : test['encoder_inputs']}
		pred_value = model.infer_value(sess,test_feed_dict)


		for i in range(0,1):
			ans = test['target_labels'][i]
			decode = pred_value[0][i]
			ans_ = [ans_id2word[int(ix)] for ix in ans if ans_id2word[int(ix)] != '<PAD>']
			gen_ = [ans_id2word[int(ix[0])] for ix in decode if ans_id2word[int(ix[0])] != '<PAD>']

			_score =  nltk.translate.bleu_score.sentence_bleu([ans_], gen_, weights = [1])
			bleu_score.append(_score)
			a =' '.join(word for word in ans_)
			g = ' '.join(word for word in gen_)
			print(a)
			print(g)
	return np.mean(bleu_score)

if __name__ == '__main__':

	PARSAR = argparse.ArgumentParser('Command line arguments')

	PARSAR.add_argument('-demo','--demo',default= False,
		type=bool, dest='demo', help = 'demo the file')

	PARSAR.add_argument('-multi_layer','--multi_layer',default= False,
		type=bool, dest='multi_layer', help = 'demo the file')

	PARSAR.add_argument('-train','--train_file',default = 'train_sport_clean_data.json',
		type=str,dest='train_file', help= 'give me train file')

	PARSAR.add_argument('-test','--test_file',default = 'test_sport_clean_data.json', 
		type = str, dest='test_file', help= 'give me test file')

	PARSAR.add_argument('-src_dict','--src_vocabulary',default = 'que_word2id_sport.json', 
		type = str, dest='src_dict', help= 'give source dictionary file')

	PARSAR.add_argument('-tgt_dict','--tgt_vocabulary',default = 'ans_word2id_sport.json', 
		type = str, dest='tgt_dict', help= 'give target target dictionary file')

	PARSAR.add_argument('-batch_size','--batch_size',default = 32, 
		type= int ,dest= 'batch_size', help = 'batch size to train model')

	PARSAR.add_argument('-encode_length','--encode_length', default = 16,
		type= int , dest = 'encode_length', help= 'encoding question length')

	PARSAR.add_argument('-decode_length','--decode_length', default = 16 ,
		type= int , dest = 'decode_length', help = 'decoding answer length')

	PARSAR.add_argument('-learning_rate','--learning_rate',default= 0.001,
		type= float, dest='learning_rate', help = 'learning rate of code')

	PARSAR.add_argument('-embedding_size','--embedding_size', default = 512,
		type= int, dest='embedding_size', help = 'embedding input')

	PARSAR.add_argument('-max_step','--max_step',default=40000, 
		type=int, dest= 'max_step', help = 'maximun number of iteration')

	PARSAR.add_argument('-tgt_sos_id','--tgt_sos_id', default=1,
		type= int , dest ='tgt_sos_id', help='end_of_sentence_id')

	PARSAR.add_argument('-tgt_eos_id','--tgt_eos_id',default=0, 
		type=int, dest= 'tgt_eos_id', help = 'end of response')

	PARSAR.add_argument('-encode_units','--encode_units',default=512,
		type=int, dest='encode_units', help = 'encoder units')

	PARSAR.add_argument('-max_gradient_norm','--max_gradient_norm',default=1,
		type=float, dest ='max_gradient_norm', help = 'max gradiant normalization')

	PARSAR.add_argument('-dropout_rate','--dropout_rate',default=512,
		type=float, dest ='dropout_rate', help = 'dropout rate')

	PARSAR.add_argument('-beam_width','--beam_width',default=3,
		type=float, dest ='beam_width', help = 'max gradiant normalization')

	PARSAR.add_argument('-attention_type','--attention_type',default='bahdanau',
		type=str, dest ='attention_type', help = 'name of attension')

	PARSAR.add_argument('-cell_type','--cell_type',default='LSTM',
		type=str, dest ='cell_type', help = 'number of layers')

	PARSAR.add_argument('-depth','--depth',default=2,
		type=int, dest ='depth', help = 'number of layers')

	PARSAR.add_argument('-use_dropout','--use_dropout',default= True,
		type=bool, dest='use_dropout', help = 'need to use dropout')

	PARSAR.add_argument('-attn_input_feeding','--attn_input_feeding',default= False,
		type=bool, dest='attn_input_feeding', help = 'need to add input in attension')



	flags = PARSAR.parse_args()
	train(vars(flags))
