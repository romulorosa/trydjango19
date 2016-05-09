from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Post
from .forms import PostForm

def post_list(request):
    #return HttpResponse("<h1>LIST</h1>")
    object_list = get_list_or_404(Post)
    context = {
        "title": "Post list",
        "object_list": object_list,
    }
    return render(request,"index.html", context)

def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")

def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")

# def post_create(request):
#     return HttpResponse("<h1>CREATE</h1>")

def post_detail(request, post_id=1):
    #instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=post_id)
    context = {
        "title": "Detail",
        "instance": instance,
    }
    return render(request,"post_detail.html", context)

def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)
