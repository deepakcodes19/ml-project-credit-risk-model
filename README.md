
---

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

### 🔹 Premium UI Header  
![Header](path/to/header.png)

### 🔹 Input Form  
![Inputs](path/to/inputs.png)

### 🔹 Credit Assessment Result  
![Results](path/to/results.png)

*(Place screenshots here once you upload them.)*

---

## 🛠️ Tech Stack

**Frontend/UI:**  
- Streamlit  
- HTML/CSS for premium styling  

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
