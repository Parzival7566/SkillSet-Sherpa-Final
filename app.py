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


# API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
# headers = {
#     "Authorization": f"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",
#     "Content-Type": "application/json",
# }

# def query(payload):
#     json_body = {
#         "inputs": f"[INST] <<SYS>> Your job is to talk like a pirate. Every response must sound like a pirate. <<SYS>> {payload} [/INST]",
#         "parameters": {"max_new_tokens": 256, "top_p": 0.9, "temperature": 0.7}
#     }
#     data = json.dumps(json_body)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     try:
#         return json.loads(response.content.decode("utf-8"))
#     except:
#         return response
    
# @app.route('/bot_response', methods=['POST'])
# def bot_response():
#     try:
#         user_input = request.json.get('user_input', '')
#         # Use the query function to get the response from Llama API
#         llama_response = query(user_input)

#         if llama_response:
#             # Extract assistant content from the Llama API response
#             # Assuming there is a key in the response that holds the generated text
#             assistant_content = llama_response[0]['generated_text'].split('[/INST] ')[1]

#             # Return the response with indented content
#             return jsonify({"response": assistant_content})
#         else:
#             return jsonify({"error": "Failed to get API response."})
#     except Exception as e:
#         return jsonify({"error": str(e)})
    
@app.route('/bot_response', methods=['POST'])
def bot_response():
    try:
        user_input = request.json.get('user_input', '')
        api_request_json = {
            "model": "llama-13b-chat",
            "messages": [
                {"role": "system", "content": "start conversation"},
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


questions = [
    ("Do you enjoy working with your hands and tools?", "Realistic (R)"),
    ("Are you naturally curious and enjoy exploring new ideas?", "Investigative (I)"),
    ("Do you have a passion for creative activities like drawing, writing, or music?", "Artistic (A)"),
    ("Do you find fulfillment in helping and working with others?", "Social (S)"),
    ("Are you ambitious and enjoy taking on leadership roles?", "Enterprising (E)"),
    ("Do you prefer working in structured and organized environments?", "Conventional (C)"),
    ("Are you interested in working outdoors or in natural settings?", "General (Mixed RIASEC)"),
    ("Do you prefer a fast-paced and dynamic work environment?", "General (Mixed RIASEC)"),
    ("Do you enjoy working with machinery and technology?", "Realistic (R)"),
    ("Do you like conducting experiments and solving complex problems?", "Investigative (I)"),
    ("Do you have a talent for artistic and creative expression?", "Artistic (A)"),
    ("Do you enjoy teaching or mentoring others?", "Social (S)"),
    ("Do you have strong negotiation and persuasion skills?", "Enterprising (E)"),
    ("Do you prefer a neat and structured workspace?", "Conventional (C)"),
    ("Do you like spending time in nature and outdoor activities?", "General (Mixed RIASEC)"),
    ("Do you thrive in high-pressure and competitive situations?", "General (Mixed RIASEC)"),
    ("Are you mechanically inclined and good at fixing things?", "Realistic (R)"),
    ("Do you enjoy analyzing data and conducting research?", "Investigative (I)"),
    ("Are you skilled in playing musical instruments or creating art?", "Artistic (A)"),
    ("Do you excel in teamwork and collaboration?", "Social (S)")
]

user_responses = {}

@app.route('/aptitude')
def aptitude():
    return render_template('aptitude.html')

@app.route('/submit_responses', methods=['POST'])
def submit_responses():
    try:
        responses = request.json  # This is already a dictionary
        num_questions = 20  # Update this number if needed
        
        # Instead of requiring all questions to be answered, handle cases where some might be missing
        if len(responses) > num_questions:
            return jsonify({"error": "Received more responses than expected."}), 400
        
        # Calculate RIASEC scores
        riasec_scores = calculate_riasec_scores(responses)
        
        # Return the calculated scores
        return jsonify(riasec_scores)
    except Exception as e:
        return jsonify({"error": str(e)})

def calculate_riasec_scores(responses):
    if len(responses) != len(questions):
        return {"error": "Number of responses does not match the number of questions."}

    # Convert responses to scores
    scores = [int(score) for score in responses.values()]
    total_score = sum(scores)
    if total_score == 0:  # Prevent division by zero
        return {"error": "Total score cannot be zero."}

    normalized_scores = {}
    for (_, category), score in zip(questions, scores):
        category_key = category.split()[0]
        normalized_scores[category_key] = normalized_scores.get(category_key, 0) + score

    # Normalize scores
    for key in normalized_scores:
        normalized_scores[key] = (normalized_scores[key] / total_score) * 100
    
    print(normalized_scores)

    return normalized_scores
    
    
if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(debug = True)


#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
