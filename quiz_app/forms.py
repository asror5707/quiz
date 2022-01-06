from django import forms

from .models import Savol,Quiz
class SavolForm(forms.ModelForm):
    class Meta:
        model = Savol
        fields = ['matn','quiz']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['nom','batafsil','savol_soni','davomiyligi']