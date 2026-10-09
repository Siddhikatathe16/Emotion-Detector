import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_happy_text(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.02,
                        "fear": 0.03,
                        "joy": 0.90,
                        "sadness": 0.04
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am happy")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(result["joy"], 0.90)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sad_text(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.02,
                        "disgust": 0.01,
                        "fear": 0.05,
                        "joy": 0.10,
                        "sadness": 0.82
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am sad")

        self.assertEqual(result["dominant_emotion"], "sadness")
        self.assertEqual(result["sadness"], 0.82)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400_error(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_network_error(self, mock_post):
        import requests

        mock_post.side_effect = requests.exceptions.ConnectTimeout

        result = emotion_detector("I am happy")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main(verbosity=2)