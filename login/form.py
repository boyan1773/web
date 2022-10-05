from tkinter import Widget
from tkinter.ttk import Style
from turtle import window_height
from django import forms
from .models import Login

class loginform(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        labels = {
            'account_name': ('帳號'),
            'password_name': ('密碼'),
        }
            
