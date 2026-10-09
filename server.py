
"""Flask web server for Watson NLP emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Display the emotion detection web page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze text and return the emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Please enter some text to analyze.", 400

    try:
        result = emotion_detector(text_to_analyze)

        if not result or result.get("dominant_emotion") is None:
            return "Emotion detection failed. Please try again.", 502


        emotions = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is "
            f"{result['dominant_emotion']}."
        )
        return emotions, 200

    except (KeyError, TypeError, ValueError):
        app.logger.exception("Invalid emotion detection response")
        return "Unable to process the emotion detection response.", 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
