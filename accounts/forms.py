from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'username','placeholder':'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password', 'autocomplete': 'off', 'placeholder': 'Password'}))
    # errors=[]
    def clean_username(self):
        username = self.cleaned_data.get('username')

        # print(f'\n\nform,cleaned_data:{self.cleaned_data}\n\n')
        
        qs = User.objects.filter(username__iexact=username)

        if not qs.exists():
            # LoginForm.errors.append('User doesn\'t exist.')
            raise forms.ValidationError('Incorrect Username or Password')
        return username