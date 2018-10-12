

#I choose topic sport health, sports and  internet

topic = ["sports","health","Internet"]

sport_name_person = ['badminton','football','tennis','table_tennis','golf','swimming','cricket','baseball','basketball']

question_with_tamplate = {'sport':{
						'question_temmplate': sport_question_template, 'mapping': {'<UNK>': sport_name_person}},

						'health':{
						'question_temmplate':health_question,'mapping':{ '<HEL>':health_, '<MED>' :medicine_list}},

						'Internet':
						{'question_temmplate': internet_question}, 'mapping':{'<TOK>':tokens, '<EQU>':equipment}

						}

sport_question_template = {

"what you know about <UNK>" :['<UNK> is good but i donot know anything ',
								'I do not know anything about <UNK>',
								'I am not more interested in <DOMAIN>',
								'I am not aware of <UNK>',
								'I like <DOMAIN> but sorry i do not know for <UNK>',
								'it seems you like <DOMAIN>',
								'Do you like <DOMAIN>. I mean you like <UNK>'],



"<UNK> is good sport to play what you think":['<UNK> is good sport but i have no idea about it',
												'I think <UNK> is good but not more interested in <sport>',
												'Do you play <UNK>?',
												'i think you like <DOMAIN>'],

"when the next match of <UNK>":['I do not know when the next match is',
								'no idea for next match of <UNK>',
								'do you like watch <UNK> ?',
								'<UNK> is good sport but honestly no idea about matches',
								'no idea for next match '],

"when the next match of <PER>": ['I do not know when the next match is',
								'no idea for next match of <PER>',
								'do you like watch <PER> ?',
								'<PER> is good  but honestly no idea about matches',
								'no idea for next match ',
								'what you think about <PER>',
								'do you like <PER>'],


"what is your review for last match of <UNK>" :['I did not watch last match',
												'I did not watch last match so i have bo review ',
												'Do you like <UNK>',
												'Do you like <DOMAIN>',
												],
"last match of <PER> is awesome" : ['i did not watch the last match of <PER> ',
									'do you enjoy last match of <PER>',
									'<PER> is best but i have no much idea about <DOMAIN>',
									'Do you like <DOMAIN>'],

"what you think which country play good <UNK>": ['I do not know which country play well <UNK>',
												'what you think which country play good <UNK>',
												'I think you like <UNK>',
												'do you like <DOMAIN>'],

"play <UNK>, we need lots of energy": ['I never play <UNK>',
										'do you play <UNK>',
										'every sports need spots need lots of energy'],

"where i get live telecast of <UNK> match",['you line to watch live <UNK> match',
										'Do you like watch match',
										'I have no idea about live telecast of <UNK> match',
										'Do you <UNK> match'],

"currently which tournament of <UNK> is going on " : ['I have no idea about tournament',
											'I do not watch any tournament',
											'do you like <DOMAIN>',
											'do you enjoy <UNK> tournament'],

'I belive <PER> is best in <UNK>' :['I do not know more about <PER>',
									'I am not more interested in <UNK>',
									'DO you like <UNK>',
									'Do you like <DOMAIN>','I have no idea about <PER>','Sorry no idea about <UNK>',
									'you are fan of <PER>'],


"Who is the best player of <UNK> in the world " : ['Do you like <UNK>','I have know idea about best player of the <UNK>',
												'what you feel who is the best player of <UNK>',
												'do you play <UNK>',
												'It is difficult to decide the best player of <UNK>',
												'I have no idea about <UNK>',
												'I have no idea about player',
												'are you playing <UNK>',
												'<DOMAIN> is good topic to talk. but i am not aware of <UNK>'],

"tell me the player of the year for <UNK>": ['sorry i can not recall',
									'I do not know the player of the year for <UNK>',
									'I have no idea about player',
									'I have zero knowledge of <UNK>',
									'I have no idea for <UNK>'],

"Who is winner of the last night match of <UNK>" : ['I usually do not watch <UNK> match',
													'I am not aware of the winner of the match',
													'do you watch match last night?',
													'do you like to watch <UNK> match'],

"who is world champion team of <UNK> last year" : ['I have no idea about last year winner',
												'i do not watch <UNK> matches',
												'no idea about champion team in <UNK>',
												'do you enjoy <UNK>',
												'you like like <DOMAIN>'],

"what are over/under for the win by <UNK> team this season" : ['i do not know anything about this season',
														'I do not watch <UNK>'],

"what are the basic rules to play <UNK>" :['I do not know basic rules to play <UNK>',
									'I never play <UNK>',
									'Do you play <UNK>',
								'Do you like <UNk> i mean you are interested in <DOMAIN>'],

"what is the best place to play <UNK> in <CITY>" :['you are asking related to <UNK> ',
											'<DOMAIN> is good but i do not aware',
											'I have no idea about any place for <UNK>',
											'I do not play <UNK> so i have no idea about place',
											'do you want to play <UNk>','no idea for the place to play <UNK>'],

"how can i join the <UNK> team":  ['Do you want to join the <UNK> team',
									'do you like <UNK>',
									'i do not know how to join <UNK> team'],

"should <PER> allow to play this season or any season",['do yo like <PER>',
													'I am not more interested in <DOMAIN>. I have no idea about <PER>.',
													'<DOMAIN> is good but i have no idea'],

"what you think when <PER> get retired":['do you like <PER>',
										'i do not know when <PER> get retired','I have no idea when <PER> retired',
										'DO you like to talk more about <PER>'],

"who is famous athlete in <UNK> and why" :['no idea bout famous athlete in <UNK>','i am not more interested in <UNK>',
											'<UNK> is good but i have no idea about athlete',
											'i am not more interested in <DOMAIN> '],

"give me list of famous tournament of <UNK> ":['no idea about any tournament of <UNK>',
												'do you like to watch <UNK> tournament',
												'i am not interested in <UNK> ',
												'do you like tournament']
}



