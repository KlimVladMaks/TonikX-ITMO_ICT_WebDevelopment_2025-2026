from django.urls import path
from .views import (CustomSignUpView, 
                    CustomLoginView, 
                    CustomLogoutView, 
                    ConfirmLogoutView,
                    WelcomeView)

urlpatterns = [
    path('signup/', CustomSignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', ConfirmLogoutView.as_view(), name="logout"),
    path('logout/perform/', CustomLogoutView.as_view(), name='logout_perform'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
]
