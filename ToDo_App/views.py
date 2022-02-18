from django.contrib import messages
from django.shortcuts import render, redirect
from ToDo_App.models import Item


def add_form(request):
    if request.method == 'POST':
        item_name = request.POST.get('itemName')
        date_perform = request.POST.get('datePerform')

        if item_name != "" and date_perform != "":
            data = Item(
                item_name=item_name,
                date_perform=date_perform,
            )
            data.save()
            return redirect('home-page')

    return render(request, 'ToDo_App/form.html', context={})


def update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.item_name = request.POST.get('itemName')
        item.date_perform = request.POST.get('datePerform')

        item.save()
        return redirect('home-page')

    return render(request, 'ToDo_App/update.html',  context={'item': item})


def delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'ToDo_App/delete.html', context={'item': item})


def item_list(request):
    items_list = Item.objects.all()
    context = {'items_list': items_list}

    return render(request, 'ToDo_App/index.html', context)



