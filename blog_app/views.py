from django.shortcuts import render
from .models import Blog,Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializer import BlogSerialiizer,CategorySerializer
from rest_framework import status
# from rest_framework import request

class CategoryListView(APIView):
    def get(self,request):
        all_category  = Category.objects.all()
        serilizers = CategorySerializer(all_category,many=True)
        return Response(serilizers.data)

# Get get_all,post
class BlogListView(APIView):
    def get(self,request):
        all_blogs = Blog.objects.filter(is_public=True)
        BlogSerialiizer_obj = BlogSerialiizer(all_blogs,many=True)
        return Response(BlogSerialiizer_obj.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        blog_dat = request.data
        BlogSerialiizer_obj = BlogSerialiizer(data=blog_dat)
        if BlogSerialiizer_obj.is_valid():
            BlogSerialiizer_obj.save()
            return Response(BlogSerialiizer_obj.data,status=status.HTTP_201_CREATED)
        else:
            return Response(BlogSerialiizer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
        
# get,det,put
class BlogDetailsView(APIView):
    def get(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        BlogSerialiizer_obj = BlogSerialiizer(blog)
        return Response(BlogSerialiizer_obj.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        BlogSerialiizer_obj = BlogSerialiizer(instance=blog,data=request.data)
        if BlogSerialiizer_obj.is_valid():
            BlogSerialiizer_obj.save()
            return Response(BlogSerialiizer_obj.data,status=status.HTTP_201_CREATED)
        else:
            return Response(BlogSerialiizer_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        blog =Blog.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_200_OK)
    

from rest_framework import generics
class GenericBlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_public=True)
    serializer_class = BlogSerialiizer
class GenericBlogDetailsView(generics.RetrieveUpdateAPIView,generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiizer



# class GenericBlogDetailsView(generics.ListCreateAPIView):
#     serializer_class = BlogSerialiizer
#     def get_queryset(self):
#         pk = self.request.GET.get('pk')
#         if pk is not None:
#             return Blog.objects.filter(pk=pk)
#         return Blog.objects.all()



    






# @api_view(['GET'])
# def blog_details(request):
#     all_blogs = Blog.objects.all()
#     return Response(all_blogs)
