

#I choose topic sport health, sports and  internet
import pickle

topic = ["sport","health","Internet"]

sport_name_person = ['badminton','squash','football','tennis','table_tennis','golf','swimming','cricket','baseball','basketball']

person_name = ['Prakash_Padukone','Zaheer_khan','Mouma_das','sachin_tendulkar','sakshi_malik','rohan_bopanna','lewis','usain_bolt','lionel_messi','rafael_nadal',
'serena_williams','samir_verma','srikant_kidambi','lakshay_sen','lee_choang_wei','lin_dan','kevin']

list_of_topics = ['hair_skin_beauty','medicine','movie','adult','small_talk','health','online_shopping']

sport_question_template = {

"what do you know about <UNK> " :['<UNK> is good but i do not know anything ',
								'I do not know anything about <UNK>',
								'basically am not more interested in <DOMAIN>',
								'I am not aware of <UNK>',
								'actually like <DOMAIN> but sorry i do not know more about <UNK>',
								'it seems you like <DOMAIN>',
								'I am not really interested in <DOMAIN>', 
								'not able to find anything related to <DOMAIN> sorry.', 
								'I could not find anything related to <UNK>', 
								"familiar with <DOMAIN>, but not <UNK>. sorry.",
								'actually i not curious about <UNK>'],


'lakshay_sen is playing as impressive as sri and lin_dan ':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'sorry to say i am not aware of this things',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

'what you think about sports like gymnastics, shotting, boxing etc. ':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],


"<UNK> is good sport to play, what do you think ":['<UNK> is good sport but i have no idea about it',
												'I think <UNK> is good but not more interested in <sport>',
												'Do you play <UNK> ?',
												'i think you like <DOMAIN>', 
												'you are absolutely right, about <UNK> sorry no idea', 
												'I love learning about <UNK>', 
												'Could you teach me about <UNK>?'],

"when is the next match of <UNK> ":['I do not know when the next match is',
								'no idea for next match of <UNK>',
								'do you like to watch <UNK> ?',
								'<UNK> is good sport but honestly no idea about matches',
								'I have absolutely no idea about the next match though.', 
								"Sorry, I do not keep up with <UNK>"],

"when is the next match of <PER> ": ['I do not know when the next match is',
								'no idea for next match of <PER>',
								'do you like to watch <PER> ?',
								'<PER> is good  but honestly no idea about matches',
								"no idea about <PER>'s next match",
								'what do you think about <PER>',
								'do you like <PER>', 
								'Never knew you liked <PER>', 
								"I've heard <PER>'s a good player, but not exactly sure when the next match is"],

'sakshi malik saina nehwal kshayap all are good student of pullela gopichand ':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

'can i asked some studied question like what you think about ':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],


"what is your review for the last match of <UNK> " :[' not watch the last match',
												'I did not watch the last match so i have no review ',
												'nothing i know about <UNK>',
												'Do you like <DOMAIN> but sorry no idea more about <DOMAIN>',
												'Sorry, i forgot to watch the last match', 
												"That's a tough question!", 
												"whatever you this i belive its right because i have no much idea about <DOMAIN> "
												],

"last match of <PER> is awesome " : ['i did not watch the last match of <PER> ',
									'did you enjoy the last match of <PER>',
									'not more interested in <DOMAIN> so no idea about <PER>',
									'<PER> seems like the  best player but i have no idea about <DOMAIN>',
									'you like <DOMAIN> is good but i do not', 
									"I would love to watch <PER> play."],

"what do you think, which country play's good <UNK> ": ['not know which country play well in <UNK>',
												'what do you think?',
												'difficult for me to answer regarding <UNK>',
												'its tough for me to say anythin about <UNK>',
												'without knowledge of <DOMAIN> how can i talk about <UNK>',
												'I think you like <UNK> but sorry',
												'can not say anything more about <UNK>', 
												"i trust on your choice, who do you favour?", 
												"try to tell you if i knew"],

"to play <UNK>, we need lots of energy ": ['I never play <UNK>',
										'do you play <UNK>?','<DOMAIN> is topic which i used too avoid',
										'to play any sports you need lots of energy'],

