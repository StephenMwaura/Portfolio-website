from django.shortcuts import render
from django.contrib import messages
from .models import Project , Profile
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    my_projects = Project.objects.filter(featured = True)
    context = {"my_projects":my_projects}
    return render(request, "portfolio/home.html", context)


def project_list(request):
    projects = Project.objects.all()
    context = {"projects" : projects}
    return render(request, "portfolio/projects.html", context)


def project_detail(request , pk):
    project = get_object_or_404(Project , pk = pk)
    context = {"project" : project}
    return render(request,"portfolio/project_detail.html", context)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thanks ,  Your message has been sent.")
            return redirect("portfolio:contact")
    else:
        form = ContactForm()
    
    context = {"form" : form}
    return render(request, "portfolio/contacts.html", context)



def about(request):
    profile = Profile.objects.first()
    context = {"profile" : profile}
    return render(request , "portfolio/about.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            send_mail(
                subject=f"New portfolio contact from {contact_message.name}",
                message=contact_message.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True,
            )

            messages.success(request, "Thanks! Your message has been sent.")
            return redirect("portfolio:contact")
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "portfolio/contacts.html", context)