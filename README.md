# 🏥 Healthcare Claim & EOB Intelligence Automation

> **LLM-assisted healthcare claim and EOB analysis using Python, Pandas, NLP, Prompt Engineering, and Generative AI.**

## 📌 Project Overview

This project demonstrates an AI-assisted workflow for analyzing healthcare claim and EOB information and generating structured business-oriented summaries.

Python and Pandas are used for preprocessing, while an LLM-oriented workflow is designed to extract important information such as claim status, denial reason, payer details, and payment-related information.

## 🎯 Objectives

- Automate basic healthcare claim and EOB analysis
- Extract important claim-related information
- Standardize denial and payment outputs
- Apply prompt engineering for consistent LLM responses
- Provide an easy-to-understand Streamlit interface

## 🔄 Project Workflow

```text
Claim / EOB Data
       ↓
Data Upload
       ↓
Data Preprocessing
       ↓
Structured Prompt
       ↓
LLM Analysis
       ↓
Validation
       ↓
Structured Business Summary
       ↓
Streamlit Dashboard
```

## ✨ Key Features

- 📄 Claim/EOB CSV processing
- 🧹 Pandas-based preprocessing
- 🔍 Claim status analysis
- ❌ Denial reason analysis
- 🏥 Payer information analysis
- 💰 Payment information analysis
- 🤖 LLM-assisted summarization
- ✍️ Prompt engineering
- 📊 Streamlit dashboard

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas | Data preprocessing |
| NLP | Text processing |
| OpenAI API | LLM integration |
| Prompt Engineering | Structured AI outputs |
| Streamlit | Interactive dashboard |
| Pytest | Testing |

## 📂 Project Structure

```text
healthcare-claim-eob-intelligence/
│
├── app/
│   └── app.py
├── data/
│   └── sample_claim_eob.csv
├── screenshots/
│   ├── dashboard.png
│   ├── claim-analysis.png
│   └── denial-analysis.png
├── tests/
│   └── test_project.py
├── .env.example
├── .gitignore
├── README.md
├── app.py
└── requirements.txt
```

## 📸 Application Screenshots

Add screenshots from the actual running application:

```text
screenshots/dashboard.png
screenshots/claim-analysis.png
screenshots/denial-analysis.png
```

Then reference them in GitHub with:

```markdown
![Dashboard](screenshots/dashboard.png)
![Claim Analysis](screenshots/claim-analysis.png)
![Denial Analysis](screenshots/denial-analysis.png)
```

## 🚀 How to Run

```bash
git clone https://github.com/YOUR_USERNAME/healthcare-claim-eob-intelligence.git
cd healthcare-claim-eob-intelligence

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
streamlit run app/app.py
```

## 🔐 Environment Variables

Create a local `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

Never commit `.env` or API keys to GitHub.

## 🧪 Testing

```bash
pytest
```

## 🔒 Data Privacy

This portfolio project should use synthetic or properly de-identified healthcare data.

**Never upload real patient information, PHI, or confidential business data.**

## 📈 Future Enhancements

- EOB PDF extraction
- OCR-based processing
- Advanced denial classification
- Confidence scoring
- Batch claim processing
- LLM-generated operational recommendations
- Database integration

## 👨‍💻 Author

**Guna Sekhar**  
AI/ML & Generative AI Developer

---

⭐ Star the repository if you find this project useful.
