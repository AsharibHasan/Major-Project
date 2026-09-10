from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
                     path("UserLogin.html", views.UserLogin, name="UserLogin"),	      
                     path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
                     path("SignupAction", views.SignupAction, name="SignupAction"),
                     path("Register.html", views.Register, name="Register"),       
		     path("ForgotPassword.html", views.ForgotPassword, name="ForgotPassword"),	      
                     path("ForgotPasswordAction", views.ForgotPasswordAction, name="ForgotPasswordAction"),
]
