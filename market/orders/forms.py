from django import forms
from . models import Orders


class AddressForm(forms.ModelForm):
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-addres-data'}))
    second_name = forms.CharField(label="surname", widget=forms.TextInput(attrs={'class': 'form-addres-data'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-addres-data'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-addres-data'}))
    postal_code = forms.CharField(label='POstal code', widget=forms.TextInput(attrs={'class': 'form-addres-data'}))

    class Meta:
        model = Orders
        fields = ['first_name', 'second_name', 'city', 'address', 'postal_code']