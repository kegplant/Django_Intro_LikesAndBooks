from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from models import *
# the index function is called when root is visited
def index(request):
    # Users.objects.create(first_name='Speros',last_name='',email='')
    # Users.objects.create(first_name='Song',last_name='',email='')
    # Users.objects.create(first_name='Julien',last_name='',email='')
    u1=Users.objects.first()
    u2=Users.objects.get(id=2)
    u3=Users.objects.get(id=3)
    # Books.objects.create(name='US history',desc='',uploader=u3) 
    # Books.objects.create(name='USSR history',desc='',uploader=u3) 
    users=Users.objects.all()
    books=Books.objects.all()
    b=[]
    for book in books:
        b.append(book)
    #users creating books
    # u1.uploads.add(b[0])
    # u1.uploads.add(b[2])
    # u1.likes.add(b[0])
    # u1.likes.add(b[len(b)-1])
    # u2.likes.add(b[0])
    # u2.likes.add(b[2])
    # books=u2.likes.all()
    # users=b[0].likers.all()
    # users=[b[0].uploader]
    users=b[2].likers.all()
    context={
        'users': users,
        'books': books
    }
    #return HttpResponse(response)
    return render(request,'likes_books/index.html',context)