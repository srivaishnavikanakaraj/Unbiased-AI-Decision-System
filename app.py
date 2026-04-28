from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    df = pd.read_csv(file)

    result = "No Bias Detected"

    if 'gender' in df.columns:
        male = len(df[df['gender'] == 'Male'])
        female = len(df[df['gender'] == 'Female'])

        if abs(male - female) > 5:
            result = "Bias Detected in Gender Distribution"

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
