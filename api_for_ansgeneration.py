import pickle
import numpy as np
import os
import json
import traceback
import requests

from ast import literal_eval
from flask import Flask
from flask_restful import reqparse,abort,Api, Resource,request

from demo import get_demo
from reader import reader

with open('config.json','r') as f:
	config = json.load(f)

with open('ans_word2id.json') as f:
	target_dict = json.load(f)

ans_id2word = dict(zip(list(target_dict.values()), list(target_dict.keys())))

reader_class = reader(config)
url = "http://35.237.108.126:9091/infer"


app = Flask(__name__)
@app.route('/generate_answer',methods=['POST'])
def apicall():
	try:
		test_json = request.json
		test = test_json["question"]

		data = '{ "query\" :"' +test + '\"}'

		headers = {
		 'content-type': "application/json",
		 'cache-control': "no-cache",
		 'postman-token': "d6a68760-bacb-dd4c-1493-5f78c4db4db5"
   			}


		'''response = requests.request("POST", url, data=data, headers=headers)
		print(response.text)
		try:
			response_list = literal_eval(response.text)
			domain = response_list[0][0]
		except:
			domain = 'oov'
		print(domain)

		if domain.find(' '):
			domain = domain.split(' ')[0]
		if domain == 'Medicine':
			domain = 'health'
		test = test+ ' '+domain'''
		test = test.lower()
		ans1,ans2,unk_list = get_demo(config,reader_class, ans_id2word, test)

		output = {'ans_1':ans1, 'ans_2':ans2}
		
		#utput = {'domain ':domain ,'ans_1 ':ans1, 'ans_2 ':ans2, 'unk_list ':unk_list}
		print(output)


		return json.dumps(output)

	except Exception as ex:
		traceback.print_exc()

if __name__ =='__main__':
	app.run(host='0.0.0.0', port=5050, debug=True)

