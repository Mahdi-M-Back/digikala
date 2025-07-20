from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , SetPasswordForm
from django import forms
from .models import Profile


class UpdatePasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'name': 'password',
        'placeholder': 'پسورد خود را وارد کنید'
        })
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'دوباره پسورد خود را وارد کنید'
        })
    )

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'})
        ,required=False
    )
    last_name = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
        ,required=False
    )
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
        ,required=False
    )
    username = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'})
        ,required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'})
    )
    username = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'})
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'پسورد خود را وارد کنید'
        })
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'دوباره پسورد خود را وارد کنید'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن'}),
        required=False
    )
    address1 = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس اول'}),
        required=False
    )
    address2 = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'}),
        required=False
    )
    city = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر '}),
        required=False
    )
    state = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' منطقه'}),
        required=False
    )
    zipcode = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی'}),
        required=False
    )
    country = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ("phone", "address1","address2","city","state","zipcode","country")