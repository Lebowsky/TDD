from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from lists.models import Item


def home_page(request):
    """ home page """

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/one-list-in-the-world')

    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
