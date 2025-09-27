from django.urls import path
from .views import CustomSignUpView, CustomLoginView

urlpatterns = [
    path('signup/', CustomSignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name="login"),
]
