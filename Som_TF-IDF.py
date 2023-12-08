#Python file for the Somali TF-IDF retrieval.
import math
import operator

queriesdict = {}
inverted_index = {}
results=[]
results2=[]
dls={}


def get_doclen(docPath):
    totalcount = 0
    f = open(docPath, 'r+',encoding='utf-8' )
    content = f.read()
    contents = content.split("\n")
    global N
    N=len(contents)
    for c in contents:
        d=c.split("-->")
        dls[d[0]]=d[1]
def get_queries(filename):
    f = open(filename, 'r+',encoding='utf-8')
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
def write_to_file(TFiDFresults):
    f = TFiDFresults
    rstring="".join(results)
    f.write(rstring.strip())
    f2 = open('TF-IDF-Evaluation', "w+", encoding="utf-8", errors="ignore")
    rstring2 = "".join(results2)
    f2.write(rstring2.strip())
    f2.close()
    f.close()
def form_the_file(qid,docs):
    i=1
    s=""
    s2=""
    for k,v in docs[:20]:
        s +=  qid + " " + str(k) + " " + str(i) + " " + str(v) + " " + " | TF_IDF_Ranking mode " + "\n"
        s2 += qid + " " + str(k) + "\n"
    results.append(s)
    results2.append(s2)
def get_stopword(Som_stop_words):
        stop_words_file = "stopwords.txt"  # somali Stop words
        with open(stop_words_file, "r") as f:
            stop_words = f.read().splitlines()
def searching(TFiDFresults):
    for k, v in queriesdict.items():
        scoredict = {}
        qterms = v.split()
        for q in qterms:
            if q in inverted_index.keys():
                doc = []
                for docID in inverted_index[q]:
                    fi = inverted_index[q][docID]
                    score=0.0
                    score=tfidf(fi,docID,len(inverted_index[q]))
                    if docID in scoredict:
                        scoredict[docID] = scoredict[docID] + score
                    else:
                        scoredict[docID] = score
        sort_dict = sorted(scoredict.items(), key=operator.itemgetter(1),reverse=True)
        form_the_file(k,sort_dict)
    write_to_file(TFiDFresults)
def tfidf(fi,dID,ni):
    dl=dls[dID]
    tf=float(fi)/float(dl)
    idf=1+ math.log(N/(ni+1))
    score = tf*idf
    return score
def _Sommain():
    queryPath = "queries.txt"
    indexPath = "Som_index.txt"
    docPath = "Som_tokens.txt"
    Som_stop_words = "stopwords.txt"
    TFiDFresults= open("TF_IDF_Results", 'w+')
    get_doclen(docPath)
    get_queries(queryPath)
    get_index(indexPath)
    searching(TFiDFresults)
    get_stopword(Som_stop_words)
_Sommain()
