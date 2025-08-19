from django.shortcuts import render,redirect
from .models import patient_detials,cardiac_arrest,diabetics,stroke_pred,anemia_hemo
from django.conf import settings
import os
import joblib
import numpy as np
import pandas as pd
# Create your views here.

MODEL_PATH = os.path.join(settings.BASE_DIR, 'DiagnoseAI', 'trainedmodels', 'cardiac_model.pkl')
MODEL_PATHd = os.path.join(settings.BASE_DIR, 'DiagnoseAI', 'trainedmodels', 'diabetes.joblib')
MODEL_PATHs = os.path.join(settings.BASE_DIR, 'DiagnoseAI', 'trainedmodels', 'stroke_pipeline.pkl')
model_patha=os.path.join(settings.BASE_DIR, 'DiagnoseAI', 'trainedmodels', 'anemia.pkl')
model_pathl=os.path.join(settings.BASE_DIR, 'DiagnoseAI', 'trainedmodels', 'liver_rfmodel.pkl')



modelc=joblib.load(MODEL_PATH)
modeldd=joblib.load(MODEL_PATHd)
models1=joblib.load(MODEL_PATHs)
modela=joblib.load(model_patha)
modell=joblib.load(model_pathl)

def patient(requests):
    if requests.method=="POST":
        PatientName=requests.POST.get('pname')
        Age=requests.POST.get('Age')
        Gender=requests.POST.get('gender')
        mail=requests.POST.get('mail')
        city=requests.POST.get('city')
        address=requests.POST.get('Address')
        Mobile_Number=requests.POST.get('MobileNumber')
        obj = patient_detials(Patient_name=PatientName,Age=Age,Gender=Gender,mail=mail,city=city,Address=address,Mobile_Number=Mobile_Number)
        

        obj.save()
        print(PatientName)
        return render(requests,"success.html")
           
    return render(requests,'Patient.html')
def success(requests):
    return render(requests,"success.html")
def cardiac(request):
    if request.method == "POST":
        # Get form data
        pname = request.POST.get('name')
        age = int(request.POST.get('age'))
        sex = request.POST.get('sex')  # 'Male' or 'Female'
        chest_pain = request.POST.get('chest_pain')
        resting_bp = int(request.POST.get('resting_bp'))
        cholesterol = int(request.POST.get('cholesterol'))
        fasting_bs = int(request.POST.get('fasting_bs'))
        resting_ecg = request.POST.get('resting_ecg')
        max_hr = int(request.POST.get('max_hr'))
        exercise_angina = request.POST.get('exercise_angina')
        oldpeak = float(request.POST.get('oldpeak'))
        st_slope = request.POST.get('st_slope')

        # Create DataFrame with correct column names
        features = pd.DataFrame({
            'Age': [age],
            'RestingBP': [resting_bp],
            'Cholesterol': [cholesterol],
            'FastingBS': [fasting_bs],
            'MaxHR': [max_hr],
            'Oldpeak': [oldpeak],
            'Sex': [sex],
            'ChestPainType': [chest_pain],
            'RestingECG': [resting_ecg],
            'ExerciseAngina': [exercise_angina],
            'ST_Slope': [st_slope]
        })

        # Prediction
        prediction = modelc.predict(features)[0]
        print("Input Features:\n", features)
        print("Prediction:", prediction)

        # Show result message
        if prediction == 1:
            message = 'There is a chance of cardiac arrest.'
        else:
            message = 'Patient is normal.'
        

        # Save to database
        obj = cardiac_arrest(
            pname=pname,
            age=age,
            Sex=sex,
            Chestpaintype=chest_pain,
            RestingBP=resting_bp,
            Cholestrol=cholesterol,
            FastingBP=fasting_bs,
            RestingECG=resting_ecg,
            MAXHR=max_hr,
            Excersice_angina=exercise_angina,
            oldpeak=oldpeak,
            STslope=st_slope,
            result=message
        )
        obj.save()

        # Show message in result page
        return render(request, 'cardiac_arrest.html', {'message': message})

    return render(request, 'cardiac_arrest.html')

def diabeticss(requests):
    if requests.method=="POST":
        pname1=requests.POST.get('pname1')
        age=requests.POST.get('age')
        pregnancies=requests.POST.get('pregnancies')
        glucose=requests.POST.get('glucose')
        bp=requests.POST.get('bp')
        skinthickness=requests.POST.get('skinthickness')
        insulin=requests.POST.get('insulin')
        bmi=requests.POST.get('bmi')
        dpf=requests.POST.get('dpf')
        print(dpf)
        dia_input=pd.DataFrame({
            'Pregnancies':[pregnancies],
            'Glucose':[glucose],
            'BloodPressure':[bp],
            'SkinThickness':[skinthickness],
            'Insulin':[insulin],
            'BMI':[bmi],
            'DiabetesPedigreeFunction':[dpf],
            'Age':[age]
            
            
        })
        diabetics_prediction=modeldd.predict(dia_input)
        print(diabetics_prediction)
        dia_result="Patient is Diabetic" if diabetics_prediction==1 else "Not a Diabeteic"
        print(dia_input)
        obj1=diabetics(
            pname=pname1,
            pregnanicies=pregnancies,
            glucose=glucose,
            bp=bp,
            skinthickness=skinthickness,
            insulin=insulin,
            bmi=bmi,
            diabetespedigreefunction=dpf,
            age=age,
            result=dia_result
            
            
            
            
        )
        obj1.save()
        return render(requests,'diabetics.html',{'dia_result':dia_result})
    
        
    return render(requests,'diabetics.html')

