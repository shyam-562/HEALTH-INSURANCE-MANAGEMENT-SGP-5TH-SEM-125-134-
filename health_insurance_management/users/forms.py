from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    
    last_name = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    
    mobile = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
    )

    address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Address'}),
    )

    birthdate = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'placeholder': 'Birth Date', 'type': 'date'})
    )

    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = ['first_name', 'last_name', 'mobile', 'address', 'birthdate', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Removing the help text for fields if needed
        self.fields['first_name'].help_text = None
        self.fields['last_name'].help_text = None
        self.fields['mobile'].help_text = None
        self.fields['address'].help_text = None
        self.fields['birthdate'].help_text = None

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        max_length=150,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    
    first_name = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    last_name = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    
    birthdate = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Birth Date', 'type': 'date'})
    )
    
    mobile = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'})
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email address'})
    )

    address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Address'}),
    )
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = ['username', 'first_name', 'last_name', 'birthdate', 'mobile', 'email', 'address', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user