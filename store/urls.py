from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_user, name="logout"),
    path("product/<int:pk>", views.product_page, name="product"),
]
