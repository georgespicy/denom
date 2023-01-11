from django import forms
from .models import Subcriber


class SubcriberForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Your email here', 'class': 'Enter_text'}))

    class Meta():
        model = Subcriber
        fields = ('email',)
