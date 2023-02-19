import openai
api_key = ""
openai.api_key = api_key
import json
#import nltk
#nltk.download('punkt')

def checkSentiment(currentIdeaState, message):
  prompt = '''
  def categorizeResponse(user):
    if userHasSymptom() = Positive:
      return('Positive')
    elif not userHasSymptom() = Negative:
      return('Negative')
    elif userIsUncertain() = Neutral:
      return('Neutral')

    Examples::
    Q: Yes, I feel pain
    A: Positive
    Q: I don't feel pain.
    A: Negative
    Q: My day has been 👍
    A: Positive
    Q: I am not sure
    A: Neutral
  

    Q: This new music video blew my mind
    A: 

  #Inputs
  current_state = {state}
  User_message = {message}

  #Output
  new_state = 
  '''.format(message=message, state=json.dumps(currentIdeaState))

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.5,
  max_tokens=100,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
  responseText = response.choices[0].text
  #print("The new idea state:", responseText)
  
  '''sentences = nltk.sent_tokenize(responseText)
  outputList = []
  for a in sentences:
    a = a.replace("\"Clarifying question\"", "").replace(":","").replace("\"", "")
    if "?" in a:
      outputList.append(a)'''

  return json.loads(responseText)


sentimentState = {
  'Sentiment' : ''
}
userInput = input('Sentence to evaluate sentiment: ')
sentimentResult = checkSentiment(sentimentState, userInput)

print(sentimentResult)