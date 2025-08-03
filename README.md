🔹 Description:
This web-based application, built with Django, is designed to streamline patient registration and provide early risk predictions for multiple health conditions using machine learning models. Patients can be registered through a simple interface, and their health parameters are used to assess the likelihood of anemia, diabetes, cardiac arrest, and stroke. The application helps healthcare providers or system users make informed decisions with the support of data-driven insights.

🔹 Key Features:
Patient Registration: A centralized form to register patient details including name, age, gender, and medical history.

Disease Prediction Modules:

Anemia Prediction: Based on parameters like Hemoglobin, MCH, MCHC, and MCV.

Diabetes Prediction: Uses Glucose, BMI, Insulin, and other key factors.

Cardiac Arrest Prediction: Analyzes data like chest pain type, cholesterol, and heart rate.

Stroke Prediction: Involves parameters such as hypertension, smoking status, and heart disease.

Machine Learning Integration: Each prediction module is backed by a trained ML model, providing real-time results based on input data.

Unified Patient Reference: A common name field connects all predictions to a specific patient record.

Result Display: Visual output or classification (e.g., “High Risk”, “Low Risk”) for each condition after submission.

Admin Panel: Django admin is used for managing patient records and viewing prediction outcomes.

🔹 Tech Stack:
Backend: Python, Django

Frontend: HTML, CSS, Bootstrap (optional for UI)

Database: SQLite

Machine Learning: Scikit-learn (for loading pre-trained models via joblib or pickle)

Tools: Django Admin, Django ORM
