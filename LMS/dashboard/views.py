from django.shortcuts import render, redirect
from django.http import HttpResponse
from dashboard.models import Post, BlogComment 
# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def post(request, slug):
    return render(request, 'dashboard/post.html')
    # return HttpResponse(f'Hello, this is {slug}')

def comment(request):
    return render(request, 'dashboard/comments.html')   

def postComment(request,slug):
    if request.method=='POST':
        pass
    return redirect('/')