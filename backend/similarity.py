from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

# Two lists of sentences
sentences1 = 'The cat sits outside'

sentences2 = ['the cat plays in the garden',
              'A woman watches TV',
              'The new movie is so great']

#Compute embedding for both lists
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

#Compute cosine-similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)
print(cosine_scores)

#Output the pairs with their score
for i in range(len(sentences2)):
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1, sentences2[i], cosine_scores[0][i]))

