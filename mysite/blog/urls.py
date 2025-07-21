from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("category/<slug:slug>/", views.category_posts, name="category_posts"),
    path("search/", views.post_search, name="post_search"),
]