"where do i get live telecast of <UNK> match " :['you like to watch live <UNK> match',
										'sorry but no idea about live telecast',
										'if i know i will let you know',
										'<DOMAIN> is topic i usually avoid to talk'
										'Do you like watch match',
										'I have no idea about live telecast of <UNK> match',
										' you <UNK> match', 
										"I'd tell you if i knew"],

"currently which tournament of <UNK> is going on " : ['honestly no idea about tournament',
											'I do not watch any tournament',
											'it seems you like <DOMAIN> but i don\'t ', 
											"I'd tell you if i knew", 
											"sorry, I dont follow <UNK>"],

'I belive <PER> is best in <UNK> ' :['not know more about <PER>',
									'I am not more interested in <UNK>',
									' you like <UNK>',
									'question related to <DOMAIN> i guess but i sorry i have no idea',
									'have no idea about <PER>','Sorry no idea about <UNK>',
									'you are fan of <PER>', 'belive me i am not right bot to talk about <DOMAIN>',
									'<DOMAIN> is topic which i dont like to talk',
									"I trust on you'\r judgement"],
	
"Who is the best player of <UNK> in the world " : ['Do you like <UNK>',
												'I have know idea about best player of the <UNK>',
												'what you feel who is the best player of <UNK>',
												'do you play <UNK>',
												'It is difficult to decide the best player of <UNK>',
												'I have no idea about <UNK>',
												'no idea about player',
												'are you playing <UNK>',
												'<DOMAIN> is good topic to talk. but i am not aware of <UNK>'],

"tell me the player of the year for <UNK> ": ['sorry i can not recall',
									'the player of the year for <UNK> ???? sorry cant answer this',
									'no knowledge about any player in <UNK>',
									'if i get answer i will let you know',
									'its better if you dont ask me anything regarding <DOMAIN>',
									'have zero knowledge of <UNK>',
									'I have no idea for <UNK>'],

"Who is winner of the last night match of <UNK> " : ['I usually do not watch <UNK> match',
													'I am not aware of the winner of the match',
													'do you watch match last night? i dont like <UNK>','belive me i am not right bot to talk about <DOMAIN>',
													'you like to watch <UNK> match but i dont like <DOMAIN>'],

"who is world champion team of <UNK> last year " : ['I have no idea about last year winner',
												'i do not watch <UNK> matches',
												'no idea about champion team in <UNK>',
												'i dont much enjoy <UNK>',
												'its better if you dont ask me anything regarding <DOMAIN>',
												'can help in <DOMAIN> related question'],

"what are over/under for the win by <UNK> team this season " : ['i do not know anything about this season',
														'I do not watch <UNK>','not more interested in <UNK>',
														'its good if you dont ask me <UNK> related stuff',
														'do not ask me something related to <UNK>'],

"what are the basic rules to play <UNK> " :['I do not know basic rules to play <UNK>',
									'I never play <UNK>','its <DOMAIN> related question','belive me i am not right bot to talk about <DOMAIN>',
									'seems you are interested in playing <UNK>',
								'Do you like <UNK> i mean you are interested in <DOMAIN>'],

"what is the best place to play <UNK> in <CITY> " :['you are asking related to <UNK> ',
											'<DOMAIN> is good but i do not aware',
											'I have no idea about any place for <UNK>',
											'I do not play <UNK> so i have no idea about place',
											'do you want to play <UNk>',
											'no idea for the place to play <UNK>'],

"how can i join the <UNK> team":  ['Do you want to join the <UNK> team',
									'do you like <UNK>',
									'i do not know how to join <UNK> team'],

"should <PER> allow to play this season or any season" : ['do you like <PER> but i have no idea about that',
													'I am not more interested in <DOMAIN>. I have no idea about <PER>.',
													'<DOMAIN> is good but i have no idea'],

"what you think when <PER> get retired":['do you like <PER> but sorry no idea',
										'i do not know when <PER> get retired',
										'no idea when <PER> retired','belive me i am not right bot to talk about <DOMAIN>',
										'do you like to talk more about <PER> but sorry i am not aware of that'],

"who is famous athlete in <UNK> and why" :['no idea about famous athlete in <UNK>',
											'i am not more interested in <UNK>',
											'<UNK> is good but i have no idea about athlete',
											'i am not more interested in <DOMAIN> ',
											'zero knowledge about famous athlete in <UNK>'],

