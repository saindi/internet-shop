from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from user.models import UserModel


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )


class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        )
    )

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("Користувач із таким ім'ям вже є")
        except UserModel.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            UserModel.objects.get(email=email)
            raise ValidationError("Користувач із такою поштою вже є")
        except UserModel.DoesNotExist:
            return email

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise ValidationError("Паролі не однакові")

    def save(self, commit=True):
        UserModel.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"]
        )


class EditUserDataForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'img']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control", "required": True}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "required": True}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }

    def clean_username(self):
        username = self.cleaned_data["username"]

        if self.instance.username == username:
            return username

        try:
            UserModel.objects.get(username=username)
            raise ValidationError("Користувач із таким ім'ям вже є")
        except UserModel.DoesNotExist:
            return username


class EditUserPasswordForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        )
    )

    class Meta:
        model = UserModel
        fields = ['password', 'password2']
        widgets = {
            'password': forms.PasswordInput(attrs={"class": "form-control", "placeholder": "New password"}),
        }

    def clean(self):
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]

        if password != password2:
            raise ValidationError("Паролі не однакові")

    def save(self, **kwargs):
        self.instance.set_password(self.cleaned_data["password"])
        self.instance.save()
