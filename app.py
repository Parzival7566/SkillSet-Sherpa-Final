from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'marksheet' not in request.files:
        return 'No file part'
    file = request.files['marksheet']
    if file.filename == '':
        return 'No selected file'
    if file:
        return 'File uploaded successfully'

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run()