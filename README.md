# sentence_generation
generate the response for out of domain query

1. QA_generation.py file help to generate question answer pair save in pickle format
2. generate_data.py generate dataset where pass parameter -t=train/test and -n=number of QA pair want
3. word_tokernized.py help its create source and target vocabulary and clean the data
4. reader.py used for prepare data for model 
5. try_sqs_with_attension.py create seq2seqmodel with attension and beam search
6. model.py used simple encoder decoder method with beam search



