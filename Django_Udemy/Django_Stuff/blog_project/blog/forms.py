from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    # Grab fields directly from Post model
    class Meta():
        model = Post
        fields = ('author', 'title', 'text') # ("__all__") would get all fields
        # to edit a particular field or widget
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
