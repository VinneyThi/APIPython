from django.urls import path
from .views import employee

urlpatterns = [
    path("",employee),
    path("<str:emailKey>",employee),
]