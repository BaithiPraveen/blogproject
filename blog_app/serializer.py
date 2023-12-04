from rest_framework import serializers 
from .models import Blog,Category
class BlogSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerialiizer(many=True,read_only=True)
    class Meta:
        model = Category
        exclude = ['id']

