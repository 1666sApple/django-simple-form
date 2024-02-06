from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    email = forms.EmailField(label="Your email", max_length=100)
    verify_email = forms.EmailField(label="Enter your email again:", max_length=100)
    text = forms.CharField(widget=forms.Textarea)