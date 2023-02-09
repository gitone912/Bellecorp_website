from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("", views.home, name="homepage"),
    path("sub/", views.sub, name="subpage")
]