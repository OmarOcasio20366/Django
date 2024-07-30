from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_NAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
# Implementing Registration View
class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout View
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {'message': 'This is a protected route. You are seeing this because you are authenticated'}
        return Response(content)