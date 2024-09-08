import re

# Load Somali stop words
with open('Somali_Stop_Words.txt', 'r') as file:
    stop_words = set(file.read().split())

# Example suffixes and prefixes in Somali
suffixes = ['aad', 'aan', 'ka', 'ku', 'ta', 'da', 'de', 'to']
prefixes = ['ka', 'ku', 'ma', 'u', 'si']

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = [stem_word(word) for word in words]
    return words

def stem_word(word):
    # Remove suffixes
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break
    # Optionally remove prefixes
    for prefix in prefixes:
        if word.startswith(prefix):
            word = word[len(prefix):]
            break
    return word

# Example usage
sample_text = "ka socota magaalada Laascaanood ayaa si weyn looga xusay xuska 18 May"
print(preprocess_text(sample_text))