def predict_stroke(request):
    if request.method == 'POST':
        # Get data from form POST
        pname=request.POST.get('pname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        hypertension = int(request.POST.get('hypertension'))
        heart_disease = int(request.POST.get('heart_disease'))
        ever_married = request.POST.get('ever_married')
        work_type = request.POST.get('work_type')
        Residence_type = request.POST.get('Residence_type')
        avg_glucose_level = float(request.POST.get('avg_glucose_level'))
        bmi = float(request.POST.get('bmi'))
        smoking_status = request.POST.get('smoking_status')

        # Create DataFrame for prediction
        input_data = pd.DataFrame([{
            'gender': gender,
            'age': age,
            'hypertension': hypertension,
            'heart_disease': heart_disease,
            'ever_married': ever_married,
            'work_type': work_type,
            'Residence_type': Residence_type,
            'avg_glucose_level': avg_glucose_level,
            'bmi': bmi,
            'smoking_status': smoking_status
        }])

        # Make prediction
        prediction = models1.predict(input_data)[0]

        stroke_result = "Chances of Stroke" if prediction == 1 else "No chance of Stroke"

        obj2=stroke_pred(
            pname=pname,
            age=age,
            gender=gender,
            hypertension=hypertension,
            heartdisease=heart_disease,
            evermarried=ever_married,
            worktype=work_type,
            residencetype=Residence_type,
            averageglucoselevel=avg_glucose_level,
            bmi=bmi,
            smokingstatus=smoking_status,
            stroke_result=stroke_result
        )
        obj2.save()
        return render(request, 'stroke_prediction.html', {'result': stroke_result})

    return render(request, 'stroke_prediction.html')

def anemia(requests):
    if requests.method=='POST':
        pname=requests.POST.get('pname1')
        gender=float(requests.POST.get('gender'))
        print(type(gender))
        hemo=float(requests.POST.get('hemo'))
        print(type(hemo))
        
        mch=float(requests.POST.get('mch'))
        print(type(mch))
        
        mchc=float(requests.POST.get('mchc'))
        print(type(mchc))
        
        mcv=float(requests.POST.get('mcv'))
        print(type(mcv))
        
        print(pname,gender,hemo,mch,mchc,mcv)
        anemia_input=pd.DataFrame({
            'Gender':[gender],
            'Hemoglobin':[hemo],
            'MCH':[mch],
            'MCHC':[mchc],
            'MCV':[mcv]
            
            
        })
   
        anemia_pred=modela.predict(anemia_input)

        print(anemia_input)
        print(anemia_pred)
        anemia_result="You have anemia" if anemia_pred==1 else "No Anemia"
        print(anemia_result)
        obj3=anemia_hemo(
            pname=pname,
            gender=gender,
            hemo=hemo,
            mch=mch,
            mchc=mchc,
            mcv=mcv,
            anemia_result=anemia_result
            )
        obj3.save()
        return render(requests,'anemia.html',{'anemia_result':anemia_result})
    return render(requests,'anemia.html')
def livers(requests):
    if requests.method=='POST':
        pname=requests.POST.get('pname')
        age=requests.POST.get('age')
        gender=requests.POST.get('gender')
        tb=requests.POST.get('tb')
        db=requests.POST.get('db')
        ap=requests.POST.get('ap')
        aa=requests.POST.get('aa')
        asa=requests.POST.get('asa')
        tp=requests.POST.get('tp')
        al=requests.POST.get('al')
        alg=requests.POST.get('alg')
        print(alg)
        features = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Total_Bilirubin': [tb],
            'Direct_Bilirubin': [db],
            'Alkaline_Phosphotase': [ap],
            'Alamine_Aminotransferase': [aa],
            'Aspartate_Aminotransferase': [asa],
            'Total_Protiens': [tp],
            'Albumin': [al],
            'Albumin_and_Globulin_Ratio': [alg]
            
        })
        liver_di=modell.predict(features)
        liver_result="liver disease traces are there" if liver_di==2 else "no traces"
        print(liver_di)        
        print(liver_result)
        
        return render(requests,'liver.html',{'lr':liver_result})
    return render(requests,'liver.html')
    
        
        
        
        
        
        
        
        