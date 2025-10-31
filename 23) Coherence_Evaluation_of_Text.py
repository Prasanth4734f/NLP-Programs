from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "The cat sat on the mat.",
    "Dogs bark loudly.",
    "Cats and dogs are great pets.",
    "I love my cat."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)

coherence_scores = []
for i in range(len(sentences)-1):
    score = cosine_similarity(X[i], X[i+1])[0][0]
    coherence_scores.append(score)

print("Pairwise sentence coherence scores:", coherence_scores)
print("Average coherence:", sum(coherence_scores)/len(coherence_scores))

-------------------------------OUTPUT----------------------------------

Pairwise sentence coherence scores: [0.0, 0.16191742597393538, 0.0]
Average coherence: 0.05397247532464513
