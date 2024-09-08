### Somali Search Engine
This is a simple Somali language search engine that allows users to search for specific terms within a collection of Somali text documents.
The documents are dynamically loaded from text files stored in the somali_ir_evaluation_corpus folder.

##### Image One
![image](https://github.com/user-attachments/assets/7e9d500b-1db4-416e-a857-87bcdc7f6047) . 

#### Result
![image](https://github.com/user-attachments/assets/3a52ea92-522b-411a-9aad-324941a8742d)





#### Features
Loads text documents from multiple files located in a specific directory.

Creates an inverted index for fast searching.

Allows users to input search queries via a web interface.

Displays results that match the search query, highlighting relevant documents.

Supports searching across multiple documents at once.

#### Prerequisites
To run this project, you will need to have the following installed on your system:

Python 3.x
Flask
Necessary Python packages (listed in requirements.txt if applicable)

#### How to Use
Clone this repository:

bash
Copy code
```
git clone https://github.com/Ali56Arif/Somali-Information-Retrieval-Corpus-and-Building-Somali-Search-Engine.git
```
Navigate to the project directory:

bash
Copy code
```
cd somali-Information-Retrieval-Corpus-and-Building-Somali-Search-Engine/IR
```
Make sure the text files (e.g., Som-0001.txt, Som-0002.txt, etc.) are located in the directory /somali_ir_evaluation_corpus or update the base_path in the app.py to match your own file path.

#### Install the required dependencies:

bash
Copy code
```
pip install -r requirements.txt
```

Run the Flask application:

#### bash
Copy code
python app.py

```
Open your browser and navigate to http://127.0.0.1:5000/.
```

Enter your search query in the search box and press "Search" to see the relevant documents.

## Project Structure
**app.py**: The main application file that contains the Flask web server and handles loading the documents and search queries.

**somali_ir_evaluation_corpus**: This directory contains the Somali text files that are indexed for search.

**search.py**: The script responsible for processing search queries and returning results.

**index_creator.py**: Creates an inverted index from the loaded documents to allow for fast searching.

templates/: Contains the HTML templates (index.html, results.html) used for the web interface.

#### Acknowledgments
Special thanks to **Abdisalam Badel** for providing the Somali Information Retrieval Corpus. His work on bridging the gap between query translation and dedicated language resources for Somali has been invaluable to this project.

You can find his original work here.

https://github.com/Abdisalam-Badel/Somali-Information-Retrieval-Corpus-Bridging-the-Gap-between-Query-Translation-and-Dedicated-Langua


