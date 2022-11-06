from cohere.classify import Example
import cohere

co = cohere.Client("2H7QHvLLgO1HK4kzz6w7EBLpoEHVJnYOTH0UbGF5")
dataset = [Example(x.split("\t")[1], x.split("\t")[0]) for x in open("preds.txt", "r").read().split("\n")]

def classify(text):
  classifications = co.classify(model="medium", inputs=[text], examples=dataset).classifications
  for x in classifications:
    if x.prediction != "positive":
      return "Our NLP processor recognized this as a negative description. It said your description was " + str(round(x.confidence[0].confidence*100, 2)) + "% negative. Please rephrase your description."
  return ""
