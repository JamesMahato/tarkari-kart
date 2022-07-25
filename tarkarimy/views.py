from django.shortcuts import  render
from django.contrib.auth.decorators import login_required

from .models import *


# @login_required(login_url="login")
def index(request):
    return render(request,'index.html')

# @login_required(login_url="login")
def product(request):
    return render(request,'product.html')


