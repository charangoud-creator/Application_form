from django import forms
from form.models import Registration

class ApplicationForm(forms.ModelForm):
    # Multiple selection fields
    TECHNOLOGY_CHOICES = [
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('HTML', 'HTML'),
        ('JavaScript', 'JavaScript'),
        ('C++', 'C++'),
    ]
    LOCATION_CHOICES = [
        ('Hyderabad', 'Hyderabad'),
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Remote', 'Remote'),
    ]

    technologies = forms.MultipleChoiceField(
        choices=TECHNOLOGY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    job_locations = forms.MultipleChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.SelectMultiple,
        required=False
    )

    willing_to_relocate = forms.BooleanField(required=False)

    class Meta:
        model = Registration
        fields = "__all__"
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            # 'remarks': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Additional information...'}),
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Full Address'}),
            'expected_salary': forms.NumberInput(attrs={'placeholder': 'Expected Salary'}),
            # 'notice_period': forms.TextInput(attrs={'placeholder': 'Notice Period'}),
            'resume': forms.ClearableFileInput(),
            # 'portfolio_url': forms.URLInput(attrs={'placeholder': 'Portfolio or Project URL'}),
        }
