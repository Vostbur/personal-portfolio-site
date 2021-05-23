from django.shortcuts import render, get_object_or_404

from .models import Post


def blog(request):
    posts = Post.objects.order_by('-published_at')
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post.html', {'post': post})
