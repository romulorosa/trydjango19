from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

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

def post_delete(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")

def post_update(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Updated")
            return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "submit_btn_text": "Update"
    }
    return render(request, "post_form.html", context)


def post_detail(request, post_id=None):
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
            messages.success(request, "Post created")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, "The form is not valid")

    context = {
        "form": form,
        "submit_btn_text": "Create"
    }
    return render(request, "post_form.html", context)
