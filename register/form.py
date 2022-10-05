from django import forms
from login.models import Login

class registerform(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        labels = {
            'account_name': ('帳號'),
            'password_name': ('密碼'),
        }

