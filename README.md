# 🤖 Multi-Agent AI System

A modular **Multi-Agent AI framework** built with **LangChain**, **OpenAI**, **Streamlit**, and **Flask**.  
This project demonstrates how multiple specialized AI agents can collaborate to perform complex tasks like research, communication, validation, and reporting.

---

## 🚀 Features
- 🕵️ **Research Agent** – Collects and analyzes information  
- 💬 **Communication Agent** – Handles structured interactions  
- 📊 **Reporting Agent** – Generates human-readable reports  
- ✅ **Qualify Agent** – Validates and filters results  
- 🌐 **Streamlit UI** for user-friendly interaction  
- ⚡ **Flask Backend** for API support (optional)

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **LangChain**
- **LangChain-OpenAI**
- **OpenAI API**
- **Streamlit** (frontend UI)
- **Flask** (backend API)
- **Pandas / Numpy** (data handling)

## 📂 Project Structure

multy_agent/
├── agents/ # Multi-agent logic
│ ├── communication_agent.py
│ ├── qualify_agent.py
│ ├── reporting_agent.py
│ └── research_agent.py
├── frontend/
│ ├── flask_app/ # Flask backend
│ │ ├── app.py
│ │ └── templates/
│ └── main_agent_ui.py # Streamlit frontend
├── data/ # Example datasets
│ └── leads.csv
├── main.py # Entry point (can orchestrate agents)
├── requirements.txt
├── .env.example # Example environment variables



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Joyal2/multy_agent.git
cd multy_agent


python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows


pip install -r requirements.txt

OPENAI_API_KEY=your_openai_api_key_here
BACKEND_URL=http://localhost:10000

cd frontend/flask_app
python app.py


## 📂 Project Structure
