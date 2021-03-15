from django.urls import path
from . import views

app_name = 'V_Maven'

urlpatterns = [
    path('', views.home, name='home'),
    path('store.html', views.store, name='store'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('signup.html', views.signup, name='signup'),
    path('signin.html', views.signin, name='signin'),
    path('signout.html', views.signout, name='signout'),
    path('delivered.html', views.delivered, name='delivered')
]