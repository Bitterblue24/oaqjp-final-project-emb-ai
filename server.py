from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    response_copy = response.copy()
    dominant_emotion = response_copy.pop('dominant_emotion')
    response_string = str(response_copy)
    emotion_list = response_string[1:-1]
    string = f"For the given statement, the system response is {emotion_list}. The dominant emotion is {dominant_emotion}."
    complete_response = string
    return complete_response
    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
