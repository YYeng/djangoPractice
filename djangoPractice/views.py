from django.shortcuts import render

from ToDo_App.models import Item


def item_list(request):
    items_list = Item.objects.all()
    context = {'items_list': items_list}

    return render(request, 'index.html', context)
