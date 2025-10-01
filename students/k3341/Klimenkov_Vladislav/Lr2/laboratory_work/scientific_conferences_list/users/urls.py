from django.urls import path
from .views import (CustomSignUpView, 
                    CustomLoginView, 
                    CustomLogoutView, 
                    ConfirmLogoutView)

urlpatterns = [
    path('signup/', CustomSignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', ConfirmLogoutView.as_view(), name="logout"),
    path('logout/perform', CustomLoginView.as_view(), name='logout_perform'),
]
