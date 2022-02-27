from django import forms

from blog.models import Posts


class CreateUpdatePost(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('likes', 'slug')
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'author': forms.HiddenInput(),
            'active': forms.HiddenInput(),
        }
