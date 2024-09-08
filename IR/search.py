from collections import defaultdict
from text_operations import preprocess_text

def search(query, inverted_index):
    words = preprocess_text(query)
    results = defaultdict(int)
    for word in words:
        for doc_id in inverted_index.get(word, []):
            results[doc_id] += 1
    return sorted(results.items(), key=lambda x: x[1], reverse=True)

# Example search
if __name__ == "__main__":
    documents = {
        1: "Magaalada Laascaanood ayaa dagaal ka dhacay.",
        2: "Doorashada Puntland ayaa lagu soo dhoweeyey.",
        3: "Magaalada Qabridahar waxay leedahay taariikh dheer.",
    }
    inverted_index = create_inverted_index(documents)
    query = "magaalada dagaal"
    print(search(query, inverted_index))
