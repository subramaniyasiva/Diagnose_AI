from django.db import models
from django.utils import timezone

# Create your models here.
class patient_detials(models.Model):
    Patient_name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=8)
    mail=models.EmailField()
    city=models.CharField(max_length=35)
    Address=models.CharField(max_length=60)
    Mobile_Number=models.IntegerField()
    
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Patient_name

class cardiac_arrest(models.Model):
    pname=models.CharField(max_length=35)
    age=models.IntegerField()
    Sex=models.CharField(max_length=7)
    Chestpaintype=models.CharField(max_length=5)
    RestingBP=models.IntegerField()
    Cholestrol=models.IntegerField()
    FastingBP=models.IntegerField()
    RestingECG=models.CharField(max_length=35)
    MAXHR=models.IntegerField()
    Excersice_angina=models.CharField(max_length=7)
    oldpeak=models.IntegerField()
    STslope=models.CharField(max_length=83)
    result=models.CharField(max_length=123,null=True, blank=True)
    
    
    def __str__(self):
        return self.pname

class diabetics(models.Model):
    pname=models.CharField(max_length=150)
    # sex=models.CharField(max_length=21)
    pregnanicies=models.IntegerField()
    glucose=models.IntegerField()
    bp=models.IntegerField()
    skinthickness=models.IntegerField()
    insulin=models.IntegerField()
    bmi=models.DecimalField(decimal_places=5,max_digits=9)
    diabetespedigreefunction=models.DecimalField(decimal_places=5,max_digits=9)
    age=models.IntegerField()
    result=models.CharField(max_length=29,null=True,blank=True)
    def __str__(self):
        return self.pname
    
class stroke_pred(models.Model):
    pname=models.CharField(max_length=25)
    age=models.IntegerField()
    gender=models.CharField(max_length=31)
    hypertension=models.IntegerField()
    heartdisease=models.IntegerField()
    evermarried=models.CharField(max_length=32)
    worktype=models.CharField(max_length=35)
    residencetype=models.CharField(max_length=34)
    averageglucoselevel=models.IntegerField()
    bmi=models.DecimalField(max_digits=6,decimal_places=4)
    smokingstatus=models.CharField(max_length=31)
    stroke_result=models.CharField(max_length=22)
    def __str__(self):
         return self.pname

class anemia_hemo(models.Model):
    pname=models.CharField(max_length=50)
    gender=models.IntegerField()
    hemo=models.IntegerField()
    mch=models.IntegerField()
    mchc=models.IntegerField()
    mcv=models.IntegerField()
    anemia_result=models.CharField(max_length=120,null=False)
    def __str__(self):
        self.pname
    
    