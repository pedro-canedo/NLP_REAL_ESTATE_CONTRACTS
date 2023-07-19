import spacy

class NERService:
    def __init__(self, model_path):
        self.nlp = spacy.load(model_path)

    def identify_fields(self, text):
        doc = self.nlp(text)
        fields = {}
        for ent in doc.ents:
            fields[ent.label_] = ent.text
        return fields
