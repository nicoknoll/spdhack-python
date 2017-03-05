import spacy
import json
from flask import Flask, request
app = Flask(__name__)
nlp = spacy.load('de')

@app.route("/")
def analyze():
    types = []
    entities = []

    doc = nlp(request.args.get('tweet'))

    for t in doc:
        types.append({
            'type': t.pos_,
            'phrase': t.orth_
        })

    if doc.ents:
        for ent in doc.ents:
            entities.append({
                'type': ent.label_,
                'phrase': ent.text
            })

    return json.dumps({
        'types': types,
        'entities': entities
    })


if __name__ == "__main__":
    app.run()
