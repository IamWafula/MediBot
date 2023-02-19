from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_caching import Cache

from similarity import getSymptomList
from closenf import updateIdea

from sentimentAnalysis import checkSentiment



config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
api = Flask(__name__)
# tell Flask to use the above defined config
api.config.from_mapping(config)
cache = Cache(api)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'


cache.set('initial', False)



@api.route('/')
@cross_origin()
def home():
    return "home page"


"""initialInput = True

listQuestions = []
listAllSymptoms = []
currQuestion = 1"""

cache.set('responses', {})

@api.route('/response', methods=['GET','POST'])
def response():
    print(cache.get('initial'))

    if not cache.get('initial'):
        userInput = request.args.get('userInput')
        listSymptoms = getSymptomList(userInput)

        listAllSymptoms = listSymptoms

        listQuestions = updateIdea(listSymptoms)

        cache.set('listQuestions', listQuestions)
        cache.set('listAllSymptoms', listAllSymptoms)

        # print(listAllSymptoms, listQuestions)
        
        cache.set('currentQuestion', 1)

        cache.set('initial', True)

        return jsonify({'response': listQuestions[0]})
    else:
        userInput = request.args.get('userInput')
        sentiment = checkSentiment(userInput)['Sentiment']

        allResponses = cache.get('responses')
        allResponses[cache.get('listQuestions')[cache.get('currentQuestion')-1]] = [userInput,sentiment]
        cache.set('responses', allResponses)


        if cache.get('currentQuestion') < len(cache.get('listQuestions')):
            cache.set('currentQuestion', cache.get('currentQuestion')+1)
            return jsonify({'response': cache.get('listQuestions')[cache.get('currentQuestion')-1]})

        else:
            ## produce summary later (if we have time)
            print(cache.get('responses'))

            print(cache.get('listAllSymptoms'))
            
            return jsonify({'response': 'Thank you for your input. We will contact you soon.'})
        

    # if request.method == 'POST':
        

        #if request.args.get('userInput') == 'Hello':

    # return "response page"


if __name__ == '__main__':
    api.run(debug=True)