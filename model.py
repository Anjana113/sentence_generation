import tensorflow as tf
from tensorflow.python.layers import core as layers_core

class Model(object):
	def __init__(self, config, train=True):
		
		self.encoder_length = config['encode_length']
		self.decoder_length = config['decode_length']
		self.encode_units = config['encode_units']
		self.scr_vocab_size = config['src_vocab_size'] + 1
		self.tgt_vocab_size = config['tgt_vocab_size']
		self.learning_rate = config['learning_rate']
		self.embedding_size = config['embedding_size']
		self.tgt_sos_id = config['tgt_sos_id']
		self.tgt_eos_id = config['tgt_eos_id']
		self.num_units = self.encode_units
		self.beam_width = config['beam_width']
		self.num_layers = config['num_layers'] 
		self.multi_layer = config['multi_layer']
		self.train = train
	
		if train:
			self.batch_size = config['batch_size']
		else :
			self.batch_size = 1

		self.encoder_inputs = tf.placeholder(tf.int32, shape=(self.encoder_length, self.batch_size), name="encoder_inputs")
		print('encoder_inputs',self.encoder_inputs.get_shape().as_list())

		self.decoder_inputs = tf.placeholder(tf.int32, shape=(self.decoder_length, self.batch_size), name="decoder_inputs")
		self.decoder_lengths = tf.placeholder(tf.int32, shape=(self.batch_size), name="decoer_length")

		print('decoder input', self.decoder_inputs.get_shape().as_list())
		print('decoder lengths',self.decoder_lengths.get_shape().as_list())

		self.target_labels = tf.placeholder(tf.int32, shape=(self.batch_size, self.decoder_length))
		print('target lable',self.target_labels.get_shape().as_list())

		self.global_step = tf.Variable(0, name='global_step', trainable = False )

		self.forward()

		if train:
			self.params = tf.trainable_variables()
			self.grd = tf.gradients(self.loss, self.params)
			clipped_grad,_ = tf.clip_by_global_norm(self.grd, config['max_grd_norm'])

			optimizer = tf.train.AdamOptimizer(self.learning_rate)
			self.train_op = optimizer.apply_gradients(zip(clipped_grad, self.params), global_step = self.global_step)


	def forward(self):
		embedding_encoder = tf.get_variable("embedding_encoder", [self.scr_vocab_size, self.embedding_size],trainable=True)
		encoder_emb_inputs = tf.nn.embedding_lookup(embedding_encoder, self.encoder_inputs)
		encoder_cell = tf.nn.rnn_cell.BasicLSTMCell(self.encode_units)

		encoder_outputs, encoder_state = tf.nn.dynamic_rnn(encoder_cell, encoder_emb_inputs, time_major=True, dtype=tf.float32)

		self.initial_state = encoder_state

		self.embedding_decoder = tf.get_variable("embedding_decoder", [self.tgt_vocab_size, self.embedding_size],trainable=True) 

		decoder_emb_inputs = tf.nn.embedding_lookup(self.embedding_decoder, self.decoder_inputs)
		self.projection_layer = layers_core.Dense(self.tgt_vocab_size, use_bias=True)
		helper = tf.contrib.seq2seq.TrainingHelper(decoder_emb_inputs, self.decoder_lengths, time_major=True)
 
		helper = tf.contrib.seq2seq.TrainingHelper(decoder_emb_inputs, self.decoder_lengths, time_major=True)

		# Decoder with helper:
		#   decoder_emb_inputs: [decoder_length, batch_size, embedding_size]
		#   decoder_length: [batch_size] vector, which represents each target sequence length.
		self.decoder_cell = tf.nn.rnn_cell.BasicLSTMCell(self.num_units)
		self.initial_state = encoder_state

		decoder = tf.contrib.seq2seq.BasicDecoder(self.decoder_cell, helper, self.initial_state,output_layer=self.projection_layer)

		final_outputs, _final_state, _final_sequence_lengths = tf.contrib.seq2seq.dynamic_decode(decoder)

		logits = final_outputs.rnn_output
		decoder_predictions_train = tf.argmax(logits, axis = -1)
		decoder_predictions_train = tf.identity(decoder_predictions_train)

		# Target labels
		#   As described in doc for sparse_softmax_cross_entropy_with_logits,
		#   labels should be [batch_size, decoder_lengths] instead of [batch_size, decoder_lengths, tgt_vocab_size].
		#   So labels should have indices instead of tgt_vocab_size classes.

		
		# Loss
		self.loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
				labels=self.target_labels, logits=logits)


	def infer_value(self, sess, feed_dict):
		inference_helper = tf.contrib.seq2seq.GreedyEmbeddingHelper(self.embedding_decoder,
			tf.fill([self.batch_size], self.tgt_sos_id), self.tgt_eos_id)


		inference_decoder = tf.contrib.seq2seq.BasicDecoder(
					self.decoder_cell, inference_helper, self.initial_state,
					output_layer=self.projection_layer)

		source_sequence_length = self.encoder_length
		maximum_iterations = tf.round(tf.reduce_max(source_sequence_length) * 2)

		decoder_initial_state = tf.contrib.seq2seq.tile_batch(
				self.initial_state, multiplier=self.beam_width)



		inference_decoder = tf.contrib.seq2seq.BeamSearchDecoder(
						cell=self.decoder_cell,
						embedding=self.embedding_decoder,
						start_tokens=tf.fill([self.batch_size], self.tgt_sos_id),
						end_token=self.tgt_eos_id,
						initial_state=decoder_initial_state,
						beam_width=self.beam_width,
						output_layer=self.projection_layer)

		outputs, _, _ = tf.contrib.seq2seq.dynamic_decode(
				inference_decoder, maximum_iterations=maximum_iterations)

		translations = outputs.predicted_ids
		pred_value = sess.run([translations], feed_dict=feed_dict)

		return pred_value



	