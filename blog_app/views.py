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
        serilizers = CategorySerializer(all_category,many=True,context={'request': request})
        return Response(serilizers.data,status=status.HTTP_200_OK)
class CategoryDetailsView(APIView):
    def get (self, request,pk):
        single_category =Category.objects.get(pk=pk)
        serializers = CategorySerializer(single_category,context={'request': request})
        return Response(serializers.data)
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
from rest_framework import mixins

class Mixnsviews(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiizer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# it is based on fields or lookup_field 
class Mixnsviews2(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiizer
    lookup_field = 'slug' # lookup_field

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# its based pk 
# class Mixnsviews2(mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   generics.GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerialiizer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class GenericBlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_public=True)
    serializer_class = BlogSerialiizer
    lookup_field ="blog_title"
class GenericBlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerialiizer
    lookup_field="slug"





    






# @api_view(['GET'])
# def blog_details(request):
#     all_blogs = Blog.objects.all()
#     return Response(all_blogs)
