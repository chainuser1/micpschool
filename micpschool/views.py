__author__ = 'Pareng Je'
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def master(request):
    return redirect('exams:home')
