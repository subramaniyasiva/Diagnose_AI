🏥 MediCheckAI – Patient Registration & Disease Risk Prediction System
🔹 Description

MediCheckAI is a web-based application built with Django that streamlines patient registration and provides early risk predictions for multiple health conditions using machine learning models. Healthcare providers can register patients through a simple interface and instantly receive predictive insights on conditions such as anemia, diabetes, cardiac arrest, liver failure, and stroke. This system supports data-driven decision-making and enhances preventive healthcare.

🔹 Key Features

Patient Registration: Centralized form to capture details (name, age, gender, medical history).

Disease Prediction Modules:

Anemia → Hemoglobin, MCH, MCHC, MCV

Diabetes → Glucose, BMI, Insulin, etc.

Cardiac Arrest → Chest pain type, cholesterol, heart rate

Liver Failure → Liver enzyme levels, bilirubin, protein values

Stroke → Hypertension, smoking status, heart disease

Machine Learning Integration: Each module powered by a trained ML model (Random Forest, Decision Tree, KNN, XGBoost, LightGBM tested; best-performing model deployed).

Unified Patient Reference: All predictions tied to a single patient record.

Result Display: Clear output classification (“High Risk”, “Low Risk”) with visual indicators.

Admin Panel: Manage patient data and review prediction outcomes via Django Admin.

🔹 Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (extendable to PostgreSQL/MySQL)

ML Libraries: Pandas, NumPy, Seaborn, Scikit-learn, LabelEncoder, StandardScaler

ML Algorithms Tested: Random Forest, Decision Tree, KNN, XGBoost, LightGBM, etc. → evaluated using accuracy & classification report

Deployment Tools: Django ORM, joblib/pickle for loading models
