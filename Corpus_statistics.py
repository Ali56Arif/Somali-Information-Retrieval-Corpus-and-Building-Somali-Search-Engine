#This file reads the somali IR evaluation corpus and then prints the statistics of the corpus
#Author Abdisalam Mahamed
import glob
import nltk

nltk.download('punkt')

corpus_path = "Somali-IR-Evaluation-corpus/*.txt"

# Initialize counters
sentence_count = 0
word_count = 0
document_count = 0

# Iterate through each document in the Somali-IR-Evaluation-corpus
for file_path in glob.glob(corpus_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        document = file.read()

        # Tokenize the document into sentences
        sentences = nltk.sent_tokenize(document)
        sentence_count += len(sentences)

        # Tokenize the document into words
        words = nltk.word_tokenize(document)
        word_count += len(words)

        document_count += 1  # Increment the document count

# Calculate average statistics
average_sentences_per_document = sentence_count / document_count
average_words_per_document = word_count / document_count

# Calculate average sentence length
average_sentence_length = word_count / sentence_count

print("Number of sentences:", sentence_count)
print("Number of words:", word_count)
print("Number of documents:", document_count)
print("Average sentences per document:", average_sentences_per_document)
print("Average words per document:", average_words_per_document)
print("Average sentence length:", average_sentence_length)
