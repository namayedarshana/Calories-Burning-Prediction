import streamlit as st
import pickle 
import pandas as pd

st.set_page_config(
    page_title="Calories Burn Prediction",
    page_icon="🔥",
    layout="centered"
)

with open("calories_model.pkl", "rb") as file:
    model = pickle.load(file)
    
    
st.title("🔥 Calories Burn Prediction")

st.write(
    "Predict the number of calories burned during exercise "
    "using a Machine Learning model."
)
st.divider()

st.subheader("🏃 Enter Exercise Details")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=150,
        value=28,
        step=1
    )

    height = st.number_input(
        "Height (cm)",
        min_value=1.0,
        max_value=300.0,
        value=165.0,
        step=1.0
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=60.0,
        step=1.0
    )


# RIGHT COLUMN
with col2:

    duration = st.number_input(
        "Exercise Duration (minutes)",
        min_value=1.0,
        max_value=1000.0,
        value=30.0,
        step=1.0
    )

    heart_rate = st.number_input(
        "Heart Rate (bpm)",
        min_value=1.0,
        max_value=1000.0,
        value=100.0,
        step=1.0
    )

    body_temp = st.number_input(
        "Body Temperature (°C)",
        min_value=1.0,
        max_value=100.0,
        value=38.0,
        step=0.1
    )


st.divider()

if st.button("🔥 Predict Calories", use_container_width=True):
    

    # -----------------------------------------------
    # VALIDATION
    # -----------------------------------------------

    errors = []

    # Age validation
    if age < 1 or age > 100:
        errors.append("⚠️ Please enter an age between 1 and 100 years.")

    # Height validation
    if height < 50 or height > 250:
        errors.append("⚠️ Please enter height between 50 and 250 cm.")

    # Weight validation
    if weight < 20 or weight > 200:
        errors.append("⚠️ Please enter weight between 20 and 200 kg.")

    # Duration validation
    if duration < 1 or duration > 300:
        errors.append(
            "⚠️ Please enter exercise duration between 1 and 300 minutes."
        )

    # Heart rate validation
    if heart_rate < 40 or heart_rate > 220:
        errors.append(
            "⚠️ Please enter heart rate between 40 and 220 bpm."
        )

    # Body temperature validation
    if body_temp < 35 or body_temp > 45:
        errors.append(
            "⚠️ Please enter body temperature between 35 and 45 °C."
        )


    # -----------------------------------------------
    # SHOW VALIDATION ERRORS
    # -----------------------------------------------

    if errors:

        for error in errors:
            st.error(error)


    # -----------------------------------------------
    # MAKE PREDICTION
    # -----------------------------------------------

    else:

        # Gender encoding
        if gender == "Female":
            gender_encoded = 0
        else:
            gender_encoded = 1


        # Create input DataFrame
        input_data = pd.DataFrame({

            "Gender": [gender_encoded],

            "Age": [age],

            "Height": [height],

            "Weight": [weight],

            "Duration": [duration],

            "Heart_Rate": [heart_rate],

            "Body_Temp": [body_temp]
        })


# Prediction
        prediction = model.predict(input_data)

        predicted_calories = prediction[0]


        # -------------------------------------------
        # DISPLAY RESULT
        # -------------------------------------------

        st.success(
            f"🔥 Estimated Calories Burned: "
            f"{predicted_calories:.2f} calories"
        )


        # -------------------------------------------
        # INPUT SUMMARY
        # -------------------------------------------

        st.subheader("📋 Input Summary")

        summary = pd.DataFrame({

            "Parameter": [
                "Gender",
                "Age",
                "Height",
                "Weight",
                "Exercise Duration",
                "Heart Rate",
                "Body Temperature"
            ],

            "Value": [
                gender,
                f"{age} years",
                f"{height} cm",
                f"{weight} kg",
                f"{duration} minutes",
                f"{heart_rate} bpm",
                f"{body_temp} °C"
            ]
        })


        st.table(summary)

