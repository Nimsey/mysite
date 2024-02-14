"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as core_views
from django.contrib.auth import views as auth_views
from home.views import logout_view, signup_view, login_view, profile
from home import views

class LogoutView(auth_views.LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('', core_views.home, name='home'),  # Project homepage
    path("polls/", include('polls.urls')),
    path("admin/", admin.site.urls),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('User/<username>/', profile, name="profile" ),# Add this line
    path('accounts/login/', views.login_view, name='accountlogin'),
]