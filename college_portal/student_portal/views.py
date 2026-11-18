from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data={
        'name':"abc",
        'age':19,
        'department':"BCA"
    }
    marks=[100,98,97]
    return render(request,'home.html',{'data1':data,'marks1':marks})
    
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
