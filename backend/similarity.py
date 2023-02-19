from sentence_transformers import SentenceTransformer, util
from scrape import diseases
from test_similarity import Complete_list1
model = SentenceTransformer('all-MiniLM-L6-v2')


# Two lists of sentences
#sentences1 = ["I feel really tired and my whole body hurts. My throat is scratchy and my nose is stuffy. I can't stop coughing and sometimes I feel really hot and then really cold. I don't really feel like eating much either."]
#sentences1=['the front of my kneecap is swollen and has throbbing pain']
#sentences1=['I feel symptoms every day, especially after I work out,']
sentences1=[' break on the skin, in the lining of an organ, or on the surface of a tissue. ']
sentences2 = Complete_list1

#Compute embedding for both lists
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

#Compute cosine-similarities
cosine_scores = util.cos_sim(embeddings1, embeddings2)

#Output the pairs with their score
scores=dict()
for i in range(len(sentences2)):
    scores[sentences2[i]]=cosine_scores[0][i]
   
scores=sorted(scores.items(), reverse=True, key=lambda x:x[1])
count=0
for a,b in scores:
    print(a,":", b)
    count+=1
    if(count==15):
        break
