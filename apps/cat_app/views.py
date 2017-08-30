from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..user_app.models import User
from .models import Cat, Like

# Create your views here.
def home(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {'user': user, 'cats': Cat.objects.all()}
        return render(request, 'cat_app/home.html', context)
    else:
        return redirect('user:index')

def add_cat(request):
    if 'user_id' in request.session:
        return render(request, 'cat_app/add_cat.html')
    else:
        return redirect('user:index')    

def post_cat(request):
    user = User.objects.get(id=request.session['user_id'])
    entry = Cat.objects.create_cat(request.POST, user)
    if not type(entry) is dict:
        return redirect('cat:home')
    else:
        if 'data' in entry:
            messages.add_message(request, messages.INFO, entry['data'], extra_tags='data')
        return redirect('cat:add_cat')

def add_like(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    user = User.objects.get(id=request.session['user_id'])
    Like.objects.create(cat=cat, user=user)
    return redirect('cat:home')

def delete_cat(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.delete()
    return redirect('cat:home')

def edit_cat_page(request, cat_id):
    if 'user_id' in request.session:
        context = {'cat': Cat.objects.get(id=cat_id)}
        return render(request, 'cat_app/cat.html', context)
    else:
        return redirect('user:index')

def edit_cat(request, cat_id):
    entry = Cat.objects.update_cat(request.POST, cat_id)
    if not type(entry) is dict:
        return redirect('cat:home')
    else:
        if 'data' in entry:
            messages.add_message(request, messages.INFO, entry['data'], extra_tags='data')
        return redirect(reverse('cat:edit', kwargs={'cat_id': cat_id}))

def show_cat(request, cat_id):
    if 'user_id' in request.session:
        context = {'cat': Cat.objects.get(id=cat_id)}
        return render(request, 'cat_app/show_cat.html', context)
    else:
        return redirect('user:index')

def log_out(request):
    request.session.flush()
    return redirect('user:index')
