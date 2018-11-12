import os
import math
import time
import json
import random
from try_sqs_with_attension import Seq2SeqModel
import tensorflow as tf
from reader import reader


def decode(config):
	tf.reset_default_graph()
	config['max_decode_step'] = 500

	reader_class = reader(config)
	path = os.getcwd()
	model_path = config['model_dir']
	model = Seq2SeqModel(config, 'decode')


	init_op = tf.global_variables_initializer()
	with tf.Session() as sess:
		sess.run(init_op)
		saver =tf.train.Saver()
		model = Seq2SeqModel(config, 'decode')
		if tf.train.checkpoint_exists(model_path):
			print('Reloading model parameters..')
			#model.restore(sess, model_path)
			saver.restore(sess, tf.train.latest_checkpoint(model_path))
		else:
			raise ValueError('No such file:[{}]'.format(model_path))

		possible_batch_test = int(reader_class.test_len/config['batch_size'])
		

		default_path = os.path.abspath(os.pardir)
		data_path = os.path.join(default_path, 'data')
		src_dict = os.path.join(data_path, config['src_dict'])
		tgt_dict = os.path.join(data_path, config['tgt_dict'])

		with open(src_dict) as f:
			ques_dict = json.load(f)

		with open(tgt_dict) as f:
			ans_dict = json.load(f)

		ans_id_word = dict(zip(list(ans_dict.values()),list(ans_dict.keys())))
		ques_id_word = dict(zip(list(ques_dict.values()),list(ques_dict.keys())))
		print(list(ans_id_word.keys())[:10])

		for idx in range(2):
			source, source_len,target, target_len =reader_class.get_without_fixed_len_test()
			predicted_ids = model.predict(sess, encoder_inputs=source, 
												  encoder_inputs_length=source_len)

			
			for j in range(32):
				ques = ''
				for i in range(source_len[j]):
					word = source[j][i]
					ques+= ques_id_word[word] + ' '

				actual_ans = ''
				for i in range(target_len[j]):
					word = target[j][i]
					actual_ans+= ans_id_word[word] + ' '

				ans_1 = ''
				ans_2 = ''
				for i in predicted_ids[j]:
					if i[0] != 0:
						ans_1 += ans_id_word[i[0]]+ ' '
					if i[1] != 0:
						ans_2 += ans_id_word[i[1]]+ ' '


				print('question : {} \nActual_answer: {} \ngenerated_answer_1 : {} \ngenerated_answer_2 : {}'.format(ques, actual_ans, ans_1, ans_2))
				print('\n------------------------------------------\n')

		
if __name__ == '__main__':
	with open('config.json') as f:
		config = json.load(f)
	decode(config)


