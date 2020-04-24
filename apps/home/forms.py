from django import forms


class ContactEmailForm(forms.Form):
    nickname = forms.CharField(max_length=20, label='昵称', min_length=2, error_messages={
        'min_length': '标题字段不符合要求!'
    })
    email = forms.EmailField(label='邮箱')
    message = forms.CharField(widget=forms.Textarea, label='内容')
