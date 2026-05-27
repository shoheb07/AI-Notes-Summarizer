from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face Summarizer
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

@app.route('/', methods=['GET', 'POST'])
def index():

    summary = ""

    text = ""

    if request.method == 'POST':

        text = request.form['text']

        if len(text) > 50:

            result = summarizer(
                text,
                max_length=120,
                min_length=30,
                do_sample=False
            )

            summary =
                result[0]['summary_text']

        else:

            summary =
                "Please enter longer text."

    return render_template(
        'index.html',
        summary=summary,
        text=text
    )

if __name__ == '__main__':
    app.run(debug=True)
