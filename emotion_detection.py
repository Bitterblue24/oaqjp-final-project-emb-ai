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
    output = emotions.copy()
    output['dominant_emotion'] = dominant_emotion
    return output



#in terminal:
    #git clone
#in integrated terminal
    #export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "
    #python3.11 -m pip install requests
    #from emotion_detection import emotion_detector
    #emotion_detector("I love this new technology")
    #print(json.dumps(result, indent=4)) 
