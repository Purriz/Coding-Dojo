from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'index.html')

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    print("You created a blog post!")
    return redirect('/')

def show(request, number):
    return HttpResponse(f"This is a placeholder to display blog: {number}")

def edit(request, number):
    return HttpResponse(f"This is a placeholder to edit blog: {number}")

def destroy(request, number):
    return HttpResponse("This is a placeholder to delete blog: {number}")