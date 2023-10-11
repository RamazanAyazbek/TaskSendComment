from django import forms
from .models import Review
from django.core.exceptions import ValidationError

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
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if photo.size > 1024 * 1024:
                raise ValidationError('Image size should not exceed 1MB.')
        return photo




