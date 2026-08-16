\# Healthcare Claim EOB Intelligence



A student project that uses Streamlit, Python, Pydantic, and the OpenAI API to analyze healthcare claim information and generate a structured claim assessment.



\## Features



\- Enter healthcare claim information through a Streamlit interface

\- Identify claim status and denial reason

\- Extract financial information

\- Generate a recommended next action

\- Return structured results using Pydantic



\## Tech Stack



\- Python

\- Streamlit

\- OpenAI API

\- Pydantic

\- python-dotenv

\- Pandas



\## Project Structure



```text

healthcare\_claim\_eob\_intelligence\_fresh/

│

├── app.py

├── README.md

├── requirements.txt

├── .env.example

├── .gitignore

│

├── data/

│

├── src/

│   ├── \_\_init\_\_.py

│   ├── analyzer.py

│   ├── models.py

│   └── prompts.py

│

└── tests/

&#x20;   └── test\_models.py

