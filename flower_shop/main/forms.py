from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'validationCustom01', 'required': True}))
    
    class Meta:
        model = Feedback
        fields = ('body', )
    # <input type="text" class="form-control" id="validationCustom01" required>
