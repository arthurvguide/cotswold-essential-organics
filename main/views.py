from django.shortcuts import render
from django.views import View

# Create your views here.
def get_base(request):
    return render(request,'base.html')

def get_home(request):
    return render(request,'home/index.html')