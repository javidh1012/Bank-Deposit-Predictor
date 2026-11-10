# 🏦 Bank Deposit Predictor

An end-to-end Machine Learning web application designed to predict whether a banking client will subscribe to a term deposit based on demographic, financial, and marketing campaign attributes.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bankdeposit-predictor.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4.2-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🔗 Live Demo

Experience the live application here:  
👉 **[https://bankdeposit-predictor.streamlit.app/](https://bankdeposit-predictor.streamlit.app/)**

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Live Demo](#-live-demo)
- [Input Features](#-input-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Local Installation & Setup](#-local-installation--setup)
- [Usage Guide](#-usage-guide)
- [Model Details](#-model-details)
- [License](#-license)

---

## 📖 Overview

Direct marketing campaigns are crucial for financial institutions to attract long-term deposits. However, contacting every prospective customer requires significant resources and operational cost.

The **Bank Deposit Predictor** leverages a trained Machine Learning model to evaluate client profiles and past campaign interactions in real time, estimating the likelihood of a term deposit subscription. This empowers marketing and sales teams to:
- Prioritize high-conversion prospects.
- Optimize telemarketing resource allocation.
- Tailor outreach strategies based on client financial profiles.

---

## ✨ Key Features

- **Intuitive Web UI**: Clean, responsive 3-column form built with Streamlit.
- **Instant Predictions**: Real-time classification indicating whether the client is likely to subscribe (`Yes` / `No`).
- **Probability Scoring**: Displays the predicted confidence/subscription probability when available.
- **Comprehensive Profiling**: Captures personal demographics, account financials, and marketing campaign history.
- **Robust Model Handling**: Cached resource loading with error handling and dependency checks.

---

## 📊 Input Features

The model evaluates **16 client attributes** categorized into three main sections:

### 1. Client Demographics & Personal Info
| Feature | Type | Description / Sample Values |
| :--- | :--- | :--- |
| `age` | Numeric | Age of the client (18–100) |
| `job` | Categorical | Occupation (`admin.`, `blue-collar`, `technician`, `management`, `services`, etc.) |
| `marital` | Categorical | Marital status (`married`, `single`, `divorced`, `unknown`) |
| `education` | Categorical | Education level (`primary`, `secondary`, `tertiary`, `university.degree`, etc.) |

### 2. Financial Status & Contact Channels
| Feature | Type | Description / Sample Values |
| :--- | :--- | :--- |
| `default` | Categorical | Has credit in default? (`no`, `yes`, `unknown`) |
| `balance` | Numeric | Average yearly balance (in currency units) |
| `housing` | Categorical | Has a housing loan? (`yes`, `no`, `unknown`) |
| `loan` | Categorical | Has a personal loan? (`no`, `yes`, `unknown`) |
| `contact` | Categorical | Communication type (`cellular`, `telephone`, `unknown`) |

### 3. Campaign & Historical Interaction Data
| Feature | Type | Description / Sample Values |
| :--- | :--- | :--- |
| `day` | Numeric | Last contact day of the month (1–31) |
| `month` | Categorical | Last contact month (`jan`, `feb`, `mar`, ..., `dec`) |
| `duration` | Numeric | Last contact duration in seconds |
| `campaign` | Numeric | Number of contacts performed during this campaign |
| `pdays` | Numeric | Days passed since last contact from a previous campaign (`-1` = not previously contacted) |
| `previous` | Numeric | Number of contacts performed before this campaign |
| `poutcome` | Categorical | Outcome of previous campaign (`unknown`, `failure`, `other`, `success`) |

---

## 🛠️ Tech Stack

- **Frontend & App Framework**: [Streamlit](https://streamlit.io/)
- **Machine Learning & Pipeline**: [Scikit-Learn](https://scikit-learn.org/) / [PyCaret](https://pycaret.org/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Model Persistence**: [Joblib](https://joblib.readthedocs.io/)
- **Deployment Platform**: Streamlit Community Cloud

---

## 📁 Project Structure

```plaintext
Bank_Deposit_predictor/
│
├── bank_dt_joblib.joblib     # Pre-trained decision tree classification model / pipeline
├── main.py                   # Streamlit web application & prediction interface
├── requirements.txt          # Python dependencies required to run the application
├── logs.log                  # Execution and runtime logs
└── README.md                 # Project documentation & setup instructions
```

---

## 💻 Local Installation & Setup

To run this application locally on your machine, follow these steps:

### 1. Prerequisites
Ensure you have **Python 3.9 - 3.11** installed on your system.

### 2. Clone or Navigate to the Repository
```bash
git clone https://github.com/<your-username>/Bank_Deposit_predictor.git
cd Bank_Deposit_predictor
```

### 3. Create and Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note:** If unpickling the model requires PyCaret or specific estimator dependencies, ensure `pycaret` is installed in your environment:
> ```bash
> pip install pycaret
> ```

### 5. Launch the Streamlit App
```bash
streamlit run main.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## 🚀 Usage Guide

1. Open the [Live Demo](https://bankdeposit-predictor.streamlit.app/) or run locally.
2. In the **Client Profile** section, fill in the customer's age, occupation, marital status, and education.
3. In the middle column, enter credit default status, average balance, loan information, and contact method.
4. In the right-hand column, supply campaign details including call duration, day/month, and previous campaign outcome.
5. Click **"Predict subscription"**.
6. View the **Estimated Outcome** (`Yes` or `No`) alongside the subscription probability score.

---

## 🧠 Model Details

- **Model Type**: Decision Tree Classifier / Pipeline
- **Target Variable**: Term Deposit Subscription (`yes` / `no`)
- **Serialized Model**: `bank_dt_joblib.joblib`
- **Inference Pipeline**: Raw input features are structured into a tabular DataFrame matching the training schema, fed into the pipeline for preprocessing, feature transformation, and final classification.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use and adapt it for learning or development purposes.

