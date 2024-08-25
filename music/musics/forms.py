from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment=forms.CharField(
        max_length=60,
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Type comment...','id':'addANote','name':'comment','rows':"2" ,'cols':"25",'maxlength':'60',})
    )
    class Meta:
        model=Comment
        fields=("comment",)