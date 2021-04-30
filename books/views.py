from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from books.forms import BookForm
from books.models import Books
# Create your views here.
def home(request):
	context={'book':"welcome to books app"}
	return render(request,'index.html',context=context)

def uploadbooks(request):
	form=BookForm()
	if request.method=="POST":
		form=BookForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return home(request)
		else:
			form=BookForm()

	context={'book':form}
	return render(request,'upload.html',context=context)

def booklist(request):
	book=Books.objects.all()
	# c=0
	# for i in book:
	# 	c=c+1

	# for i in range(c):
	# 	Books.objects.filter(id=i).delete()
	
	book=Books.objects.all()

	
	return render(request,'book_list.html',{'book':book})
	#(request,'booklist.html',{'book':"book"})





