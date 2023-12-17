from django import forms


class newPost(forms.Form):

    content = forms.CharField( widget=forms.Textarea, label='')
    