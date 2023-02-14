from django.urls import path
from django.contrib.auth import views as auth_view
from .forms import *
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('aboutme/', aboutme, name='aboutme'),
    path('aboutweb/', aboutweb, name='aboutweb'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='authenticate/login.html',authentication_form=LoginForm),name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='home'),name='logout'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='authenticate/passwordchange.html', form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='authenticate/passwordchangedone.html'),name='passwordchangedone'),
    
]