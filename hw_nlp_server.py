from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse
import bl
import spacy


nlp = spacy.load("en_core_web_sm")

app = FastAPI(title="Example API", description="A simple FastAPI with Swagger UI", version="1.0")

@app.get("/ping")
def ping():
    return {"pong": "🐸"}

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


@app.get("/entities/")
def first():
    text = "Taylor Swift performed in Los Angeles on March 3rd, 2023."
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({"text": ent.text, "label": ent.label_})

    return {"entities": entities}


@app.get("/entities2/")
def second():
    text = "Serena Williams had dinner with Tom Hanks in Paris."
    doc = nlp(text)
    people = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            people.append(ent.text)
    return {"people": people}


print(">>> Loading entities3 endpoint…")
@app.get("/entities3/")
def third():
    print(">>> entities3 route registered")
    text = "She was running and had run 5 kilometers by 7am."
    doc = nlp(text)
    res = []
    for token in doc:
        res += (f"{token.text:10} ➝ {token.lemma_}")
    return {"lemma":res}


@app.get("/entities4/")
def fourth():
    text = "This is an example sentence with some stop words."
    doc = nlp(text)
    filtered_words = [token.text for token in doc if not token.is_stop]
    return {"filtered" : filtered_words}


@app.get("/entities5/")
def fifth():
    nlp.vocab["powerful"].is_stop = True
    text = "SpaCy is awesome and powerful."
    doc = nlp(text)
    stop_words = [token.text for token in doc if token.is_stop]
    return {"stop words" : stop_words}

@app.get("/entities6/")
def sixth():
    from spacy.matcher import PhraseMatcher

    matcher = PhraseMatcher(nlp.vocab)

    # Use PhraseMatcher to identify the phrase "artificial intelligence" in a sentence and print matches

    phrase = ["artificial intelligence", "Artificial Intelligence"]
    patterns = [nlp(text) for text in phrase]
    matcher.add("AI_PHRASE", patterns)

    text = "Artificial Intelligence is the future. I study artificial intelligence."
    doc = nlp(text)

    matches = matcher(doc)
    res = []
    for match_id, start, end in matches:
        res.append(doc[start:end].text)
    return {"res":res}


@app.get("/entities7/")
def seventh():
    text = "The cat sat on the mat."
    doc = nlp(text)
    res = []
    for token in doc:
        res.append(f"{token.text:10} {token.pos_:10} {spacy.explain(token.pos_)}")
    return {"res": res}


@app.get("/entities8/")
def eighth():
    from spacy.language import Language
    @Language.component("custom_separator")
    def custom_separator(doc):
        for token in doc[:-1]:
            if token.text == '^':
                doc[token.i + 1].is_sent_start = True
        return doc

    nlp.add_pipe('custom_separator', before='parser')
    print(nlp.pipe_names)

    text = "SpaCy is great ^ It helps with NLP tasks ^ Really useful."

    doc = nlp(text)
    res = []
    for sent in doc.sents:
        print(sent)
    return {"res": res}


# @app.post("/entities9/")
# def ninth():
#     from spacy import displacy
#     sentence = input("Enter a sentence: ")
#     doc = nlp(sentence)
#     res = []
#     for token in doc:
#         res.append(f"{token.text:10} {token.pos_:10} {spacy.explain(token.pos_)}")
#     return {"res": res}














