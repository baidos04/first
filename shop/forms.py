from django import forms


class CustomLoginForm(forms.Form):
    ACCOUNT_CHOICES = [
        ('google', 'Google Account'),
        ('facebook', 'Facebook Account'),
        ('apple', 'Apple'),
    ]

    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, widget=forms.RadioSelect)
    name = forms.CharField(max_length=255, label='Your Name')
    age = forms.IntegerField(label='Your Age')
