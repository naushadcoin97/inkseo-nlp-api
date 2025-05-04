from flask import Flask, request, jsonify
import spacy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")

@app.route('/extract', methods=['POST'])
def extract():
    data = request.get_json()
    doc = nlp(data['content'])
    keywords = list(set([chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text) > 2]))
    return jsonify(keywords[:15])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
