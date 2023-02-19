api_key = "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"

import openai
import json
import nltk
#from similarity import elements_to_send
openai.api_key = api_key ## You can store secrets by clicking on the Python kernel

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.system('python similarity.py')

with open('elements.txt') as f:
    lines = f.readlines()


def updateIdea(currentIdeaState, message):
  '''
  def findSymptoms(userInput):
      while userInput != anyPreciseMedicalTerm:
        try:
          askCreativeClarifyingQuestion()
        except:
          Question targets same specific type of pain or body part()
        userInput.morePrecise()  
      if userInput == PreciseEnough():
        askOtherAssociativeSymptoms
        print(DiseaseName with highest Probability based on symptoms)
        print(DiseaseName with second highest Probability based on symptoms)
        print(DiseaseName with third highest Probability based on symptoms)
    '''
  prompt = '''
    def askClarifyingQuestions(userInput):
        read(UserInput) as list
        if UserInput[0] != PreciseEnough():
          askQuestionsToClarify()
          UseSimpleTermsInQuestion()
          ExplainMedicalTextIfUserRequests()       
        select symptom in UserInput similar to UserInput[0]:
          askQuestionsToClarify()          
         


  # Inputs
  curren_state = {state}
  User_message = {message}

  # Output in JSON
  new_state = 
  '''.format(message=message,state=json.dumps(currentIdeaState))

  # print("Prompt:", prompt)

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=100,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  responseText = response.choices[0].text

  #print(responseText)
  sentences = nltk.sent_tokenize(responseText)
  outputList = []
  for a in sentences:
    a = a.replace("\"Clarifying question\"", "").replace(":","").replace("\"", "")
    if "?" in a:
      outputList.append(a)

  #print("The new idea state:", responseText)
  #responseText = responseText.split(":")[1]
  #finalData = responseText.split(",")
  #print(finalData[0])

  #return json.load(responseText)
  return outputList


startingState = {
'Clarifying question':'',
'Identified symptoms with their precise name':''
}

#userInput = elements_to_send

# print(userInput)
newState = updateIdea(startingState, lines)

print(newState)