"give me list of famous tournament of <UNK> ":['no idea about any tournament of <UNK>',
												'do you like to watch <UNK> tournament but i am sorry i don\'t',
												'i am not interested in <UNK> '],

"would you like to talk about <topic>":['do you interest in <topic>',
					'i am not good bot to talk about <topic>',
					'i am sorry i cant help you in <topic>',
					'Ahhh <topic> related question. sorry',
					'can i assign another bot aware of this <topic>'],


"say something related to <topic>":['do you interest in <topic>',
					'i am not good bot to talk about <topic>',
					'i am sorry i cant help you in <topic>',
					'Ahhh <topic> related question. sorry',
					'can i assign another bot aware of this <topic>'],

'i want to talk about something related to <topic>':['do you interest in <topic>',
					'i am not good bot to talk about <topic>',
					'i am sorry i cant help you in <topic>',
					'Ahhh <topic> related question. sorry',
					'can i assign another bot aware of this <topic>',
					'i am not aware of this topic ',
					'if i know anything related to this one i will let you know'],

'now actually i want to talk about someone related to <topic>':['do you interest in <topic>',
					'i am not good bot to talk about <topic>',
					'i am sorry i cant help you in <topic>',
					'Ahhh <topic> related question. sorry',
					'can i assign another bot aware of this <topic>',
					'i am not aware of this topic ',
					'if i know anything related to this one i will let you know']


}




health_ = ['head_ache','stomach_pain','acne','heart_pain','body_pain','depression','stress','cancer','fewer','cold','infection','high_sugar',
			'blood_pressure','dental_issue','anxiety_problem','skin_diseases','negativity','foot_pain']
medicine_list =['Amitriptyline','Cyclizine','Midazolam','Hyoscine hydrobromide','Atropine','Lorazepam']


