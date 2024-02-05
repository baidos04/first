from django.urls import path
from .views import (
    UserList, UserCreate, UserUpdate, UserDetail, UserDelete,
    CategoryList, CategoryCreate, CategoryUpdate, CategoryDetail, CategoryDelete,
    AdList, AdCreate, AdUpdate, AdDetail, AdDelete,
    ContactList, ContactCreate, ContactUpdate, ContactDetail, ContactDelete, login_view,
)

urlpatterns = [
    # User URLs
    path('users/', UserList.as_view(), name='user-list'),
    path('users/create/', UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdate.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),

    # Category URLs
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/create/', CategoryCreate.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdate.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDelete.as_view(), name='category-delete'),

    # Ad URLs
    path('ads/', AdList.as_view(), name='ad-list'),
    path('ads/create/', AdCreate.as_view(), name='ad-create'),
    path('ads/<int:pk>/', AdDetail.as_view(), name='ad-detail'),
    path('ads/<int:pk>/update/', AdUpdate.as_view(), name='ad-update'),
    path('ads/<int:pk>/delete/', AdDelete.as_view(), name='ad-delete'),

    # Contact URLs
    path('contacts/', ContactList.as_view(), name='contact-list'),
    path('contacts/create/', ContactCreate.as_view(), name='contact-create'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path('contacts/<int:pk>/update/', ContactUpdate.as_view(), name='contact-update'),
    path('contacts/<int:pk>/delete/', ContactDelete.as_view(), name='contact-delete'),

    path('login/', login_view, name='login-login')
]

