import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    
    formatted_response = response.json()
    emotion_predictions = formatted_response["emotionPredictions"]
    top_prediction = emotion_predictions[0]
    emotions = top_prediction["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    return {'emotions': emotions, 'dominant_emotion': dominant_emotion}



#in terminal:
    #git clone
#in integrated terminal
    #export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "
    #python3.11
    #from EmotionDetection.emotion_detection import emotion_detector (creates pychache)
    #import requests
    #import json
    #pip install flask
    #result = emotion_detector("I love this new technology")
    #print(json.dumps(result, indent=4)) 
    #exit()
    #export FLASK_APP=server.py
    #run flask
#make sure package has a pychache
#make surethere are node-moduals: flask and package-io
#also theres a venv folder. not sure if its important
