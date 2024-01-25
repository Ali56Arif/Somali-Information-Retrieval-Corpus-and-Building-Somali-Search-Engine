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
10) evaluation.py: is the file that holds scripts used to evaluate the performance.



# Usage

Please run the Evalaution.py file and exchange the two file names that hold the values of the two models. If you want to 
use the TF-IDF the file name must be TF-IDF-Evaluation and if you want to use the PRF the file name must be 
PRF-Evaluation, these two files are inside the Evaluation.py.

After downloading please change the folder name to Somali_IR_Evaluation_Corpus


