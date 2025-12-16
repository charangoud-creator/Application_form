from django.db import models

class Registration(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    linkedin_url = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)  # New: Full address

    # Education Details
    highest_qualification = models.CharField(max_length=100, blank=True, null=True)
    university_or_college = models.CharField(max_length=100, blank=True, null=True)
    passing_year = models.PositiveIntegerField(blank=True, null=True)
    grade_or_percentage = models.CharField(max_length=10, blank=True, null=True)

    # Job Preferences
    TECHNOLOGY_CHOICES = [
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('HTML', 'HTML'),
        ('JavaScript', 'JavaScript'),
        ('C++', 'C++'),
    ]
    technologies = models.JSONField(default=list)  # Multiple techs selected

    LOCATION_CHOICES = [
        ('Hyderabad', 'Hyderabad'),
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Remote', 'Remote'),
    ]
    job_locations = models.JSONField(default=list)

    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Resume
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    # portfolio_url = models.URLField(blank=True, null=True)  # Optional portfolio link

    # Additional Information
    willing_to_relocate = models.BooleanField(default=False)

    # Submission timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.surname} ({self.email})"
