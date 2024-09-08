### Somali Search Engine
This is a simple Somali language search engine that allows users to search for specific terms within a collection of Somali text documents.
The documents are dynamically loaded from text files stored in the somali_ir_evaluation_corpus folder.

This project has been an insightful journey into the world of information retrieval, natural language processing, and web development.

Before diving into the technical details, I would like to share some background information on the Somali language and its significance.

### Background Information
The Somali Language: Somali is an Afro-Asiatic language belonging to the Cushitic branch. It is the mother tongue of the Somali people and is widely spoken in several countries:

**Somalia:** Somali is the official language and is spoken by nearly the entire population.

**Ethiopia:** In the Somali region of Ethiopia, Somali is a widely spoken language.

**Kenya:** The Somali community in Kenya, particularly in the North Eastern Province, speaks Somali.

**Djibouti:** Somali is one of the national languages.

**Somali Diaspora:** There are significant Somali-speaking communities in countries such as the United States, Canada, the United Kingdom, Sweden, Norway, and many others due to migration.

Given the widespread use of the Somali language, there is a growing need for digital tools that support Somali text processing. This project aims to address one such need by developing a search engine tailored for Somali documents.

### Project Overview
The primary goal of this project is to create a functional search engine for Somali text documents. The main components of the project include:

**Text Processing:**

This involves preparing the text data by cleaning and structuring it for efficient indexing and searching.

Key steps include loading and removing stopwords (common words that should be ignored in searches).
Indexing:

Creating an efficient data structure that maps words to the documents they appear in.

This helps in quickly finding documents that contain specific words.

**Searching:**
Finding and retrieving documents that match the user's search query.
This involves processing the query, matching it against the index, and returning relevant documents.

**Web Interface:**

Providing a user-friendly interface where users can input their queries and view the search results.
This is implemented using Flask, a lightweight web framework for Python.

### Project Structure
The project is organized into several components:

**static/:** Contains the CSS file for styling the web pages.
**templates/:** Contains the HTML templates for the home page and results page.
**app.py:** The main Flask application file.
**index_creator.py:** Script for creating the index from the text documents.
**search.py:** Script for handling the search functionality.
**Som_index_creator.py:** Additional indexing functionality if required.
**Somali_Stop_Words.txt:** File containing the stopwords in the Somali language.
**text_operations.py:** Script for text processing operations like loading and removing stopwords.

### How It Works
**Setup**:

Create and activate a virtual environment.
Install Flask using pip.

**Text Operations:**

Load stopwords from the Somali_Stop_Words.txt file.
Remove stopwords from text using the text_operations.py script.

**Index Creation:**

Use the index_creator.py script to create an index mapping words to documents.

**Searching:**

Use the search.py script to search for documents that match the user's query.

**Web Interface:**

Use app.py to set up a Flask web application.

The home page (index.html) allows users to input their search queries.

The results page (results.html) displays the documents that match the search query.

**Running the Application:**

Start the Flask server by running python app.py.
Open a web browser and navigate to http://127.0.0.1:5000/ to use the search engine.

### Conclusion
This project demonstrates the integration of various components to build a functional search engine tailored for Somali text documents. It showcases the importance of information retrieval and natural language processing in creating digital tools that support widely spoken languages like Somali.

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

#### Acknowledgments
Special thanks to **Abdisalam Badel** for providing the Somali Information Retrieval Corpus. His work on bridging the gap between query translation and dedicated language resources for Somali has been invaluable to this project.

You can find his original work here.

https://github.com/Abdisalam-Badel/Somali-Information-Retrieval-Corpus-Bridging-the-Gap-between-Query-Translation-and-Dedicated-Langua


