from flask import Flask, request, render_template
from collections import defaultdict
from search import search
from index_creator import create_inverted_index
from text_operations import preprocess_text
import os

app = Flask(__name__)

# Function to read multiple text files and load the content into the documents dictionary
def load_documents():
    documents = {}
    base_path = 'D:/MASTER/IR/somali_ir_evaluation_corpus/'  # Update with your path
    files = ['Som-0001.txt', 'Som-0002.txt', 'Som-0003.txt', 'Som-0004.txt', 'Som-0005.txt', 'Som-0006.txt', 'Som-0007.txt', 'Som-0008.txt', 'Som-0009.txt', 'Som-0010.txt', 'Som-0011.txt', 'Som-0012.txt', 'Som-0013.txt', 'Som-0014.txt', 'Som-0015.txt', 'Som-0016.txt']  # List of your text files
    for i, file_name in enumerate(files, 1):
        try:
            with open(os.path.join(base_path, file_name), 'r', encoding='utf-8') as file:
                content = file.read()
                documents[i] = content.strip()
        except UnicodeDecodeError:
            # Try a different encoding if utf-8 fails
            with open(os.path.join(base_path, file_name), 'r', encoding='ISO-8859-1', errors='ignore') as file:
                content = file.read()
                documents[i] = content.strip()
    return documents

# Load documents from text files
documents = load_documents()

# Create the inverted index using the loaded documents
inverted_index = create_inverted_index(documents)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_route():
    query = request.form['query']
    results = search(query, inverted_index)
    return render_template('results.html', query=query, results=results, documents=documents)

if __name__ == '__main__':
    app.run(debug=True)