health_ = ['head che','stomach pain','acne','heart pain','body pain','depression','stress','cancer','fewer','cold','infection','high sugar',
			'blood pressure','dental issue','anxiety problem','skin diseases','negativity','foot pain']
medicine_list =['Amitriptyline','Cyclizine','Midazolam','Hyoscine hydrobromide','Atropine','Lorazepam']


health_question ={
	'by the way i am suffering from <HEL> last four to five days what should i have to do':['you will get well soon from <HEL>',
																	'i am never suffering from <HEL>','i am sorry can not guide for health issue'
																	'last four five days is not so good for you.'],

	'how to over come from <HEL> . tell me some fastest way to overcome from <HEL>' :['how long you suffering from <HEL>',
																'i do not know any fastest way to overcome from <HEL>',
																'there should some way to fastest overcome from <HEL> but i do not know',
																'I do not have any idea about health related stuff'],

	'can you tell me basic treatment for <HEL>' :['how long you suffering from <HEL>',
												'sorry i do not know any treatment for <HEL>',
												'i do not any basic treatment for <HEL>',
												'i sorry i do not have any idea for <DOMAIN> stuff'],

	'give me list of some best doctor for <HEL>' : ['I am sorry i do not know any doctor here',
													' i do not have any list of doctor for <HEL>',
													'are you suffering from <HEL>',
													'do you want to concern doctor for <HEL>?',
													'do you need to go doctor for <HEL>'],


	'tell me which hospital i can visit for <HEL>' :['Do you want to answer for <DOMAIN> related stuff',
													'i am sorry i have no idea about hospital',
													'do you want to visit hospital for <HEL>'],

	'can you suggest some home remedies for <HEL>':['i have no idea for home remedies',
													'I am not good person to answer you',
													'I can not suggest you any home remedies',
													'I have no idea for home remedies for <HEL>'],

	'i think i have to concern some doctor for <HEL>. Can you suggest me doctor ?':['I have no idea which doctor is good for <HEL>'
													'are you suffering from <HEL>',
													'how long did you suffering from <HEL>',
													'i belife doctor must help you',
													'for <HEL>, its better to concern doctor'],

	'tell me list of hospital in near by area ' : ['no idea for hospital in this area',
												'are you planning to visit hospital',
												'are you no feeling well ?',
												'I can not reply anything related to <DOMAIN>'],


	'what are the basic symptoms for <HEL>' : ['I do not know what are the basic symptoms for <HEL>',
											'are you suffering from <HEL> ?',
											'answer related to <DOMAIN> is bit difficult for me',
											'no idea for <HEL> symptoms'],

	'how should i avoid <HEL> and live happy life': ['i do not know how you avoid <HEL>',
												'always better to avoid <DOMAIN> issue'
												'i am not much aware of <DOMAIN> related stuff'],

	'How much <MED> i have to take in days.' : ['i can not answer your this question',
												'you should ask some expert to know how much <MED> you should take',
												'i can not guide you for <DOMAIN>'],

	'my age is 22. according to my age group how much <MED> dose i should take per day' : ['age group is matter but i do not have any idea for <MED>',
													'are you suffering from <DOMAIN> issue ?',
													'i hope you get well soon',
													'I have zero knowledge for <DOMAIN>'],

	'how should i make <HEL> go away':['I have no idea about <HEL>',
										'you should take care of <HEL>',
										'how long do you suffering from <HEL>',
										'for <DOMAIN> related question, i do not help you'],

	'i feel i have <HEL> what should i have to do ':['I have no idea about <HEL>',
										'you should take care of <HEL>',
										'how long do you suffering from <HEL>',
										'for <DOMAIN> related question, i do not help you'],

	'what is the best way to fight <HEL>' : ['i do not know the best way to fight <HEL>',
										'i have no idea how to fight with <HEL>',
										'talk about <DOMAIN> is good but i have no idea <HEL>'],

	'what things i have to remember so that i never suffer from <HEL> in a life.' :['i wish you never suffer from <HEL>',
										'its really bad if person suffer from <HEL>',
										'i can not help you in <DOMAIN>',
										'have you ever suffering from <HEL> ?'],

	'how to get rid of <HEL>' : ['i do not now how to get rid of <HEL>',
								'no idea about <HEL>',
								'do not know anything related to <DOMAIN>'],

	'can i die because of <HEL>':['no idea that person can die because of <HEL>'.
									'no knowledge related to <HEL>',
									'are you suffering from <HEL>'],

	'what are the possible reason for the <HEL>' :['no idea what can be the reason for <HEL>',
											'are u suffering from <HEL>',
											'i can not tell you the possible reason for <HEL>'],

	'can you please tell me what are the possible reason that people suffering from <HEL>':['no idea what can be the reason for <HEL>',
											'are u suffering from <HEL>',
											'i can not tell you the possible reason for <HEL>'],

	'how can i reduce the weight so i can wear any kind of clothes':['I have no idea how you reduce weight',
											'I can not answer regarding <DOMAIN>',
											'do you want to reduce weight'],
	'how can i gain weight :' :['do you want to gain the weight',
							'i have no information about weight gaining',
							'i do not know how to gain the weight',
							'sorry i have no idea about this'],

	'generally people are scar from surgery can tell me why':['I do not know why people scar from surgery',
														'are you ever scar from surgery '],

	'which kind of food should take while suffering from <HEL>' : ['no idea which food you should take while suffering from <HEL>',
															'are you suffering from <HEL>',
															'i can not help you in the <HEL>',
															'<DOMAIN> i never understood'],

	'what are some best source of energy. i mean which food provide good source of energy ': ['i do not know whic food provide good amount of energy',
												'I do not know what is the good source of energy',
												'i have no idea for <DOMAIN>'],

	'what to do if i want to overcome from <HEL> within three four days':['how long you suffering from <HEL>',
																'i do not know how to overcome from <HEL>',
																'there should some way to overcome from <HEL> but i do not know',
																'I do not have any idea about health related stuff'],

	'what are the possible herbal treatment for <HEL> ': ['how long you suffering from <HEL>',
												'sorry i do not know any herbal treatment for <HEL>',
												'i do not any treatment for <HEL>',
												'i sorry i do not have any idea for <DOMAIN> stuff'],


	'can you tell me some side effect for <MED>' : ['i do not know what are the side effect for <MED>',
												'I have no idea about <MED>',
												'I am not aware of <MED>',
												'Its better if you avoid question related to <DOMAIN>'],

	'tell me name of exercises that io have to do regularly':[ 'i do not know more about exercises',
															'I have no idea about exercises',
															'this is good question but i can not help in <DOMAIN>'],

	'how should doctor treat with patients who is suffering from <HEL>':['i do not how should doctor treat with patients',
														"are you want me to answer related to <DOMAIN>",
														'I have no idea about this']

}




