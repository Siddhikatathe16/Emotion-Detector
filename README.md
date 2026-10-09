\# Watson NLP Emotion Detection



\## Project Overview



This project uses Python and Flask to provide a web interface for emotion detection. It processes text and returns emotion categories: anger, disgust, fear, joy, and sadness, along with the dominant emotion.



\## Technologies Used



\* Python

\* Flask

\* Requests

\* HTML, JavaScript, and Bootstrap

\* unittest and unittest.mock

\* Pylint



\## Project Structure



\* `server.py` — Flask application and routes

\* `EmotionDetection/emotion\_detection.py` — emotion detection function

\* `EmotionDetection/\_\_init\_\_.py` — package initialization

\* `templates/index.html` — web interface

\* `static/mywebscript.js` — browser-side request handling

\* `test\_emotion\_detection.py` — automated unit tests



\## Run the Application



From the project directory, run:



```bash

python server.py

```



Open `http://127.0.0.1:5000` in your browser.



\## Run Unit Tests



```bash

python -m unittest -v test\_emotion\_detection.py

```



\## Code Quality



Run Pylint on the Flask server:



```bash

python -m pylint server.py

```



The server achieved a Pylint score of 10.00/10 in the local check.



\## Service Availability Note



The Watson emotion prediction endpoint timed out during testing in the current network environment. Automated unit tests use mocked responses and do not represent live Watson predictions.



