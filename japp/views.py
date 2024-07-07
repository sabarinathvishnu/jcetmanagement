from django.shortcuts import render,redirect
from japp.models import bookdb

# Create your views here.
def mainpage_book(request):
    return render(request,"book.html")
def save_book(request):
    if request.method == "POST":
        a = request.POST.get('bname')
        b = request.POST.get('aname')
        c = request.POST.get('price')
        obj = bookdb(bookname=a,authorname=b,price=c)
        obj.save()
        return redirect(mainpage_book)
def display_book(request):
    data = bookdb.objects.all()
    return render(request,"displaybook.html",{'data':data})
def edit_book(request,bookid):
    data = bookdb.objects.get(id=bookid)
    return render(request,"editbook.html",{'data':data})
def update_book(request,bookid):
    if request.method == "POST":
        a = request.POST.get('bname')
        b = request.POST.get('aname')
        c = request.POST.get('price')
        bookdb.objects.filter(id=bookid).update(bookname=a,authorname=b,price=c)
        return redirect(display_book)
def delete_book(request,bookid):
    data = bookdb.objects.filter(id=bookid)
    data.delete()
    return redirect(display_book)


