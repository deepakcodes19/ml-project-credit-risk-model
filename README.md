## **💳 Easy Finance – Credit Risk Modelling**

An end-to-end **Credit Risk Prediction System** built with **Machine Learning, Python, and Streamlit**, designed to estimate the **probability of loan default**, assign a **credit score**, and classify applicants into **risk tiers** (Poor to Excellent).

This project simulates a real-world risk engine used in **banks, lending fintechs, and NBFCs**, and includes:

- 🧠 A trained ML model (Logistic Regression)  
- ⚙️ Scaler, feature engineering & preprocessing pipeline  
- 🔍 Real-time prediction using a Streamlit UI  
- 🎚️ Dynamic credit score + risk rating  
- 📊 Feature importance visualization  
- 🚀 Deployable, modular project structure  

---

## 🚀 Live Features
**✔ Real-time Credit Risk Prediction**  

**🔍 Live App: https://dy-ml-project-credit-risk-model.streamlit.app/**

Enter customer inputs such as age, income, loan amount, delinquency ratio, DPD, utilization, loan purpose, residence type, etc.

**✔ Default Probability (0–100%)**  
The model outputs the applicant’s likelihood of default using logistic regression.

**✔ Credit Score (300–900)**  
A custom scoring formula converts probability → score.

**✔ Credit Rating Classification**  
- Excellent  
- Good  
- Average  
- Poor  

**✔ Premium UI / UX**  
A modern, fintech-style interface with:  
- Gradient header  
- Clean input layout  
- Risk heat color indicator  
- Premium result box  
- Credit score gauge (linear meter)  
- Animated high-risk alerts  

---

## 🧠 Machine Learning Model
**Algorithm:** Logistic Regression  
**Training Pipeline Includes:**  
- Feature engineering  
- Scaling (MinMaxScaler)  
- Dummy variable encoding  
- Custom risk-score transformation  
- Model saved via `joblib`

**Top Predictive Features (based on coefficients):**  
- Loan-to-Income Ratio  
- Credit Utilization Ratio  
- Delinquency Ratio  
- Average DPD per Delinquency  
- Number of Open Accounts  
- Residence Type  
- Loan Purpose & Loan Type  

---



## 📂 Project Structure

```bash
project/
│
├── main.py                     # Streamlit UI Application
├── prediction_helper.py        # Prediction pipeline (model loading, preprocessing & scoring)
│
├── artifacts/                  # Saved model + preprocessing assets
│   └── model_data.joblib       # Trained ML model, scaler, features, metadata
│
├── README.md                   # Full project documentation
│

```



## 🧩 How It Works
1. User enters loan and personal information  
2. Data is preprocessed & scaled  
3. Logistic Regression calculates default probability  
4. Probability → Credit Score (300–900)  
5. UI displays:
   - Default Probability  
   - Credit Score  
   - Rating (Poor → Excellent)  
   - Gauge Meter  
   - Risk Heat Indicator  
   - High-Risk Alert if probability > 40%

---

## 📸 Screenshots

### 🔹 Credit Assessment Result  
<img width="1411" height="810" alt="image" src="https://github.com/user-attachments/assets/f394fb11-9d03-47a8-8a83-862d10cc2402" />







---

## 🛠️ Tech Stack

**Frontend/UI:**  
- Streamlit  
- Basic HTML/CSS for premium styling  

**Backend & ML:**  
- Python  
- Scikit-learn  
- Pandas  
- Numpy  
- Joblib  

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/<repo-name>
cd <repo-name>

pip install -r requirements.txt
streamlit run main.py
