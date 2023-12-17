
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following/<str:profilename>/", views.following, name="following"),

    ## API
    path("listing", views.listing, name="listing"),
    path("profile/<str:profilename>/", views.profile, name="profile"),
    path("profile/<str:profilename>/follow", views.follow, name="follow")

    
]
