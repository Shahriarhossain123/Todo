from django.shortcuts import render, redirect
from .models import TodoListItem


#
# Create your views here.

def home(r):
    if r.method == 'POST':
        title = r.POST['title']
        status = False
        if not status:
            print(False)
        else:
            status = False

        user = TodoListItem.objects.create(title=title, status=status)
        user.save()

    pro = TodoListItem.objects.all()
    return render(r, 'index.html', locals())


def itemSave(r):
    if r.method == 'POST':
        title = r.POST['title']

        user = TodoListItem.objects.create(title=title)
        user.save()

    return render(r, 'index.html', locals())


def update(r, id):
    pro = TodoListItem.objects.get(id=id)
    if r.method == 'POST':
        title = r.POST['title']
        status = r.POST['status']

        pro.title = title
        pro.status = status
        pro.save()

    return render(r, 'index.html', locals())


def delete(r, id):
    de = TodoListItem.objects.get(id=id)
    de.delete()
    return redirect('home')

# Create your views here.
