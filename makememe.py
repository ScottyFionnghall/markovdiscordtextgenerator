import markovify
import re
import spacy

nlp = spacy.load("en_core_web_sm")

# Use space ... don't how it works and if it works at all
class POSifiedText(markovify.NewlineText):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
# Open files
with open("corpus.json") as f:
    text = f.read()
    f.close()
with open("corpus2.json") as f:
    text2 = f.read()
    f.close()

# Build the model.
text_model1 = markovify.NewlineText.from_json(text)
text_model2 = markovify.NewlineText.from_json(text2)
model_cobmo = markovify.combine([ text_model1,text_model2 ], [ 2,1 ])
# Print 120 randomly-generated sentences
for i in range(120):
    with open("output2.txt",'a',encoding='utf-8') as f:
        f.write(str(model_cobmo.make_sentence())+'\n')
        f.close
