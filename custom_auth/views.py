# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework import filters, generics

from custom_auth import models
from custom_auth.filters import UserFilter
# Create your views here.
from custom_auth.forms import SignUpForm
from custom_auth.serializers import UserSerializer


def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Signup successfully. Please login.')
            return redirect('home')
        else:
            print(form.errors)
            messages.add_message(
                request,
                messages.ERROR,
                'Error. Please ensure data is correct.')

    form = SignUpForm()
    kwargs = locals()
    return render(request, 'custom_auth/signup.html', kwargs)



def user_list(request):
    data = UserFilter(request.GET, queryset=models.User.objects.all())

    kwargs = locals()
    return render(request, 'custom_auth/filter.html', kwargs)


class UsersListView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = '__all__'
    ordering = ('id',)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'id', 'date_of_birth')
