from django import forms
from Confession.models import ConfessionPost

class ConfessionForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = ConfessionPost
        fields = ('title', 'content', 'display_name')