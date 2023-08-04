from django.shortcuts import render

from blog.models import BlogModel

# Create your views here.
def about(request):
    adminval = BlogModel.objects.last()
    about = {
        'ab':adminval
    }
    return render(request,'about/about.html',about)