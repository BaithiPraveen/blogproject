from django.shortcuts import render
from .models import Blog
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def blog_details(request):
    all_blogs = Blog.objects.all()
    return Response(all_blogs)
