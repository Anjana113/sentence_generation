import pickle
import random 
import re
import json
import argparse

with open('question_temmplate.pkl','rb') as f:
	final_dict = pickle.load(f)

list_of_topic = list(final_dict.keys())

def run(config):
	lst = []
	data_size = config['data_size']
	print(data_size)
	for i in range(0,data_size):
		write_it = {}
		x = 0
		topic = 'sport'

		question_temmplate = final_dict[topic]['question_temmplate']
		mapping_words = list(final_dict[topic]['mapping'].keys())

		question_list = list(question_temmplate.keys())

		choose_question  = random.randint(0,len(question_list)-1)

		question = question_list[choose_question]
		respone = question_temmplate[question]

		choose_response = random.randint(0,len(respone)-1)
		answer = respone[choose_response]

		for word in mapping_words:

			if question.find(word) > -1:
				replace_word_list = final_dict[topic]['mapping'][word]
				replace_word = replace_word_list[random.randint(0,len(replace_word_list) - 1 )]
				question = question.replace(word , replace_word)
				if answer.find(word) > -1:
					answer = answer.replace(word, replace_word)

		question = re.sub('<DOMAIN>',topic, question)
		answer = re.sub('<DOMAIN>', topic, answer)
		#print("question {} \n answer {} \n ----------------\n".format(question, answer))
		write_it['question'] = question
		write_it['answer'] = answer
		write_it['domain'] = topic
		lst.append(write_it)

	print(config['data_type'])
	file_name = config['data_type']+'.json'

	print(len(lst))
	with open(file_name,'w') as f:
		json.dump(lst,f)




if __name__ == '__main__':
	PARSER = argparse.ArgumentParser("Command line arguments")
	PARSER.add_argument("-n", "--size", default=1000,
						type=int, dest="data_size", help="Number of question and answer generate")
	PARSER.add_argument("-t", "--data_type", default='train_sport',
						type=str, dest="data_type", help="generate train or test data")
	FLAGS = PARSER.parse_args()
	run(vars(FLAGS))




