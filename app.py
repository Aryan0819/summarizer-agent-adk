import os
from flask import Flask, request, jsonify
from google.adk import agent
from google.adk import model_provider

app = Flask(__name__)

# 1. Configure the Gemini Model via ADK
gemini_model = model_provider.GeminiModel(
    model_name="gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY") # Or use ADC on Cloud Run
)

# 2. Define the Agent Capability
@agent.capability(
    name="summarize_text",
    description="Summarizes long pieces of text into a concise paragraph."
)
def summarize(text: str):
    prompt = f"Please provide a concise summary of the following text: {text}"
    response = gemini_model.generate(prompt)
    return response.text

# 3. HTTP Endpoint for Cloud Run
@app.route("/", methods=["POST"])
def run_agent():
    data = request.get_json()
    input_text = data.get("text", "")
    
    if not input_text:
        return jsonify({"error": "No text provided"}), 400
    
    # Invoke the agent capability
    result = summarize(input_text)
    return jsonify({"summary": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))