from django import forms
from django.contrib.auth import password_validation
from business.validators import vpassword





class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'New Password'}),
                                                                validators=[vpassword])
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Verify New Password'}))

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user

    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'password_incorrect': ("Your old password was entered incorrectly. Please enter it again."),
    }
