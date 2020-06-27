#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User
#
#
# class SignUpForm(UserCreationForm):
#     user_name = forms.CharField(max_length=200, null=False)
#     user_mobile = forms.CharField(max_length=200, null=True)
#     user_email = forms.EmailField(max_length=200, null=True)
#     user_address = forms.CharField(max_length=200, null=True)
#     user_password = forms.CharField(max_length=200, null=False, default="password")
#
#
#     class Meta:
#         model = User
#         fields = ('user_name', 'user_mobile', 'user_email', 'user_address','user_password','profile_photo','public_id')
#
#
