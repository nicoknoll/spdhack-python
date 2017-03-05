import spacy
import json
from flask import Flask, request

app = Flask(__name__)
nlp = spacy.load('de')

@app.route("/")
def analyze():
    words = []

    doc = nlp(request.args.get('tweet'))

    for t in doc:
        words.append({
            'word': t.orth_,
            'type': t.pos_
        })

    return json.dumps(words)

if __name__ == "__main__":
    app.run()
