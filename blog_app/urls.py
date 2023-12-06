from django.urls import path,include
# from .views import BlogListView,BlogDetailsView,CategoryListView,CategoryDetailsView,GenericBlogListView,GenericBlogDetailsView,Mixnsviews,Mixnsviews2
from .views import BlogViewSet#BlogListView,BlogDetailsView,CategoryListView,CategoryDetailsView,GenericBlogListView,GenericBlogDetailsView,Mixnsviews,Mixnsviews2
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs',BlogViewSet,basename="blogs")

urlpatterns = [
    path("",include(router.urls))
   # cls based views
   # path("class_blog_list/",BlogListView.as_view(),name="all_blog_list"),
   # path("class_blog_details/<int:pk>/",BlogDetailsView.as_view(),name="blog_details"),
   # path("class_category_list_view/",CategoryListView.as_view(),name="class_category_list_view"),
   # path("category/<int:pk>/", CategoryDetailsView.as_view(), name="category-detail"),


   # #genricviews in listcreated view
   # path("generic_views_blog_list/",GenericBlogListView.as_view(),name="generic_blog_details"),

   # #genericview in RetrieveUpdateDestroyAPIView
   # path("generic_views_blog_details/<str:slug>/",GenericBlogDetailsView.as_view(),name="generic_views_blog_details"),

   # #Mixnsviews create,get_list
   # path("mixin_views_blog_list/",Mixnsviews.as_view(),name="mixin_views_blog_list"),

   # # Mixnsviews get,update,delete 1 record
   # # path("mixin_views2_blog_list/<int:pk>",Mixnsviews2.as_view(),name="mixin_views_blog_list"),
   # path("mixin_views2_blog_list/<str:slug>",Mixnsviews2.as_view(),name="mixin_views_blog_list"),


]
