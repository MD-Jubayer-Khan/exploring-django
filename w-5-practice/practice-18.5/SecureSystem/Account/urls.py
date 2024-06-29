from django.urls import path
from Account.views import ProfilePage, SignupPage, LoginPage, LogutPage, ChangePassWord, ChangePassWord2

urlpatterns = [
    path("profile/", ProfilePage, name="profile"),
    path("signUp/", SignupPage, name="signup"),
    path("login/", LoginPage, name="login"),
    path("logout/", LogutPage, name="logout"),
    path("Change-Password/", ChangePassWord, name="changepassword"),
    path("Change-Password2/", ChangePassWord2, name="changepassword2"),
]
