# 🔬 AI Research Assistant (Multi-Agent System)

## 📌 Overview
This project is a **multi-agent AI research assistant** built using **CrewAI** and **Streamlit**. It automates the entire research workflow—from data collection to analysis and final report generation.

The system uses multiple specialized agents that collaborate to generate structured and insightful research outputs with minimal user input.

---

## ⚙️ Features
- 🔍 Automated research on any topic  
- 🤖 Multi-agent system (Researcher, Analyst, Writer)  
- 📊 Generates:
  - Research Findings  
  - Analysis Report  
  - Final Report  
- ⚡ Powered by Groq LLMs  
- 🌐 Real-time data via Serper API  
- 🖥️ Simple Streamlit UI  

---

## 🧠 System Architecture
- **Research Specialist** → Collects data  
- **Data Analyst** → Analyzes information  
- **Content Writer** → Generates reports  

All agents work together using CrewAI orchestration.

---

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/AI-Research-Assistant-Multi-Agent.git
cd AI-Research-Assistant-Multi-Agent

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables
Create a .env file:
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key

▶️ Run the App
streamlit run app.py

🖥️ Usage
1.Enter a research topic
2.Click Start Research
3.Wait for processing
4.View/download generated reports

📂 Project Structure
├── app.py
├── crew.py
├── agents/
├── tasks/
├── research_findings.md
├── analysis_report.md
├── final_report.md
├── requirements.txt
└── .env

🛠️ Tech Stack
1.Python
2.CrewAI
3.Streamlit
4.Groq API
5.Serper API

📈 Future Improvements
1.Add agent memory
2.Improve UI
3.Export to PDF
4.Add more agents


