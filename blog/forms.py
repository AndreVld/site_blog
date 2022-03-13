from django import forms

from blog.models import Posts, Comments


class CreateUpdatePost(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ('likes', 'slug')
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'author': forms.HiddenInput(),
            'active': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ('created_at',)
        widgets = {
            'post': forms.HiddenInput(),
            'comment_author': forms.HiddenInput(),
            'parent_comment': forms.HiddenInput(),
        }
