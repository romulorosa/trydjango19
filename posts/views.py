from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def post_list(request, context):
    #return HttpResponse("<h1>LIST</h1>")
    return render(request,"index.html", context)

def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")

def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")

def post_create(request):
    return HttpResponse("<h1>CREATE</h1>")

def post_detail(request):
    return HttpResponse("<h1>DETAIL</h1>")
