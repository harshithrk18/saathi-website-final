from django import forms
from saathiweb.models import Student

class AppointmentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        }))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Webmail ID'
        }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your message'
    }))


    class Meta():
        model = Student
        fields = '__all__'
