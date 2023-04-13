from django import forms
from django.forms import ModelForm
from .models import Feature


class Reg_form(ModelForm):
    class Meta:
        model=Feature
        fields={
                "roll_no",
                "sem_reg",
                "hostel_name",
                "room_no",
                "department",
                "programme",
                "name",
                "email",
                "phone_number",
                "pincode",
                "address",
                "address2",
                "amount",
                "cgpi",
                "sgpi",
                "transaction_number",
                "date_of_payment",
                "fathers_name"

            }
        labels={
                'roll_no':"Roll Number",
                'sem_reg':"Registered Semester Number",
                'hostel_name':"Hostel Name",
                'room_no':"Hostel Room No",
                'department':"Department",
                'programme':"Programme",
                'name':"Name",
                'email':"Email",
                'phone_number':"Phone Number",
                'pincode':"Pincode",
                'address':"Permanent Address",
                'address2':"Correspondance Address",
                'cgpi':"CGPI",
                'sgpi':"SGPI",
                'amount':"Amount",
                'transaction_number':"transaction_number",
                'date_of_payment':"date_of_payment",
                'fathers-name':"fathers_name"
                }
        help_text ={'roll_no':"20BCS000",
                    'sem_reg':'Current Semester you are applying to',
                }
        widgets={
                'roll_no':forms.TextInput(attrs={'class':'form-control','placeholder':'20XXX000'}),
                'sem_reg':forms.TextInput(attrs={'class':'form-control','placeholder':'2'}),
                'hostel_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Satpura Hostel'}),
                'room_no':forms.TextInput(attrs={'class':'form-control','placeholder':'A-0001'}),
                'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Computer Science and Engineering Department','row':'1'}),
                'programme':forms.TextInput(attrs={'class':'form-control','placeholder':'B.Tech'}),
                'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Full Name'}),
                'fathers_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Father Name'}),
                'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'20xxx000@nith.ac.in'}),
                'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'9999999999'}),
                'pincode':forms.TextInput(attrs={'class':'form-control','placeholder':'111111'}),
                'address':forms.Textarea(attrs={'class':'form-control form-control-lg','placeholder':'Your permanent address',}),
                'address2':forms.Textarea(attrs={'class':'form-control form-control-lg','placeholder':'Your correspondence address'}),
                'cgpi':forms.TextInput(attrs={'class':'form-control','placeholder':'7.5'}),
                'sgpi':forms.TextInput(attrs={'class':'form-control','placeholder':'7.5'}),
                'amount':forms.TextInput(attrs={'class':'form-control','placeholder':'College Fees Paid'}),
                'transaction_number':forms.TextInput(attrs={'class':'form-control','placeholder':'SBI Collect Reference Number'}),
                'date_of_payment':forms.DateInput(attrs={'class':'form-control','placeholder':'01/01/2023'}),
        }

