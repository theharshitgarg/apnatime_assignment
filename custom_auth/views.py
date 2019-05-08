# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .forms import SignUpForm


def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Signup successfully. Please login.')
            redirect('home')
        else:
            print(form.errors)
            messages.add_message(
                request,
                messages.ERROR,
                'Error. Please ensure data is correct.')

    form = SignUpForm()
    kwargs = locals()
    return render(request, 'custom_auth/signup.html', kwargs)
