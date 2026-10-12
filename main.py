from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


MODEL_PATH = Path(__file__).with_name("bank_dt_joblib.joblib")
FEATURES = [
	"age",
	"job",
	"marital",
	"education",
	"default",
	"balance",
	"housing",
	"loan",
	"contact",
	"day",
	"month",
	"duration",
	"campaign",
	"pdays",
	"previous",
	"poutcome",
]


@st.cache_resource
def load_model():
	loaded_object = joblib.load(MODEL_PATH)

	if isinstance(loaded_object, dict):
		for key in ("model", "estimator", "classifier", "pipeline", "clf"):
			candidate = loaded_object.get(key)
			if hasattr(candidate, "predict"):
				return candidate
		for value in loaded_object.values():
			if hasattr(value, "predict"):
				return value
		raise TypeError(
			f"Saved model file does not contain a prediction model. Loaded dict keys: {list(loaded_object.keys())}"
		)

	if hasattr(loaded_object, "predict"):
		return loaded_object

	raise TypeError(f"Saved model file type is not supported: {type(loaded_object).__name__}")


st.set_page_config(page_title="Bank Deposit Predictor", layout="wide")
st.title("Bank Deposit Predictor")
st.caption("Estimate whether a client will subscribe to a term deposit.")

model = None
model_error = None
try:
	model = load_model()
except ModuleNotFoundError as error:
	model_error = f"Model dependency not installed: {error.name}. Install the packages in requirements.txt."
except Exception as error:
	model_error = f"The saved model could not be loaded: {error}"

if model_error:
	st.error(model_error)

with st.form("prediction_form"):
	st.subheader("Client profile")
	col1, col2, col3 = st.columns(3)
	with col1:
		age = st.number_input("Age", min_value=18, max_value=100, value=40, step=1)
		job = st.selectbox(
			"Job",
			[
				"admin.",
				"blue-collar",
				"entrepreneur",
				"housemaid",
				"management",
				"retired",
				"self-employed",
				"services",
				"student",
				"technician",
				"unemployed",
				"unknown",
			],
		)
		marital = st.selectbox("Marital status", ["married", "single", "divorced", "unknown"])
		education = st.selectbox(
			"Education",
			[
				"secondary",
				"tertiary",
				"primary",
				"unknown",
				"basic.4y",
				"basic.6y",
				"basic.9y",
				"high.school",
				"illiterate",
				"professional.course",
				"university.degree",
			],
		)
	with col2:
		default = st.selectbox("Credit in default", ["no", "yes", "unknown"])
		balance = st.number_input("Average yearly balance", value=1500, step=100)
		housing = st.selectbox("Housing loan", ["yes", "no", "unknown"])
		loan = st.selectbox("Personal loan", ["no", "yes", "unknown"])
		contact = st.selectbox("Contact type", ["cellular", "telephone", "unknown"])
	with col3:
		day = st.number_input("Last contact day of month", min_value=1, max_value=31, value=15, step=1)
		month = st.selectbox(
			"Last contact month",
			["may", "jan", "feb", "mar", "apr", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
		)
		duration = st.number_input("Last contact duration (seconds)", min_value=0, value=180, step=10)
		campaign = st.number_input("Contacts during this campaign", min_value=1, value=1, step=1)
		pdays = st.number_input("Days since previous contact (-1 = never)", min_value=-1, value=-1, step=1)
		previous = st.number_input("Contacts before this campaign", min_value=0, value=0, step=1)
		poutcome = st.selectbox("Previous campaign outcome", ["unknown", "failure", "other", "success"])

	submitted = st.form_submit_button("Predict subscription", type="primary", disabled=model is None)

if submitted and model is not None:
	row = {
		"age": age,
		"job": job,
		"marital": marital,
		"education": education,
		"default": default,
		"balance": balance,
		"housing": housing,
		"loan": loan,
		"contact": contact,
		"day": day,
		"month": month,
		"duration": duration,
		"campaign": campaign,
		"pdays": pdays,
		"previous": previous,
		"poutcome": poutcome,
	}
	input_data = pd.DataFrame([[row[feature] for feature in FEATURES]], columns=FEATURES)

	try:
		prediction = model.predict(input_data)[0]
		st.subheader("Prediction")
		st.metric("Estimated outcome", str(prediction).replace("_", " ").title())

		if hasattr(model, "predict_proba"):
			probabilities = model.predict_proba(input_data)[0]
			classes = list(getattr(model, "classes_", []))
			positive_index = next(
				(index for index, label in enumerate(classes) if str(label).lower() == "yes"),
				None,
			)
			if positive_index is not None and positive_index < len(probabilities):
				st.metric("Estimated subscription probability", f"{probabilities[positive_index]:.1%}")
	except Exception as error:
		st.error(f"Prediction failed: {error}")
