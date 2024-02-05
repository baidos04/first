from django.shortcuts import render
from .forms import CustomLoginForm

from django.views import generic
from rest_framework import generics
from .models import User, Category, Ad, Contact
from .serializers import UserSerializer, CategorySerializer, AdSerializer, ContactSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdList(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreate(generics.CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdate(generics.UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDetail(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDelete(generics.DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdate(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            account_type = form.cleaned_data['account_type']
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']

    else:
        form = CustomLoginForm()

    return render(request, 'shop/login.html', {'form': form})
