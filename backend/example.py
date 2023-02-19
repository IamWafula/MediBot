"""import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

from similarity import getSymptomList

print(getSymptomList("I have pain in my left arm and my left leg"))
"""

import iknowpy

engine = iknowpy.iKnowEngine()

# show supported languages
print(engine.get_languages_set())

# index some text
text = 'This is a test of the Python interface to the iKnow engine.'
engine.index(text, 'en')

# print(getattr(engine, ))

# print the raw resultt


engine.index("My head and hand are hurting ","en")
paragraph=[]
for s in engine.m_index['sentences']:
    for e in s['entities']:
        #if(e['type']=='Concept'):
        print(e['type'], " : ", e['index'])
            #print(e['index'])
            #paragraph.append(e['index'])
#paragraph=' '.join(paragraph)
#print(paragraph)
#print(engine.m_index)
           