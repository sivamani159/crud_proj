from django import forms 

CHOICES=(
    ("1","python"),
    ("2","django"),
    ("3","devops"),
    ("4","others")
)

class Student(forms.Form):
    name=forms.CharField(label='name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    email=forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    courses=forms.ChoiceField(choices=CHOICES)
    jdate=forms.DateField(label='jdate',widget=forms.DateInput(attrs={'class':'form-control','placeholder':'jdate'}))