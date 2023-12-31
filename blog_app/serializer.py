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
        exclude = ['id',]


# HyperlinkedModelSerializer

# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     category_name = serializers.CharField()
#     category = BlogSerialiizer(many=True,read_only=True)
    # category = serializers.StringRelatedField(many=True,read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # category = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="blog_details")

#     class Meta:
#         model = Category
#         fields = "__all__"


