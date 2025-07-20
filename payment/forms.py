from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
        required=True
    )
    shipping_email = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        required=True
    )
    shipping_address1 = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس اول'}),
        required=True
    )
    shipping_address2 = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'}),
        required=False
    )
    shipping_city = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر '}),
        required=True
    )
    shipping_state = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' منطقه'}),
        required=False
    )
    shipping_zipcode = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی'}),
        required=True
    )
    shipping_country = forms.CharField(
        label="",
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
        required=True
    )

    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_full_name',
            'shipping_email',
            'shipping_address1',
            'shipping_address2',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode',
            'shipping_country',
        ]

        exclude = ['user',]

