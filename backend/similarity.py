from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import iknowpy

import nltk

nltk.download('all')

# initialize the engine
iknow = iknowpy.iKnowEngine()

def getSymptomList(userSentenceMain):
    import ssl

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    from sentence_transformers import SentenceTransformer, util
    #from scrape import diseases
    from test_similarity import Complete_list1


    model = SentenceTransformer('all-MiniLM-L6-v2')

    #userSentence = nltk.sent_tokenize(userSentenceMain)
    stemmer = PorterStemmer()

    # Stemming
    #for i in range(len(userSentence)):
        #words = nltk.word_tokenize(userSentence[i])
    iknow.index(userSentenceMain, "en")
    paragraph=[]
    for s in iknow.m_index['sentences']:
        for e in s['entities']:
            if(e['type']=='Concept' or e['type']=='Relation'):
                paragraph.append(e['index'])
    words = [stemmer.stem(word) for word in paragraph]
    # words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
        
    userSentence = ' '.join(words)  

    print(userSentence)


    # Two lists of sentences
    #sentences1 = ["I feel really tired and my whole body hurts. My throat is scratchy and my nose is stuffy. I can't stop coughing and sometimes I feel really hot and then really cold. I don't really feel like eating much either."]
    sentences1=[userSentence]
    #sentences1=['I feel symptoms every day, especially after I work out,']

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
    #for a,b in scores:
    #   print(a,":", b)
    #   count+=1
    #   if(count==15):
    #       break
    priority_list=scores[0:int(0.05 * len(scores))]
    prior=[priority_list[a][0] for a in range(len(priority_list))]
    elements_to_send=prior
    with open("elements.txt", "w") as output:
        output.write(str(elements_to_send))

    return elements_to_send
