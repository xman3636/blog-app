from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post # use . since both fviews and models are in the same directory

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) # request is everything we recieve from the user, 'blog...' is the template file, and {} is what were giving the template file

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # automatically handles the case in where a non existant post is requested
    return render(request, 'blog/post_detail.html', {'post': post})