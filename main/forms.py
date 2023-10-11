from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=("name", "email", "text", "photo")
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control border"}),
            "email":forms.EmailInput(attrs={"class":"form-control border"}),
            "text":forms.Textarea(attrs={"class":"form-control border"}),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control-file"}) 
        }




