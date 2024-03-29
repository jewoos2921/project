from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "account"
urlpatterns = [

    path("login/", LoginView.as_view(template_name="acc/login.html"), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("create/", AccountCreateView.as_view(), name='create'),
    path("detail/<int:pk>", AccountDetailView.as_view(), name='detail'),
    path("update/<int:pk>", AccountUpdateView.as_view(), name='update'),
    path("delete/<int:pk>", AccountDeleteView.as_view(), name='delete'),
]
