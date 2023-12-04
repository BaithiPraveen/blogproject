from django.urls import path,include
from .views import BlogListView,BlogDetailsView,GenericBlogListView,GenericBlogDetailsView

urlpatterns = [
   # cls based views
   path("class_blog_list/",BlogListView.as_view(),name="all_blog_list"),
   path("class_blog_details/<int:pk>/",BlogDetailsView.as_view(),name="blog_details"),

   #genricviews in listcreated view
   path("generic_views_blog_list/",GenericBlogListView.as_view(),name="generic_blog_details"),

   #genericview in RetrieveUpdateAPIView
   path("generic_views_blog_details/<int:pk>/",GenericBlogDetailsView.as_view(),name="generic_views_blog_details"),

]
