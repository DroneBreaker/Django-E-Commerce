from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store', views.store, name='store'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('signup.html', views.signup, name='signup'),
    path('signin.html', views.signin, name='signin'),
    path('signout.html', views.signout, name='signout')
]