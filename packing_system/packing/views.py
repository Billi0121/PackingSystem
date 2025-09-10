from django.shortcuts import render
from .models import Group, Furniture

# Create your views here.
def index(request):
    kitchen = Group.objects.get(pk=3)
    livingroom = Group.objects.get(pk=2)
    bedroom = Group.objects.get(pk=1)
    context = {
        'kitchen': kitchen,
        'bedroom': bedroom,
        'livingroom': livingroom,
    }
    return render(request, 'packing/index.html', context)

def group(request, slug):
    group = Group.objects.get(name=slug)
    furnitures = Furniture.objects.filter(Group=group)
    context = {
        'furnitures': furnitures,
        'group': group
    }
    return render(request, 'packing/group.html', context)