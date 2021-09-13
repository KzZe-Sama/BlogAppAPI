from django.urls import path,include
from .views import RegistrationView,UserRetrieveUpdateAPIView,GetAllUserAPIView
urlpatterns = [
    path('register',RegistrationView.as_view())
]
