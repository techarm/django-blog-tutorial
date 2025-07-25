from django.urls import path
from . import views

urlpatterns = [
    # FBV版をコメントアウトして、CBV版を有効化
    # path("", views.post_list, name="post_list"),
    # path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:post_id>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("category/<slug:slug>/", views.category_posts, name="category_posts"),
    path("search/", views.post_search, name="post_search"),
    path("about/", views.AboutView.as_view(), name="about"),
    path(
        "archive/<int:year>/<int:month>/",
        views.MonthArchiveView.as_view(),
        name="archive_month",
    ),
]
