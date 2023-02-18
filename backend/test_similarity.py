import pandas as pd
import numpy as np
import re
from sentence_transformers import SentenceTransformer, util
from scrape import diseases
model = SentenceTransformer('all-MiniLM-L6-v2')
'''
# Two lists of sentences
#sentences1 = ["I feel really tired and my whole body hurts. My throat is scratchy and my nose is stuffy. I can't stop coughing and sometimes I feel really hot and then really cold. I don't really feel like eating much either."]
#sentences1=['the front of my kneecap is swollen and has throbbing pain']
#sentences1=['I feel symptoms every day, especially after I work out,']
sentences1=['Arthritis and Chronic Fatigue Syndrome']
sentences2 = diseases

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
    '''

df=pd.read_html("https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html")
df1=df[0]
Diseases= df1[df1[0].isna()==0][0]
Diseases=list(Diseases)
for a in range(len(Diseases)):
  Diseases[a]=Diseases[a].replace("^", " or ")
#pattern="UMLS:[a-zA-Z0-9]*_([a-zA-Z ]*)"
pattern=".+?([^UMLS:C\d{7}_]+)"
dis=[]
for a in Diseases:
  okay=re.findall(pattern, a)
  okay="".join(okay)
  dis.append(okay)

num_occur=list(np.where(df1[0].isna()==0)[0] )
Symptoms=list(df1[2].unique())
Symptoms=[a for a in Symptoms if str(a)!="nan"]
for a in range(len(Symptoms)):
  if(type(Symptoms[a])==float):
    Symptoms[a]=Symptoms[a].replace("^", " or ")
Complete_list=[a for a in Complete_list if str(a)!="nan"]
for a in range(len(Complete_list)):
  if(type(Complete_list[a])==float):
    Complete_list[a]=Complete_list[a].replace("^", " or ")
pattern=".+?([^UMLS:C\d{7}_]+)"
Complete_list1=[]
for a in Complete_list:
  okay=re.findall(pattern, a)
  okay="".join(okay)
  Complete_list1.append(okay)

#Complete_list1=Complete_list1[1:]
Complete_list=Complete_list1.copy()
Complete_list1=list(dict.fromkeys(Complete_list1))
New_Dataset=dict()
for a in range(len(dis)-1):
  New_Dataset[dis[a]]=Complete_list[num_occur[a]:num_occur[a+1]]
New_Dataset[dis[-1]]=Complete_list[num_occur[-1]:]

t=[]
for a in Complete_list1:
  l=[]
  for b in New_Dataset.keys():
    l.append(a in New_Dataset[b])
  t.append(l)
for a in range(len(t)):
  for b in range(len(t[a])):
    if t[a][b]==True:
      t[a][b]=1
    else:
      t[a][b]=0

diagnosis=pd.DataFrame(t)
diagnosis.index=Complete_list1
diagnosis.columns=dis
for a in diagnosis.columns:
  print(a, diagnosis[a].sum())
