from django.urls import path

from .views import home, blog, post, search

app_name = "blog"
urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("post/<int:id>/", post, name="post"),
    path("search/", search, name="search")
]
