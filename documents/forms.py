from django import forms # new 
from .models import Document#new 
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth import get_user_model


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('markdown',)


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()#=> auth.User
#         fields = ('username', 'email', 'first_name','last_name')

        