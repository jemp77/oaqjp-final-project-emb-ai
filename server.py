from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Create new list without dominant_emotion
    emotions = [
        f"'{key}': {value}"
        for key, value in response.items()
        if key != 'dominant_emotion'
    ]
    # Get dominant emotion
    dominant_emotion = response["dominant_emotion"]
    # format it as string
    emotions_str = ', '.join(emotions[:-1]) + ' and ' + emotions[-1]
    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is "
        f"{emotions_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)