# from django import forms
# from .models import User, ContactUs
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserLoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = ContactUs
#         fields = ['name', 'email', 'message']

        
        
# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required. Enter a valid email address.')
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']



from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Name',
            'email': 'Email',
            'password1': 'password1',
            'password2': 'password2',}

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']






from .models import FormData

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['field1', 'field2', 'field3']
        labels = {
            'field1': 'Name',
            'field2': 'Email',
            'field3': 'Message',
        }