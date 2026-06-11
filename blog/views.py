from django.shortcuts import render
from django.utils import timezone
from .models import Post # use . since both fviews and models are in the same directory

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) # request is everything we recieve from the user, 'blog...' is the template file, and {} is what were giving the template file