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
import os
def get_demo(config, reader_class, ans_id2word, question):
	model = Model(config, train=False)
	data,unk_list = reader_class.prepare_data(config, question, 15)

		# [Variable and model creation goes here.]
	init_op = tf.global_variables_initializer()
	with tf.Session() as sess:
		sess.run(init_op)
		saver = tf.train.Saver()
		path = os.getcwd()
		path = os.path.join(path,'model')
		saver.restore(sess, tf.train.latest_checkpoint(path))
		feed_dict = {model.encoder_inputs : data}

		pred_value = model.infer_value(sess,feed_dict =feed_dict)
		pred_value = pred_value[0][0]

		gen_answer = ''
		gen_answer1 = ''

		for ix in pred_value :

			word =  ans_id2word[int(ix[0])]
			word1 = ans_id2word[int(ix[1])]
			if word != '<PAD>':
				gen_answer += word + ' '
			if word1 != '<PAD>':
				gen_answer1 +=word1+ ' '

	return gen_answer, gen_answer1, unk_list




