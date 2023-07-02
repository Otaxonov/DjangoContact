from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from Contact.forms import ContactForm
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render(request, "contact/home.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "first_name": form.cleaned_data['first_name'],
                "last_name": form.cleaned_data['last_name'],
                "email": form.cleaned_data['email'],
                "message": form.cleaned_data['message']
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, "admin@example.com", ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found")

            messages.success(request, "Message Sent.")
            return redirect("contact_home")
        messages.error(request, "Error message not sent.")

    form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})
