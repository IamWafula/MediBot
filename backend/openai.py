api_key = "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"

import openai
import json
openai.api_key = api_key ## You can store secrets by clicking on the Python kernel


def updateIdea(currentIdeaState, message):
  #lst = symptoms
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
    def askClarifyingQuestions():
        read({lst})
        for symptoms in lst:
            while symptoms.isnotPreciseEnough():
                askCreativeClarifyingQuestions()
                symptoms.morePrecise()
        if 


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
  print("The new idea state:", responseText)
  return json.loads(responseText)

startingState = {
'Three suspected diseases and their probability':'',
'Clarifying question':'',
'Identified symptoms with their precise name':''
}

userInput = input('Response: ')
newState = updateIdea(startingState, userInput)