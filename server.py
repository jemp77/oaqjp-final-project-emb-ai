"""Flask server for the emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the text provided in the request and return its detected emotions.

    Retrieves the text from the 'textToAnalyze' query parameter, passes it
    to the emotion_detector function, and formats the emotion scores and
    dominant emotion into a readable string.

    Returns:
        str: A formatted message containing the emotion scores and the
        dominant emotion, or an error message if the input text is invalid.
    """
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
    # Return invalid in case dominant_emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is "
        f"{emotions_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the application's main page.

    Returns:
        flask.Response: The rendered HTML page from the 'index.html' template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
