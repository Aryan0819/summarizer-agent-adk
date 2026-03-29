# 🤖 Gemini Summarizer Agent (ADK)

[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Gemini%201.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

## 📌 Overview
This repository contains a production-ready AI Agent built using the **Google Agent Development Kit (ADK)** and **Gemini 1.5 Flash**. The agent is specifically designed to perform **Text Summarization** tasks and is deployed as a serverless container on **Google Cloud Run**.

### Key Features
* **AI Engine:** Powered by Gemini 1.5 Flash via Vertex AI.
* **Architecture:** Containerized Flask application optimized for high-concurrency.
* **Deployment:** Serverless hosting on Google Cloud Run for auto-scaling.
* **ADK Compliant:** Built using the structured patterns of the Google ADK.

---

## 🏗️ Technical Stack
* **Language:** Python 3.11+
* **Framework:** Flask / Google-ADK
* **Model:** Gemini 1.5 Flash
* **Cloud Services:** Cloud Run, Artifact Registry, Vertex AI
* **CI/CD:** Google Cloud Build



---

## 🚀 Getting Started

### Prerequisites
1. A Google Cloud Project with **Billing Enabled**.
2. **Vertex AI API** enabled in the console.
3. Google Cloud SDK installed (if deploying locally).

#### 1. Local Installation
To test the agent on your local machine before deploying:

```bash
# Clone the repo
git clone [https://github.com/Aryan0819/summarizer-agent-adk.git](https://github.com/Aryan0819/summarizer-agent-adk.git)
cd summarizer-agent-adk

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```
### 🛠️ API Usage
The agent exposes a single `POST` endpoint that accepts JSON data.

**Endpoint:** `/`  
**Method:** `POST`  

**Request Body:**
```json
{
  "text": "The Agent Development Kit (ADK) is a framework designed to help developers build and deploy production-ready AI agents quickly on Google Cloud. It provides a structured way to define capabilities and models."
}
{
  "summary": "The ADK is a Google Cloud framework for building production-ready AI agents. It simplifies the process of defining agent capabilities and deploying them efficiently."
}
```
---

### ✅ Final Checklist for Submission

Before submitting your project to the track evaluators, ensure you have completed these steps:

1. **GitHub Repository:** Confirm all local changes, including this README, have been pushed:
   ```bash
   git add .
   git commit -m "Finalizing documentation and deployment steps"
   git push origin main
   ```
2. **Cloud Run Service URL:** After running the gcloud run deploy command, copy the generated Service URL. It should look like: https://summarizer-agent-xxxxxxxxxx.a.run.app
3. **Live Testing:** Verify your deployment is active and the Gemini API is responding by running this command in your terminal (replace <YOUR_SERVICE_URL> with your actual Cloud Run link):
   ```bash
   curl -X POST <YOUR_SERVICE_URL> \
     -H "Content-Type: application/json" \
     -d '{"text": "The $300 Google Cloud credit allows students to explore enterprise-grade AI tools. It is a vital resource for learning production-level deployment."}'
    ```
