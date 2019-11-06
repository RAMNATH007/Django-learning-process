from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

class Hello(View):
    def get(self,request):
        return render(request,'new.html')
hello=Hello.as_view()
class Hello1(View):
    def get(self,request):
        return render(request,'tech.html')
hello1=Hello1.as_view()

# Create your views here.
