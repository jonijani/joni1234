from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blog(request):
    joni = Blog.objects.all()
    #joni = Blog.objects.order_by('-date)[:2]to show only 2 or order by date

    return render(request, 'blog/all_blog.html',{'zak':joni})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/detail.html',{'blog':blog})