health_question ={
	'by the way i am suffering from <HEL> last four to five days what should i have to do':
	['you will get well soon from <HEL>', 'i am never suffering from <HEL> so i have no idea about this',
	 'sorry i am not right person to guide you for health issue', 'last four five days is not so good for you.', "I've never really suffered from <HEL>"],


	'how to over come from <HEL> . tell me some fastest way to overcome from <HEL>' :['how long your suffering from <HEL>',
																'not know any fastest way to overcome  <HEL>',
																'there should be some way to fastly overcome  <HEL> but i do not know',
																'I do not have any idea about health related stuff', 
																'zero idea about <DOMAIN> related stuff',
																'actually i am not aware of this things',
																"I'd tell you if i knew."],

	'i am curious to know more about stomach_infection , throat_infection, viral_fewer ':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

	'ops i want to know about something irrelavant want to check can you help me':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

	'Apollo , medpub , netmeds and medpubmart provide good medical delivery services':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

	'what you thing about specailist like Cardiologists, Dermatologists , Gastroenterologists  in Apollo hospital':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

	'can you tell review for hospital like parekh , vadilal , kg , mamta':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

	'give me an idea for different vaccine':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],


	'can you tell me basic treatment for <HEL>' :['from how long are you suffering from <HEL>',
												'sorry i do not know any treatment for <HEL>',
												'i do not know any basic treatment for <HEL>',
												'i sorry i do not have any idea for <DOMAIN> stuff', 'belive me i am not right bot to talk about <DOMAIN>',
												 "I'd tell you if i knew."],

	'give me list of some best doctors for <HEL>' : ['I am sorry i do not know any doctor here',
													' i do not have any list of doctor for <HEL>',
													'are you suffering from <HEL> but sorry i cant help you',
													'do you want to concern doctor for <HEL>? in that case i can not help you sorry',
													'honestly i have no idea about doctor', 
													'its better if you avoid <DOMAIN> related stuff',
													"I'd tell you if i knew.",
													'actually i am not aware of this things', 
													"I might not be the best to take advice from, regarding this"],


	'tell me which hospital i can visit for <HEL>' :['Do you want me to an answer for <DOMAIN> related stuff? i will i am too dump for that',
													'sorry i have no idea about hospital','belive me i am not right bot to talk about <DOMAIN>',
													'do you want to visit hospital for <HEL>', 
													"I'd tell you if i knew.", 'actually i am not aware of this things'],

	'can you suggest some home remedies for <HEL>':['i have no idea for home remedies',
													'I am not good person to answer you',
													'belive me i am not right bot to talk about <DOMAIN>',
													'I can not suggest you any home remedies',
													'I have no idea for home remedies for <HEL>', 
													"I'd tell you if i knew.", 
													"you should really visit a doctor, you know?"],

	'i think i have to concern some doctor for <HEL>. Can you suggest me doctor ?':['I have no idea which doctor is good for <HEL>'
													'are you suffering from <HEL> that\'s bad but sorry cant help you ',
													'i belive doctor must help you','belive me i am not right bot to talk about <DOMAIN>',
													'actually i am not aware of this things',
													'for <HEL> related query, please try to avoid'
													'for <HEL>, its better to concern doctor'],

	'tell me list of hospital in near by area ' : ['no idea for hospital in this area',
												'are you planning to visit hospital sorry i cant help you ',
												'zero knowledge about hospital in near me',
												'if i get to know i will inform you',
												'bit difficult for me to answer this question',
												'I can not reply anything related to <DOMAIN>'],


	'what are the basic symptoms for <HEL>' : ['I do not know what are the basic symptoms for <HEL>',
											'are you suffering from <HEL> ?','I dont know anything about <HEL>',
											'its really tough question for me','try to avoid asking me anything about <HEL>',
											'i feel <DOMAIN> is topic where i dont aware of anything',
											'answer related to <DOMAIN> is bit difficult for me',
											'no idea for <HEL> symptoms','very less idea anything related to <HEL>', 
											'actually i am not aware of this things'],

	'how should i avoid <HEL> and live happy life': ['i do not know how you avoid <HEL>',
												'always better to avoid <DOMAIN> issue','actually i am not aware of this things',
												'not much aware of <DOMAIN> related stuff','very less knowledge regarding <DOMAIN>',
												'its better if you do not ask <DOMAIN> related question',
												'do not know what to do to live happy life','If i know i will tell you'],

	'How much <MED> i have to take per days.' : ['i can not answer your this question','no idea how much you should take <MED>',
												'you are not asking me right question. it seems something related to <HEL>',
												'you should ask some expert to know how much <MED> you should take',
												'belive me i am not right bot to talk about <DOMAIN>',
												'actually i am not aware of this things',
												'i can not guide you for <DOMAIN>',
												 "you should really visit a doctor, you know?", 
												 "I'd tell you if i knew"],

	'my age is 22. according to my age group how much <MED> dose i should take per day' : ['age group is matter but i do not have any idea for <MED>',
													'are you suffering from <DOMAIN> issue ? sorry i cant help you',
													'i hope you get well soon',
													'I have zero knowledge for <DOMAIN>', 
													"I'd tell you if i knew.", 
													"you should really visit a doctor, you know?"],

	'how should i make <HEL> to go away':['I have no idea about <HEL>',
										'you should take care of <HEL>',
										'i have no idea about <HEL> else i definately help you',
										'i can not answer anything related to <DOMAIN>',
										'bit difficult question for me because it belong from <DOMAIN>',
										'i wish <HEL> is go away but dint know how','belive me i am not right bot to talk about <DOMAIN>'
										'for <DOMAIN> related question, i do not help you'],

	'i feel i have <HEL> what should i have to do ':['I have no idea about <HEL>',
										'you should take care of <HEL> but what care i dont know',
										'for <DOMAIN> related question, i do not help you',
										'i found it tough for me to talk about something related to <DOMAIN>',
										'zero idea about <HEL> ',
										'to talk about <HEL> is difficult for me',
										'actually i am not aware of this things'
										],

	'what is the best way to fight <HEL>' : ['i do not know the best way to fight <HEL>',
										'i have no idea how to fight with <HEL>',
										'talk about <DOMAIN> is good but i have no idea <HEL>',
										'for <HEL> related question, i do not help you'],

	'what things i have to remember so that i never suffer from <HEL> in a life.' :['i wish you never suffer from <HEL>',
										'its really bad if person suffer from <HEL>',
										'i can not help you in <DOMAIN>',
										'actually i am not aware of this things'],

	'how to get rid of <HEL>' : ['i do not now how to get rid of <HEL>',
								'no idea about <HEL>','actually i am not aware of this things','belive me i am not right bot to talk about <DOMAIN>',
								'do not know anything related to <DOMAIN>',
								'for <DOMAIN> related question, i do not help you'],

	'can i die because of <HEL>':['no idea that person can die because of <HEL>',
									'no knowledge related to <HEL>',
									'are you suffering from <HEL>','belive me i am not right bot to talk about <DOMAIN>'
									'actually i am not aware of this things',
									'for <HEL> related question, i do not help you'],

	'what are the possible reason for the <HEL>' :['no idea what can be the reason for <HEL>',
											'are u suffering from <HEL>',
											'i can not tell you the possible reason for <HEL>'],

	'can you please tell me what are the possible reason that people suffering from <HEL>':['no idea what can be the reason for <HEL>',
											'are u suffering from <HEL>',
											'not able to tell you the possible reason for <HEL>',
											'try to avoid <HEL> related question',
											'its actually not qood question for me , i think'],

	'how can i reduce the weight so i can wear any kind of clothes':['I have no idea how you reduce weight',
											'I can not answer regarding <DOMAIN>',
											'do you want to reduce weight nut sorry i cant help you'],

	'how can i gain weight :' :['do you want to gain the weight',
							'information about weight gaining',
							'i do not know how to gain the weight',
							'sorry i have no idea about this',
							'actually i am not aware of this things'],

	'generally people are scar from surgery can tell me why':['I do not know why people scar from surgery',
														'are you ever scar from surgery ',
														'i found it bit weird question form me'],

	'which kind of food should take while suffering from <HEL>' : ['no idea which food you should take while suffering from <HEL>',
															'are you suffering from <HEL>',
															'i can not help you in the <HEL> related stuff',
															'<DOMAIN> i never understood',
															'actually i am not aware of this things'],

	'what are some best source of energy. i mean which food provide good source of energy ': ['not know which food provide good amount of energy',
												'I do not know what is the good source of energy',
												'i have no idea for <DOMAIN>',
												'i am not right bot to talk about this'],

	'what to do if i want to overcome from <HEL> within three four days':['how long you suffering from <HEL>',
																'no idea how to overcome from <HEL>','belive me i am not right bot to talk about <DOMAIN>',
																'there should some way to overcome from <HEL> but i do not know',
																'I do not have any idea about health related stuff',
																'its better if you dont ask me <HEL> related stuff','belive me i am not right bot to talk about <DOMAIN>'
																],

	'what are the possible herbal treatment for <HEL> ': ['herbal treatment is good honestly i have no idea',
												'sorry i do not know any herbal treatment for <HEL>',
												'no idea for <HEL> treatment','try to avoid <HEL> related question',
												'sorry i do not have any idea for <DOMAIN> stuff'],


	'can you tell me some side effect for <MED>' : ['not aware of what are the side effect for <MED>',
												'I have no idea about <MED>',
												'not aware of even <MED>',
												'feel like you asked me wrong question',
												'have zero idea about <MED> related stuff',
												'Its better if you avoid question related to <DOMAIN>', 
												"I'd tell you if i knew"],

	'tell me name of exercises that io have to do regularly':[ 'i do not know much about exercises',
															'I have no idea about exercises',
															'this is good question but i can not help in <DOMAIN>', 
															 "you should check with others who workout regularly", 
															 "sorry, I've not worked out in years!",
															 'actually i am not aware of this things'],

	'how should doctor treat with patients who is suffering from <HEL>':['how should i know that how should doctor treat with patients',
														"are you want me to answer related to <DOMAIN>",
														'I have no idea about this', 'belive me i am not right bot to talk about <DOMAIN>',
														'actually i am not aware of this things'],

	'give me some idea related to diarrhoea':['i am to bad in <DOMAIN>',
										'its better if you avoid <DOMAIN> related stuff','I have zero knowledge regarding <DOMAIN>'	],

	'would you like to talk about health':['i am to bad in <DOMAIN>',
										'its better if you avoid <DOMAIN> related stuff','I have zero knowledge regarding <DOMAIN>'	]


}




