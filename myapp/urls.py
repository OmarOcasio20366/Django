from django.urls import path, include
from . import views
from .views import UserCreate, Logout
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProtectedView

urlpatterns = [
    
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('register/', UserCreate.as_view(), name='register'),
    # path('api/', include('myapp.urls')),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', Logout.as_view(), name='logout'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    
]

