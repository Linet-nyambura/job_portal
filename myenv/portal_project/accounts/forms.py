from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, JobSeekerProfile, EmployerProfile, Company

class EmployeeRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_job_seeker = True
        if commit:
            user.save()
            JobSeekerProfile.objects.create(user=user)
        return user

class EmployerRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    company_location = forms.CharField(max_length=100)
    company_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
            company = Company.objects.create(
                name=self.cleaned_data.get('company_name'),
                location=self.cleaned_data.get('company_location'),
                description=self.cleaned_data.get('company_description')
            )
            EmployerProfile.objects.create(user=user, company=company)
        return user

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def get_user(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.MultipleObjectsReturned:
            users = User.objects.filter(email=email)
            user = users.first()
        except User.DoesNotExist:
            user = None
        return user

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = self.get_user()
        if user is None or not user.check_password(password):
            raise forms.ValidationError("Invalid login credentials")
        return cleaned_data

class YourProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    id_number = forms.CharField(max_length=20)
    passport_picture = forms.ImageField()
