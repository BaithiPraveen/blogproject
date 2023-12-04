from django.urls import path,include
from .views import BlogListView,BlogDetailsView

urlpatterns = [
   # cls based views
   path("class_blog_list/",BlogListView.as_view(),name="all_blog_list"),
   path("class_blog_details/<int:pk>/",BlogDetailsView.as_view(),name="blog_details"),
]
