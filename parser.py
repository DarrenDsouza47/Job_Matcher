import spacy
import spacy_transformers


def resume_parser(resume_text):
    nlp = spacy.load('model-best')
    doc = nlp(resume_text)

    output = {}
    for ent in doc.ents:
        if ent.label_ not in output:
            output[ent.label_] = [ent.text]
        else:
            output[ent.label_].append(ent.text)
    
    return output



