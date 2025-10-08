from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (CustomSignUpView, 
                    CustomLoginView, 
                    ConfirmLogoutView,
                    WelcomeView,
                    UserDetailView)


urlpatterns = [
    path('signup/', CustomSignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', ConfirmLogoutView.as_view(), name="logout"),
    path('logout/perform/', LogoutView.as_view(), name='logout_perform'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