tokens = ['learning_python', 'learning_photography','machine_learning_tutorial','generating_animation','chatting','advertising', 'blog_reading','publish_blog']

equipment = ['computer','laptop','head phones','speaker','keyboard','hard_drive','pen_drive','mouse']
software = ['excel','microsoft_word','oracle','vlc_media_player','paint','pdf_maker']
password =['facebook', 'desktop','google','slack','laptop','mobile']
internet_question ={
	'best brand for purchasing a new <EQU>':['would you like to purchase a <EQU>',
											'i do not know any brand for <EQU>',
											'no know <DOMAIN> things','its better if you avoid <DOMAIN> related stuff'],

	'give me list of best site for <TOK>' :['you are interested in <TOK>',
											'for <DOMAIN> related question, i do not help you',
											'i am not aware for the site for <TOK>',
											'actually i am not aware of this things',
											'no idea about <TOK>'],

	'I want to purchase <EQU>. what you think which brand is best':['do you want to purchase <EQU>',
												'I have no idea for which brand is best for <EQU>',
												'this is <DOMAIN> related stuff. I can not help you',
												'its better if you avoid <DOMAIN> related stuff',
												'for <EQU> related question, i do not help you'],

	'what is the best way to clean <EQU>':['Do you have <EQU>',
											'not much aware of how to clean <EQU>',
											'i do not know how to clean <EQU>',
											'for <EQU> related question, i do not help you',
											'not able say anything related to <DOMAIN>','actually i am not aware of this things'],

	'what feature you have to check while you are going for buy <EQU>' : [
										'I am not aware for all feature for <EQU>',
										'are you going to buy <EQU> ??? sorry i dont have any idea',
										'no idea which feature you have to check for <EQU>'],

	'what you think how internet help you ':['i do not know how internet help you',
											'for <DOMAIN> related question, i do not help you',
											'its better if you avoid <DOMAIN> related stuff',
											'actually i am not aware of this things'],

	'what are the some best site you have to visit everyday' :['do you want to visit sites everyday? but i cant help you',
										'for <DOMAIN> related question, i do not help you',
										'i do not know which site you have to visit','belive me i am not right bot to talk about <DOMAIN>',
										'better to avoid <DOMAIN> related question'],

	'which internet browser i have to used to get good speed':['i am not aware of this',
										'I am not aware of all the internet browser',
										'its better if you avoid <DOMAIN> related stuff',
										'which browser do you like to use',
										'actually i am not aware of this things'],

	'how can i reset password for <PWD> ':['do you want to reset password',
											'are you using <PWD>',
											'its better if you avoid <DOMAIN> related stuff',
											'for <DOMAIN> related question, i do not help you',
											'i even do not know how to reset the password'],

	'can you tell me how to use <SOF>': ['i am not aware of how to use <SOF> ',
										'do you like to use <SOF> ?',
										'actually i am not aware of this things',
										'its better if you avoid <DOMAIN> related stuff',
										'not able to help you in using <SOF>'],

	'tell me some approximate cost for <EQU>' : ['I have no idea for the cost of <EQU>',
												'its better if you avoid <DOMAIN> related stuff','belive me i am not right bot to talk about <DOMAIN>',
												'actually i am not aware of this things',
												'Do you want to purchase <EQU> but i have no idea about it',
												'for <EQU> related question, i do not help you'],

	'what are the best <EQU> which i get in reasonable price ': ['i do not know what are the best <EQU>',
											'I am not aware of price for <EQU>','actually i am not aware of this things',
											"I'd tell you if i knew",
											'for <EQU> related question, i do not help you'],

	'where can i buy <EQU> for my mac book':["I'm sorry i do not know about <EQU>", 
											 "I'd tell you if i knew", 
											 'its better if you avoid <EQU> related stuff',
											 'actually i am not aware of this things'
											 "I'm not really sure ,sorry."],

	'who invented the <EQU>':['I do not know who invented the <EQU>',
							'Do you use <EQU>',
							'nothing i can say',
							'anyways i am not interested in <DOMAIN>', 
							"I'd tell you if i knew", 
							"someone who's really talented, for sure."],

	'what are the best use of <SOF>' :['do you like to use <SOF>',
										'i think it is useful but i dont have any idea. sorry',
										'its better if you avoid <DOMAIN> related stuff',
										'i do not know what is the best use of <SOF>', 
										"I'd tell you if i knew"],

	'which company manufacture best <EQU>':['I have no idea for company name',
										'I do not know which company manufacture <EQU>',
										'would you like to talk about <DOMAIN>',
										'for <DOMAIN> related question, i do not help you'],

	'can you give me some basic tutorial for <SOF>':['do yo want tutorial for <SOF>',
											'are you aware of <SOF>',
											' no idea for <SOF>',
											'actually i am not aware of this things',
											'its better if you avoid <DOMAIN> related stuff',
											'I am not aware of <SOF> tutorial'],

	'which website gives me some basic information for <TOK>' : ['i am not aware  which website help you',
								'do you want information for <TOK>',
								' i am not much aware of <TOK>','belive me i am not right bot to talk about <DOMAIN>',
								'its better if you avoid <DOMAIN> related stuff'],

	'how can i clean my mail box':['Do you want to clean mail box',
									'are you using mail box?? but i have no idea',
									'I have zero knowledge about how to clean mail box'],

	'how can i connect my phone to television monitor':['Do you want to connect phone with television monitor',
														'i do not know how to connect phone',
														'do you asked in question related to <DOMAIN> ?', 
														'I have zero knowledge regarding <DOMAIN>',
														'for <DOMAIN> related question, i do not help you' ],

	'best site to download the software':['Do you want to download the <software>',
											'i do not know any site for download', 'belive me i am not right bot to talk about <DOMAIN>',
											'not aware of this','its better if you avoid <DOMAIN> related stuff',
											'this is <DOMAIN> related stuff sorry no idea'],


	'I want to install <SOF> . can you suggest me some good online resource' :['I have no idea about any online stuff',
																		'I do not know how to install <SOF>',
																		'no idea. sorry',
																		'its better if you avoid <DOMAIN> related stuff',
																		'do you try find <SOF> resource online but sorry i can not help you'],

	'From how far away is a Wi-Fi connection accessible ?' :['you are more interested in <DOMAIN>',
					'not know how far wi-fi work',
					'i do not know how far you get wi-fi connection',
					'no knowledge for wi-fi connection','belive me i am not right bot to talk about <DOMAIN>',
					'its better if you avoid <DOMAIN> related stuff',
					'for <DOMAIN> related question, i do not help you'],


	'can you tell review for amazon flipkart myntra':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

	'which one is more preferable site for dancing ':['i am not aware of this',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ',
													'sorry to say i am not aware of this things'],

	'tell me something regarding bluetooth, wi-fi_net, 4g and 5g ':[
													'i am not aware of this',
													'i am to bad in <DOMAIN>',
													'if i know i will let u know', 
													'no idea about this',
													'better to asked me something relevant',
													'sorry can\'t say anything regarding this',
													'i want to help you but here i am fail sorry',
													'it sounds bit difficult question for me',
													'I am not good bot to answer this question',
													'i am to bad in this domain ','I have zero knowledge regarding <DOMAIN>',
													'sorry to say i am not aware of this things'],

	'tell me something related to 5gnet':['i am to bad in <DOMAIN>',
										'its better if you avoid <DOMAIN> related stuff','I have zero knowledge regarding <DOMAIN>'	]

}


question_with_tamplate = {'sport':{
						'question_temmplate': sport_question_template, 'mapping': {'<UNK>': sport_name_person,'<PER>':person_name} ,'<DOMAIN>':'sport','<topic>':list_of_topics},

						'health':{
						'question_temmplate':health_question,'mapping':{ '<HEL>':health_, '<MED>' :medicine_list} , '<DOMAIN>':'health'},

						'internet':
						{
						'question_temmplate': internet_question, 'mapping':{'<TOK>':tokens, '<EQU>':equipment, '<SOF>':software,'<PWD>': password},'<DOMAIN>':'internet'}
						}



with open('question_temmplate.pkl','wb') as f:
	pickle.dump(question_with_tamplate,f)