import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked

# ---------------------------------------------------
# PREMIUM PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Easy Finance: Credit Risk Modelling",
    page_icon="🏦",
    layout="wide"
)


# ---------------------------------------------------
# PREMIUM HEADER DESIGN
# ---------------------------------------------------
# PREMIUM HEADER
# ---------------------------------------------------
st.markdown("""
    <style>
        .header {
            background: linear-gradient(90deg, #003C6C, #99BFCF);
            padding: 15px 10px;
            border-radius: 12px;
            text-align: center;
            color: white;
            font-size: 32px;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            letter-spacing: 0.5px;
        }
        .subheader {
            text-align: center;
            font-size: 16px;
            color: #4a4a4a;
            margin-top: 8px;
            margin-bottom: 10px;
        }
        .box {
            background: #ffffff;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }
        .result-box {
            background: #f8f9fa;
            padding: 20px;
            border-left: 6px solid #00416A;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>

    <div class="header">🏦 Easy Finance – Credit Risk Modelling</div>
    <div class="subheader">Smart. Fast. Reliable credit score decisions.</div>
""", unsafe_allow_html=True)



# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.subheader("📄 Customer Information")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# --- Row 1 ---
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income (₹)', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000)

# Loan-to-income ratio
loan_to_income_ratio = loan_amount / income if income > 0 else 0

# --- Row 2 ---
with row2[0]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")

with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)

with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

# --- Row 3 ---
with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)

with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)

with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=10, step=1, value=2)

# --- Row 4 ---
with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])

with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])

with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------
# CALCULATE BUTTON + RESULT BOX
# ---------------------------------------------------
if st.button("🔍 Calculate Risk", use_container_width=True):

    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months,
        avg_dpd_per_delinquency, delinquency_ratio,
        credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Premium Output Box
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader("📊 Credit Assessment Result")

    st.write(f"**Default Probability:** `{probability:.2%}`")
    st.write(f"**Credit Score:** `{credit_score}`")
    st.write(f"**Rating:** `{rating}`")

    st.markdown("</div>", unsafe_allow_html=True)
