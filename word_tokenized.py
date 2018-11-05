import spacy
import pickle
import argparse
import json
import os


nlp = spacy.blank('en')

def get_fixed_length_token( string, required_len,domain, q_a):

	'''
	this function create fixed length of string so make perfect input for tensorflow tensor
	'''
	string = string.replace('?', ' ')
	string = string.replace('.', ' ')
	string = string.lower()
	string = nlp(string)
	lst = []
	for token in string:
		lst.append(token.text)

	#this if condition apply for question where question folppw by domain
	if q_a == 'q':
		lst.append(domain)
	if len(lst) < required_len:
		pad_data = required_len - len(lst)
		lst = lst + ['<PAD>']*pad_data
	else:
		lst = lst[:required_len]
	return lst

'''
Same dictionary for QA
def create_dictionary(tokenized_list):
	word2id = {}

	index = 2
	word2id['<PAD>'] = 0
	word2id['<S>'] = 1

	for data in tokenized_list:
		question = data['question']
		answer = data['answer']

		for token in question:
			if token not in list(word2id.keys()):
				word2id[token] = index
				index +=1

		for token in answer:
			if token not in list(word2id.keys()):
				word2id[token] = index
				index +=1

	return word2id'''
# its create different dictionary for question and annswer



def create_dictionary(tokenized_list):
	'''
		this fuction create different vocabulary for question and answer
	'''
	que_word2id = {}
	que_index = 2
	que_word2id['<PAD>'] = 0
	que_word2id['<S>'] = 1

	ans_word2id = {}
	ans_index = 2
	ans_word2id['<PAD>'] = 0
	ans_word2id['<S>'] = 1


	for data in tokenized_list:
		question = data['question']
		for token in question:
			if token not in list(que_word2id.keys()):
				que_word2id[token] = que_index
				que_index += 1

		answer = data['answer']
		for token in answer:
			if token not in list(ans_word2id.keys()):
				ans_word2id[token] = ans_index
				ans_index +=1

	return que_word2id, ans_word2id


def tokenized_data(word2id, lst):
	'''
		this fucntion map word with it fixed index
	'''
	return_list = [word2id[word] if word in list(word2id.keys()) else word2id['unk'] for word in lst]
	return return_list

def run(config):
	file_name = config['data_type']+'.json'
	with open(file_name, 'r') as fh:
		data_list = json.load(fh)

	lst = []
	for data in data_list:
		question = data['question']
		answer = data['answer']
		clean_data = {}

		question = get_fixed_length_token(question, config['ques_len'], data['domain'],'q')
		answer = get_fixed_length_token(answer,config['ans_len'], data['domain'],'a')

		clean_data['question'] = question
		clean_data['answer'] = answer
		clean_data['token'] = data['domain']
		clean_data['question_target']= question + ['<S>'] + answer + [data['domain']]

		lst.append(clean_data)

	'''if os.path.isfile('que_word2id_sport.json'):

		with open('que_word2id_sport.json','r') as f:
			que_word2id = json.load(f)

		with open('ans_word2id_sport.json','r') as f:
			ans_word2id = json.load(f)

		#if word not in list(ans_word2id.keys()):
		#	ans_word2id[word] = ans_id

		print('before ',len(que_word2id))
	else:'''
	que_word2id, ans_word2id  = create_dictionary(lst)


	print('before ',len(que_word2id))
	word = '_unk'
	que_id = len(que_word2id)
	ans_id = len(ans_word2id)

	if word not in list(que_word2id.keys()):
		que_word2id[word] = que_id


	que_id2word = dict(zip(list(que_word2id.values()), list(que_word2id.keys())))
	ans_id2word = dict(zip(list(ans_word2id.values()), list(ans_word2id.keys())))

	for data in lst :
		data['question_id'] = tokenized_data(que_word2id, data['question'])
		data['answer_id'] = tokenized_data(ans_word2id,data['answer'])

	file_name = config['data_type']+'_clean_data.json'

	print(len(lst))
	with open(file_name,'w') as f:
		json.dump(lst, f)

	if config['data_type']=='train':
		with open('que_word2id.json','w') as f:
			json.dump(que_word2id, f)

		with open('que_id2word.json','w') as f:
			json.dump(que_id2word, f)

		with open('ans_word2id.json','w') as f:
			json.dump(ans_word2id, f)

		with open('ans_id2word.json','w') as f:
			json.dump(ans_id2word, f)





if __name__ == '__main__':
	PARSER = argparse.ArgumentParser("Command line arguments")
	
	PARSER.add_argument("-t", "--data_type", default='train',
						type=str, dest="data_type", help="give me file name for tokenized data")

	PARSER.add_argument('-ql','--ques_len',default = 15, type= int ,
						dest ='ques_len',help = 'give me maximun number of word in question')

	PARSER.add_argument('-al','--ans_len',default= 15, type= int,
						dest='ans_len',help = 'give me maximum number of word in answer')

	FLAGS = PARSER.parse_args()
	run(vars(FLAGS))
