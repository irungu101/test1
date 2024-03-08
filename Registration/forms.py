from Registration.models import Student
from django import forms


class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=10, required=True)
    last_name = forms.CharField(max_length=10, required=True)
    email = forms.EmailField()
    date_of_birth = forms.DateField()
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'phone_number', 'password']