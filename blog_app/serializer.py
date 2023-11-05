from rest_framework import serializers 
from .models import Blog
class BlogSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


