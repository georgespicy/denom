from django import forms
from .models import Subcriber, Contact



class ContactForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Full Name', 'class': 'mail_text'}))

    phone_number = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'phone number', 'class': 'mail_text'}))

    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'your email here', 'class': 'mail_text'}))

    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'placeholder': 'Message',
            'class': 'massage-bt', 
            'id': 'comment'
        }
    ))

    class Meta():
        model = Contact
        fields = ('first_name', 'phone_number', 'email', 'message')
