# Somali Information Retrieval Corpus: Bridging the Gap between Query Translation and Dedicated Language Resources

# This is the official GitHub for the paper: Somali Information Retrieval Corpus: Bridging the Gap between Query Translation and Dedicated Language Resources 
# In this corpus we have listed the important components as:



1) Somali IR Evaluation Corpus: holds the documents, with 2335 Somali text documents. Rename this file as Somali_IR_Evaluation_Corpus
2) Judgements: the number of documents judged against the total documents concerning the queries.
3) queries.txt: holds the queries used 16 in total.
4) Somali_Stop_Words.txt: the number of Somali stop words identified are in this file
5) Som_PRF_IR.py: this file contains the Psuedo relevance feedback technique implementation
6) Som_TF-IDF.py: the TF-IDF python file is in this file
7) PRF-Evaluation: Results after Som_PRF.py is run.
8) TF-IDF-Evaluation: holds results after successfully running Som_TF-IDF.py
9) Som_index_creator.py: if you want to re-run the whole process this file creates the index, you need to run it first.
===============================================================================================================



To use this file all you need is to first run either the Som_TF-IDF.py or Som_PRF_IR.py, to see the performance of the system after you run one of these files,
you can run evaluation.py. This file will deal with two different tasks 1) TF-IDF-Evaluation and 2) PRF-Evaluation. So when you run Som-PRF.py, the method becomes open('PRF-Evaluation', 'r') as retrieved_file: and when you run the Som.TF-IDF.py the method becomes open('TF-IDF-Evaluation', 'r') as retrieved_file:

# If you want to re-run the whole process on your own please rename the corpus as Somali_IR_Evaluation_Corpus, and start running from Som_index_creator.py, then follow the previously mentioned steps.

