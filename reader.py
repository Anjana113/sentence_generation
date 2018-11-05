import json
import os
import numpy as np
import random
import spacy
nlp= spacy.blank('en')
class reader(object):
	def __init__(self, config):
		path = os.getcwd()
		train_file = os.path.join(path, config['train_file'])
		test_file = os.path.join(path,config['test_file'])
		with open(train_file,'r') as f:
			train_data = json.load(f)

		with open(test_file, 'r') as f:
			test_data = json.load(f)

		src_dict = config['src_dict']
		tgt_dict = config['tgt_dict']

		with open(src_dict) as f:
			self.source_dict = json.load(f)

		with open(tgt_dict) as f:
			self.target_dict = json.load(f)

		print(len(self.source_dict))
		
		self.train_index = 0
		self.test_index = 0
		self.batch_size = config['batch_size']
		self.train_len = len(train_data)
		self.test_len = len(test_data)
		self.encoder_length = config['encode_length']
		self.decoder_length = config['decode_length']
		self.train_data = train_data
		self.test_data =test_data
		#Symbol for end of sentence
		self.tgt_sos_id = config['tgt_sos_id']
		# Symbol for end of decode process.
		self.tgt_eos_id = config['tgt_eos_id']

		self.train_source_dataset = [data['question_id']+[0] for data in train_data]
		self.train_output_dataset = [data['answer_id'] for data in train_data]
		self.training_encoder_inputs = self.train_source_dataset
		self.training_decoder_inputs = [[self.tgt_sos_id]+lst for lst in self.train_output_dataset]
		self.training_target_labels = [lst +[self.tgt_eos_id] for lst in self.train_output_dataset]


		self.test_source_dataset = [data['question_id']+[0] for data in train_data]
		self.test_output_dataset = [data['answer_id'] for data in train_data]
		self.testing_encoder_inputs = self.test_source_dataset
		self.testing_decoder_inputs = [[self.tgt_sos_id]+lst for lst in self.test_output_dataset]
		self.testing_target_labels = [lst +[self.tgt_eos_id] for lst in self.test_output_dataset]

	def get_train_data(self):
		if (self.train_index + self.batch_size) > len(self.train_data):
			self.train_index = 0

		training_encoder_inputs_1 = np.empty((self.encoder_length, self.batch_size))
		training_target_labels_1 = np.empty((self.batch_size, self.decoder_length))
		training_decoder_inputs_1 = np.empty((self.decoder_length, self.batch_size))

		ix = 0
		for idx in range(self.train_index, self.train_index+self.batch_size):
			training_encoder_inputs_1[:,ix] = self.training_encoder_inputs[idx]
			training_target_labels_1[ix] = self.training_target_labels[idx]
			training_decoder_inputs_1[:,ix] = self.training_decoder_inputs[idx]
			ix +=1

		#print(training_encoder_inputs_1[0])
		self.train_index = self.train_index+ self.batch_size
		feed_dict = {
				'encoder_inputs': training_encoder_inputs_1,
				'target_labels': training_target_labels_1,
				'decoder_inputs': training_decoder_inputs_1,
				'decoder_lengths':  np.ones((self.batch_size), dtype=int) * self.decoder_length
				}

		return feed_dict

	def get_without_fixed_len(self):
		if (self.train_index + self.batch_size) > len(self.train_data):
			self.train_index = 0

		seqs_x = self.train_source_dataset[self.train_index : self.train_index+self.batch_size]
		seqs_y = self.train_output_dataset[self.train_index : self.train_index+self.batch_size]

		lengths_x = []
		lengths_y = [] 

		for i,j in zip(seqs_x,seqs_y):
			try:
				word_input = i.index(0)
			except:
				word_input = 15

			try:
				word_output = j.index(0)
			except:
				word_input = 15


			lengths_x.append(word_input)
			lengths_y.append(word_output)

		x_lengths = np.array(lengths_x)
		y_lengths = np.array(lengths_y)

		maxlen_x = np.max(x_lengths)
		maxlen_y = np.max(y_lengths)

		x = np.ones((self.batch_size, maxlen_x)).astype('int32') * end_token
		y = np.ones((batch_size, maxlen_y)).astype('int32') * end_token
	
		for idx, [s_x, s_y] in enumerate(zip(seqs_x, seqs_y)):
			x[idx, :lengths_x[idx]] = s_x
			y[idx, :lengths_y[idx]] = s_y
		return x, x_lengths, y, y_lengths



	def get_test_data(self):
		if (self.test_index + self.batch_size) > len(self.test_data):
			self.train_index = 0

		testing_encoder_inputs_1 = np.empty((self.encoder_length, self.batch_size))
		testing_target_labels_1 = np.empty((self.batch_size, self.decoder_length))
		testing_decoder_inputs_1 = np.empty((self.decoder_length, self.batch_size))

		ix = 0
		for idx in range(self.test_index, self.test_index+self.batch_size):
			testing_encoder_inputs_1[:,ix] = self.testing_encoder_inputs[idx]
			testing_target_labels_1[ix] = self.testing_target_labels[idx]
			testing_decoder_inputs_1[:,ix] = self.testing_decoder_inputs[idx]
			ix +=1


		self.test_index = self.test_index+ self.batch_size
		feed_dict = {
				'encoder_inputs': testing_encoder_inputs_1,
				'target_labels': testing_target_labels_1,
				'decoder_inputs': testing_decoder_inputs_1,
				'decoder_lengths':  np.ones((self.batch_size), dtype=int) * self.decoder_length
				}

		return feed_dict


	def prepare_data(self, config,sentence, required_len):
		sentence = sentence.lower()
		sentence = sentence.replace('?', ' ')
		sentence = sentence.replace('.', ' ')
		sentence = sentence.lower()
		sentence = nlp(sentence)
		lst = []
		for token in sentence:
			lst.append(token.text)

		if len(lst) < required_len:
			pad_data = required_len - len(lst)
			lst = lst + ['<PAD>']*pad_data
		else:
			lst = lst[:required_len]

		unk_list = [word for word in lst if word not in self.source_dict.keys() ]

		question_id = [ self.source_dict[word] if word in self.source_dict.keys() else self.source_dict['_unk'] for word in lst]
		print(question_id)

		question_id.append(0)


		testing_encoder_inputs_1 = np.empty((self.encoder_length, 1))
		testing_encoder_inputs_1= np.array(question_id)
		testing_encoder_inputs_1 = np.reshape(testing_encoder_inputs_1,(16,1))
		print(testing_encoder_inputs_1.shape)

		return testing_encoder_inputs_1, unk_list







