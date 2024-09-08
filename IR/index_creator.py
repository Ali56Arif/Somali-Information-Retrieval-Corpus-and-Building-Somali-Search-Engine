from collections import defaultdict
from text_operations import preprocess_text

def create_inverted_index(documents):
    inverted_index = defaultdict(list)
    for doc_id, text in documents.items():
        words = preprocess_text(text)
        for word in words:
            inverted_index[word].append(doc_id)
    return inverted_index
