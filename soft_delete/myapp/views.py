from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def soft_del(request, pk):
    item = XYZ_Shop.everything.get(id=pk)
    item.soft_delete()
    item.save()
    return redirect("deleted_items")

def restore_data(request, pk):
    item = XYZ_Shop.everything.get(id=pk)
    item.restore()
    item.save()
    return redirect("home")

def permanent_delete(request, pk):
    item = XYZ_Shop.everything.get(id=pk)
    item.delete()
    return redirect("home")

def home(request):
    form = XYZ_Shop.objects.all()
    return render(request, 'home.html',{'form':form})

def deleted_items(request):
    form = XYZ_Shop.everything.filter(is_deleted=True)
    return render(request, 'deleted_items.html',{'form':form})