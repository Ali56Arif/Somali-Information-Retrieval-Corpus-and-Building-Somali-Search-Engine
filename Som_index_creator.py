#This file creates the inverted index, for the Somali PRF IR retrieval.
import os
import operator
import re
Som_index = {}
Som_TF = {}
Som_DF = {}
Som_tokens = {}

Som_docs_path = "Somali-IR-Evaluation-corpus"
filenamelist = os.listdir(Som_docs_path)
#def remove_special_characters(text):
    #cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    #return cleaned_text
def create_inverted_index():
    for filename in filenamelist:
        content = []
        #Removing especial characters needs special considerations, there are few characters,
        #which we don't remove. The below are the removed ones, in Somali IR.
        special = '&^" ' '.#@$*'
        name_of_file = filename.split('.txt')
        docID = name_of_file[0]
        f = open(Som_docs_path + '\\' + filename, 'r+', encoding='latin-1')
        translator = str.maketrans(special, ' ' * len(special))
        raw_data = f.read()
        # Remove special characters
        raw_data = raw_data.translate(translator)
        content = raw_data.lower().split()
        unigram_token = []
        for c in content:
            unigram_token.append(c)
            if c in Som_index:
                if docID not in Som_index[c]:
                    Som_index[c].update({docID: 1})
                else:
                    Som_index[c][docID] += 1
            else:
                Som_index[c] = {docID: 1}
        Som_tokens[docID] = len(unigram_token)
def generate_tf_df(index_gram, gram_tf, gram_df):
    for key, value in index_gram.items():
        term_frequency = 0
        docString = ""
        i = 0
        for k, v in value.items():
            i += 1
            term_frequency += v
            docString += k
            if i < len(value):
                docString += " "
        no_of_docs = len(value)
        gram_tf[key] = term_frequency
        gram_df[key] = {docString: no_of_docs}
def generate_tf_table(gram_tf, nof):
    sort_dict = sorted(sorted(gram_tf.items()), key=operator.itemgetter(1), reverse=True)
    tfstring = ""
    f = open(nof, "w+", encoding="utf-8", errors="ignore")
    for k, v in sort_dict:
        tfstring += str(k) + "-->" + str(v) + "\n"
    f.write(tfstring.strip())
    f.close()
def generate_df_table(gram_df, nof):
    sort_dict = sorted(gram_df.items(), key=operator.itemgetter(0))
    f = open(nof, "w+", encoding="utf-8", errors="ignore")
    write_string = ""
    for k, v in sort_dict:
        df_value = ""
        for key, value in v.items():
            df_value = str(key) + " -> " + str(value)
        final_string = str(k) + "-->" + df_value + "\n"
        write_string += final_string
    f.write(write_string.strip())
    f.close()
def write_index_to_file(dict_gram, nof):
    final_term = ""
    f = open(nof, "w+", encoding="utf-8", errors="ignore")
    for k, v in dict_gram:
        value_term = ""
        i = 0
        for key, val in v.items():
            i += 1
            value_term += "(" + str(key) + "," + str(val) + ")"
            if i < len(v):
                value_term += ","

        final_term += str(k) + "-->" + value_term + "\n"
    f.write(final_term.strip())
    f.close()
def write_tokens_to_file(grams_tokens, nof):
    token_string = ""
    f = open(nof, "w+", encoding="utf-8", errors="ignore")
    for k, v in grams_tokens.items():
        token_string += str(k) + "-->" + str(v) + "\n"
    f.write(token_string.strip())
    f.close()
def _Sommainindexer():
    create_inverted_index()
    sorted_index = sorted(Som_index.items(), key=operator.itemgetter(0))
    write_index_to_file(sorted_index, "Som_Index.txt")
    write_tokens_to_file(Som_tokens, "Som_tokens.txt")
_Sommainindexer()
