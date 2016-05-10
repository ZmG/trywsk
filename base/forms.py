from django import forms

class NewsSubscribeForm(forms.Form):

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'email address', 'class':'input-large'}))

