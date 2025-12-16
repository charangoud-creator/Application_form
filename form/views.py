from django.shortcuts import render,redirect
from .form import ApplicationForm

# Create your views here.

# Registration form view
def register(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)

            # Handle checkbox (technologies) and multi-select (job_locations)
            instance.technologies = request.POST.getlist("technologies")
            instance.job_locations = request.POST.getlist("job_locations")

            instance.save()
            return redirect("registration_success")  # URL name
    else:
        form = ApplicationForm()

    return render(request, "registration_form.html", {"form": form})

# Success page view
def registration_success(request):
    return render(request, "registration_success.html")

# About page view
def about(request):
    return render(request, 'about.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')