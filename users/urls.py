from django.urls import path
from users import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("register",user_view.register,name="register"),
    path("login",auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path("logout",auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
    path("profile",user_view.profile,name="profile"),
    # path("passwor-reset", auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="passwordreset"),
    # path("passwor-reset/done", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    # path("passwor-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
    #      name="password_reset_confirm")

]




