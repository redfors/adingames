from django.shortcuts import render
from .models import Blog
from logpage.models import Profile

def blog(request):
    blog = Blog.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'blog/blog.html', {'blog': blog, 'typeuser': typeuser})
    else:
        return render(request, 'blog/blog.html', {'blog': blog})
