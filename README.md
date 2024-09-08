### Somali Search Engine
This is a simple Somali language search engine that allows users to search for specific terms within a collection of Somali text documents. The documents are dynamically loaded from text files stored in the somali_ir_evaluation_corpus folder.

## Features
Loads text documents from multiple files located in a specific directory.
Creates an inverted index for fast searching.
Allows users to input search queries via a web interface.
Displays results that match the search query, highlighting relevant documents.
Supports searching across multiple documents at once.

## Prerequisites
To run this project, you will need to have the following installed on your system:

Python 3.x
Flask
Necessary Python packages (listed in requirements.txt if applicable)

# How to Use
Clone this repository:

bash
Copy code
git clone https://github.com/Ali56Arif/Somali-Information-Retrieval-Corpus-and-Building-Somali-Search-Engine.git
Navigate to the project directory:

# bash
Copy code
cd somali-Information-Retrieval-Corpus-and-Building-Somali-Search-Engine/IR
Make sure the text files (e.g., Som-0001.txt, Som-0002.txt, etc.) are located in the directory /somali_ir_evaluation_corpus or update the base_path in the app.py to match your own file path.

## Install the required dependencies:

# bash
Copy code
pip install -r requirements.txt
Run the Flask application:

# bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000/.

Enter your search query in the search box and press "Search" to see the relevant documents.

# Project Structure
**app.py**: The main application file that contains the Flask web server and handles loading the documents and search queries.
**somali_ir_evaluation_corpus**: This directory contains the Somali text files that are indexed for search.
**search.py**: The script responsible for processing search queries and returning results.
**index_creator.py**: Creates an inverted index from the loaded documents to allow for fast searching.
templates/: Contains the HTML templates (index.html, results.html) used for the web interface.

## Acknowledgments
Special thanks to **Abdisalam Badel** for providing the Somali Information Retrieval Corpus. His work on bridging the gap between query translation and dedicated language resources for Somali has been invaluable to this project.

You can find his original work here.

https://github.com/Abdisalam-Badel/Somali-Information-Retrieval-Corpus-Bridging-the-Gap-between-Query-Translation-and-Dedicated-Langua


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


