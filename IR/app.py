from flask import Flask, request, render_template
from collections import defaultdict
from search import search
from index_creator import create_inverted_index
from text_operations import preprocess_text

app = Flask(__name__)

# Example documents (replace with your actual data)
documents = {
    1: "Magaalada Laascaanood ayaa dagaal ka dhacay.",
    2: "Doorashada Puntland ayaa lagu soo dhoweeyey.",
    3: "Magaalada Qabridahar waxay leedahay taariikh dheer.",
    4: "Xuska 18 May ayaa si weyn looga xusay guud ahaan Somaliland.",
    5: "Macluumaadka jaamacada Jigjiga waxaan ka helay website-ka.",
    6: "Fatahaada wabiga Shabeelle ayaa saameyn ku yeelatay dadka deegaanka.",
    7: "Xidhiidhka Shiinaha iyo Africa wuxuu soo bilowday muddo dheer.",
    8: "Ciyaaryahanka ugu fiican kubadda cagta adduunka waa Lionel Messi.",
    9: "Taariikhda heesaha fanaanka qaaday heesta 'Baladweyne Allahayow'.",
    10: "Xaalada deegaanka Tigreega ayaa weli kacsan.",
    11: "1-da Luulyo waa maalinta xorriyadda Soomaaliya.",
    12: "Gabayada abwaan Gaashaandhigga waa kuwa ugu caansan.",
    13: "Doonta Titan ee aaday burburka Titanic.",
    14: "Sidee lagu doortay tirsiga 24 saac ee maalinta.",
    15: "Suuqa Jigjiga ee gubtay ayaa dib loo dhisayaa.",
    16: "Sacuudiga iyo arimaha Xajka ayaa si weyn loo hadal hayaa."
}

# Create the inverted index
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
