from django import forms
from Blog.models import BlogPost, Images


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    content = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = BlogPost
        fields = ('title', 'content',)


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image',)
