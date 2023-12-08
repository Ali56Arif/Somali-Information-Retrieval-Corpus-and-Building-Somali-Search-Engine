#This file contians, the PRF python scripts for Somali IR retrieval system.
import math
import operator


queriesdict = {}
inverted_index = {}
doc_length = {}
file_content = []
file_content2 = []
def get_avdl_doclen(docPath):
    totalcount = 0
    f = open(docPath, 'r+', encoding='utf-8')
    content = f.read()
    contents = content.split("\n")
    global N
    N=len(contents)
    for c in contents:
        d = c.split("-->")
        doc_length[d[0]] = int(d[1])
        totalcount += float(d[1])
    global avdl
    avdl=totalcount/N
def get_queries(filename):
    f = open(filename, 'r+', encoding='utf-8')
    content = f.read()
    qcontent = content.split("\n")
    for q in qcontent:
        qstring = q.split(" ")
        query = " ".join(qstring[1:])
        queriesdict[qstring[0]] = query
def get_index(indexPath):
    f = open(indexPath, 'r+', encoding='utf-8')
    content = f.read()
    contents = content.split("\n")
    for c in contents:
        index = c.split("-->")
        docs = index[1].split(",")
        inlist = {}
        i = 0
        while i <= len(docs) - 1:
            inlist[docs[i][1:]] = docs[i + 1][:-1]
            i = i + 2
        inverted_index[index[0]] = inlist
def get_stop_words(common_words_path):
    global stop_words
    f = open(common_words_path, 'r+', encoding='utf-8')
    content = f.read().lower()
    stop_words = content.split()

def do_pseudo_relevance(qid,docs):
    dict_relTerms_feq = {}
    score = 0
    for key_doc,value_doc in docs[:3]:
        for key,value in inverted_index.items():
            if key not in stop_words and (not key.replace('.','',1).isdigit()):
                if key_doc in inverted_index[key]:
                    score = inverted_index[key][key_doc]
                    if key in dict_relTerms_feq:
                        dict_relTerms_feq[key] = int(score) + int(dict_relTerms_feq[key])
                    else:
                        dict_relTerms_feq[key] = int(score)
    temp_dict = (sorted (dict_relTerms_feq.items(), key = operator.itemgetter(1), reverse = True))
    print("Current Runing Query is:  " + qid)

    for k,v in temp_dict[:5]:
        queriesdict[qid] = queriesdict[qid] + " "+ k
def form_the_file(qid,docs):
    i=1
    s=""
    s2=""
    for key,value in docs[:20]:
       # s+="Q-"+""+qid+" "+str(key)+" "+str(i)+" "+str(value)+" "+" | PRF Score"+"\n"
        s +=  qid + " " + str(key) + " " + str(i) + " " + str(value) + " " + " | PRF Score" + "\n"
        #s2+="Q-"+""+qid+" "+str(key)+"\n"
        s2 +=  qid + " " + str(key) + "\n"

        i=i+1
    file_content.append(s)
    file_content2.append(s2)
def write_to_file(results):
    f = open(results, "w+", encoding="utf-8", errors="ignore")
    rstring = "".join(file_content)
    f.write(rstring.strip())
    f2 = open('PRF-Evaluation', "w+", encoding="utf-8", errors="ignore")
    rstring2 = "".join(file_content2)
    f2.write(rstring2.strip())
    f.close()
def populate_query_qfi(k):
    stop_words_file = "stopwords.txt"  #somali Stop words
    with open(stop_words_file, "r") as f:
        stop_words = f.read().splitlines()
    query_temp = {}
    query_terms = k.split()
    for terms in query_terms:
        if not terms in query_temp:
         if query_temp not in stop_words:
            query_temp[terms] = query_terms.count(terms)
    return query_temp
def searching(pseudo_Relevance_Done,results):
    for k, v in queriesdict.items():
        scoredict = {}
        qtermdict = populate_query_qfi(v)
        for q, qfi in qtermdict.items():
            if q in inverted_index:
                doc = []
                for docID in inverted_index[q]:
                    fi = inverted_index[q][docID]
                    score=0.0
                    score=BM25(docID, len(inverted_index[q]), fi, qfi)
                    try:
                        scoredict[docID] = scoredict[docID] + score
                    except KeyError:
                        scoredict[docID] = score
        sort_dict = sorted(scoredict.items(), key=operator.itemgetter(1),reverse=True)
        if pseudo_Relevance_Done:
            print("Query "+k+ " run succesfully")

            form_the_file(k, sort_dict)
        else:
            do_pseudo_relevance(k,sort_dict)
    write_to_file(results)
def get_kval(dID, k1, b):
    dl = doc_length[dID]
    k = k1 * ((1 - b) + (b * (float(dl) / avdl)))
    return k
#the BM25 matching and scoring algorithm implementation
def BM25(dID, ni, fi, qfi):
    ri = 0
    R = 0
    k1 = 1.2
    k2 = 300
    b = 0.75
    kval = get_kval(dID, k1, b)
    p1 = (((float(ri) + 0.5) / (float(R) - float(ri) + 0.5)) / ((float(ni) - float(ri) + 0.5) / (float(N) - float(ni)
          - float(R) + float(ri) + 0.5)))
    p2 = (((float(k1) + 1) * float(fi)) / (float(kval) + float(fi)))
    p3 = (((float(k2) + 1) * float(qfi)) / (float(k2) + float(qfi)))
    p4 = math.log(p1, 2)
    score = p4 * p2 * p3
    return score

#main function
def _main():
    queryPath = "queries.txt"
    indexPath = "Som_Index.txt"
    docPath = "Som_tokens.txt"
    common_words_path = "stopwords.txt"
    results="PRF.txt"
    Pseudo_Relevance_Done = False
    get_avdl_doclen(docPath)
    get_queries(queryPath)
    get_index(indexPath)
    get_stop_words(common_words_path)
    searching(Pseudo_Relevance_Done,results)
    Pseudo_Relevance_Done = True
    searching(Pseudo_Relevance_Done,results)
_main()