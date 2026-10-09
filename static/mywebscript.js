
function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value.trim();
    const output = document.getElementById("system_response");

    if (!text) {
        output.textContent = "Please enter some text to analyze.";
        return;
    }

    output.textContent = "Analyzing text...";

    const request = new XMLHttpRequest();
    request.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(text),
        true
    );
    request.timeout = 15000;

    request.onload = function () {
        if (request.status === 200) {
            output.textContent = request.responseText;
        } else {
            output.textContent =
                "Error (" + request.status + "): " +
                (request.responseText || "Emotion detection failed.");
        }
    };

    request.onerror = function () {
        output.textContent =
            "Cannot connect to the application server.";
    };

    request.ontimeout = function () {
        output.textContent =
            "The request timed out. Please try again.";
    };

    request.send();
}