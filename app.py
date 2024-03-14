from flask import Flask, render_template, request, jsonify
import webbrowser
import json
import requests
from llamaapi import LlamaAPI

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

# Initialize LlamaAPI
llama = LlamaAPI('LL-XkQh3GO3VGa6oq1sOtxYkLaeQfnxQvLbq6oV04jS6STjFpNh58dk5HBA0brrEY1H')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/bot_response', methods=['POST'])
def bot_response():
    try:
        user_input = request.json.get('user_input', '')
        api_request_json = {
            "model": "llama-7b-chat",
            "messages": [
                {"role": "system", "content": "Career Counsellor and educationalist"},
                {"role": "user", "content": user_input},
            ]
        }

        # Replace this with your actual method for making the API request
        llama_response = llama.run(api_request_json)

        if llama_response:
            # Extract assistant content from the Llama API response
            #assistant_content = llama_response.get("choices", [])[0].get("message", {}).get("content", "")
            return (json.dumps(llama_response.json(), indent=2))
        else:
            return jsonify({"error": "Failed to get API response."})
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug = True)
