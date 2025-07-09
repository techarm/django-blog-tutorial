from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_world, name="hello_world"),
    path("time/", views.current_time, name="current_time"),
    path("info/", views.show_request_info, name="request_info"),
    path("template/", views.hello_template, name="hello_template"),
    path("greeting/", views.greeting, name="greeting"),
    path("greet/<str:username>/", views.greet_user, name="greet_user"),
]
