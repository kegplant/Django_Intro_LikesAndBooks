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
    print b


    context={
        'users': users,
        'books': books
    }
    #return HttpResponse(response)
    return render(request,'likes_books/index.html',context)