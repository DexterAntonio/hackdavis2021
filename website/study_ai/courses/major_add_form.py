from django import forms

class CommentForm(forms.Form):
    major_title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Major Title"
        })
    )
    major_website = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Department Website"
        })
    )

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Enter Major Requirement"
        })
    )