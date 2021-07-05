from django.shortcuts import render, redirect
from django.http import HttpResponse
from dashboard.models import Post, BlogComment 
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'dashboard/index.html',context)

def post(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {"post":post}
    return render(request, 'dashboard/post.html', context)

def comment(request):
    comments = BlogComment.objects.all()
    context = {"comments": comments}
    return render(request, 'dashboard/comments.html', context)   

def postComment(request,slug):
    if request.method=='POST':
        pass
    return redirect('/')