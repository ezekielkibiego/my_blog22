from .models import Blog, Author
from django import forms

class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), 
                                    empty_label='Select an author')
    
    class Meta:
        model = Blog
        fields = ['author', 'title', 'text', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)