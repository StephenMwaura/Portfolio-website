from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "class": "form-input"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "class": "form-input"}),
            "message": forms.Textarea(attrs={"placeholder": "Your message...", "class": "form-input", "rows": 6}),
        }

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 10:
            raise forms.ValidationError("Your message is a bit short — tell me a little more.")
        return message