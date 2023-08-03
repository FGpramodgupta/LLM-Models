from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('all-MiniLM-L6-v1')
embeddings = model.encode(sentences)
print(embeddings)