from django.db import models

# Create your models here.
class Feature(models.Model):
    department= models.CharField(max_length=50)
    programme= models.CharField(max_length=20)
    hostel_name= models.CharField(max_length=20)
    room_no=models.CharField(max_length=6)
    roll_no= models.CharField(max_length=8)
    name = models.CharField(max_length=50)
    # hindi_name= models.CharField(max_length=100)
    fathers_name=models.CharField(max_length=50)
    date_of_payment=models.DateField()
    transaction_number=models.CharField(max_length=17)
    address= models.TextField(max_length=500)
    address2= models.TextField(max_length=500)
    email=  models.EmailField(max_length=50)
    sem_reg=models.IntegerField()
    phone_number=models.IntegerField()
    amount=models.IntegerField()
    pincode= models.IntegerField()
    sgpi=models.FloatField(max_length=5)
    cgpi=models.FloatField(max_length=5)

class Semester_subjects(models.Model):
    rollno=models.IntegerField(null=True)
# list for open elective
