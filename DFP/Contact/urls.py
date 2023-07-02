from django.urls import path
from Contact import views

urlpatterns = [
    path("", views.home_view, name="contact_home"),
    path("contact/", views.contact_view, name="contact_contact")
]