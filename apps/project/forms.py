from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(label='邮箱', error_messages={
        'required': '邮箱不能为空',
        'invalid': '邮箱不合法'
    })
