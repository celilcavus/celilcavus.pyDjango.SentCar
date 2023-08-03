from django.shortcuts import render

from blog.models import BlogModel

# Create your views here.
def blog(request):
    val = BlogModel.objects.all()
    blogVal = {
        'blog':val
    }
    return render(request,'blog/index.html',blogVal)

def details(request,detail_id):
    if detail_id > 0:
        findVal = BlogModel.objects.get(pk=detail_id)
        findBlogVal = {
            'findBlog':findVal
        }
        return render(request,'blog/details.html',findBlogVal)