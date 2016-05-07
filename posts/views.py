from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post
# Create your views here.
def post_list(request, context={}):
    #return HttpResponse("<h1>LIST</h1>")
    return render(request,"index.html", context)

def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")

def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")

def post_create(request):
    return HttpResponse("<h1>CREATE</h1>")

def post_detail(request, post_id):
    #instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=post_id)
    context = {
        "title": "Detail",
        "instance": instance,
    }
    return render(request,"post_detail.html", context)
