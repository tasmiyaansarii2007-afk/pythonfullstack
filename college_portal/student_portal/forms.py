from django import forms

class Student_form_data(forms.Form):
   reg_no=forms.IntegerField()
   name1=forms.CharField()
   email1=forms.EmailField()