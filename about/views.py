from django.shortcuts import render

# Create your views here.

def view_page(request):
	return render(request,'about/index.html')
