from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name",max_length=50),
    phone = forms.CharField(label="Phone",max_length=50),
    email = forms.CharField(label="Email",max_length=50),
    # message = forms.Textarea(label="Name",max_length=50),