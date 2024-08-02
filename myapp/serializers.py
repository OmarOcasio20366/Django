from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User
from .models import UploadedFile
from .models import MyModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'
        
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        # fields = 'created'
