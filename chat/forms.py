from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    # review = forms.CharField()
    class Meta:
        model = Contact
        fields = "__all__"
        # fields =["name", "email", "type", "message", "review"]