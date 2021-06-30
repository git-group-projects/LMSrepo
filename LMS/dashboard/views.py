from django.shortcuts import render, redirect
from django.http import HttpResponse
from dashboard.models import Post, BlogComment 
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'dashboard/index.html',context)

def post(request,slug):
    # posts = Post.objects.all()
    # context = {"posts":posts}
    return render(request, 'dashboard/post.html')

def comment(request):
    comments = BlogComment.objects.all()
    context = {"comments": comments}
    return render(request, 'dashboard/comments.html', context)   

def postComment(request,slug):
    if request.method=='POST':
        pass
    return redirect('/')