tokens = ['learning python', 'learning photography','machine learning tutorial','generating animation','chatting','advertising', 'blog reading','publish blog']

equipment = ['computer','laptop','head phones','speaker','keyboard','hard drive','pen drive','mouse']
software = ['excel','microsoft word','oracle','vlc media player','paint','pdf maker']
password =['facebook', 'desktop','google','slack','laptop','mobile']
internet_question =

{
	'best brand for purchasing a new <EQU>':['would you like to purchase a <EQU>',
											'i do not know any brand for <EQU>',
											'I am not aware of <DOMAIN> things',],
	'give me list of best site for <TOK>' :['you are interested in <TOK>',
											'i am not aware for the site for <TOK>','i am not aware of <TOK>'],

	'I want to purchase <EQU>. what you think which brand is best':['DO you want to purchase <EQU>',
												'I have no idea for which brand is best for <EQU>',
												'I think this <DOMAIN> related stuff. I can not help you'],
	'what is the best way to clean <EQU>':['Do you have <EQU>',
											'i am not aware how to clean <EQU>',
											'i do not know how to clean <EQU>',
											'I am not able say anything related to <DOMAIN>'],

	'what feature you have to check while you are going for buy <EQU>' : ['I am not aware for all feature for <EQU>',
										'are you going to buy <EQU>',
										'no idea which feature you have to check for <EQU>'],

	'what you think how internet help you ':['i do not know how internet help you'],

	'what are the some best site you have to visit everyday' :['do you want to visit sites everyday?',
										'i do not know which site you have to visit'],

	'which internet browser i have to used to get good speed':['i am not aware of this',
										'I am not aware of all the internet browser',
										'which browser do you like to use'],

	'how can i reset password for <PWD> ':['do you want to reset password','are you using <PWD>'
										'i even do not know how to reset the password'],

	'can you tell me how to use <SOF>': ['i am not aware of how to use <SOF> ',
										'do you like to use <SOF> ?',
										'i can not help you how to use <SOF>'],

	'tell me some approximate cost for <EQU>' : ['I have no idea for the cost of <EQU>',
												'Do you want to purchase <EQU>'],

	'what are the best <EQU> which i get in reasonable price ': ['i do not know what are the best <EQU>',
											'I am not aware of price for <EQU>',
											''],

	'where can i buy <EQU> for my mac book':[],

	'who invented the <EQU>':['I do not know who invented the <EQU>',
							'Do you use <EQU>',
							'I am not more interested in <DOMAIN>'],

	'what are the best use of <SOF>' :['do you like to use <SOF>',
										'i do not know what is the best use of <SOF>'],

	'which company manufacture best <EQU>':[],
	'can you give me some basic tutorial for <SOF>':[],
	'which website gives me some basic information for <TOK>' : [],
	'how can i clean my mail box':[],
	'how can i connect my phone to television monitor':[],
	'best site to download the software':[],
	'I want to install <SOF> . can you suggest me some good online resource' :[],
	'From how far away is a Wi-Fi connection accessible ?' :[]


}