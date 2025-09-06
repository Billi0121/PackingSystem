from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    kitchen = Group.objects.get(pk=2)
    livingroom = Group.objects.get(pk=3)
    bedroom = Group.objects.get(pk=4)
    context = {
        'kitchen': kitchen,
        'bedroom': bedroom,
        'livingroom': livingroom,
    }
    return render(request, 'packing/index.html', context)

def group(request, slug):
    group = Group.objects.get(name=slug)
    furniture = Furniture.objects.filter(Group=group)
    context = {
        'furniture': furniture,
    }
    return render(request, 'packing/group.html')