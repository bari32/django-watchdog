from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-created')[:10]
    answer = 1+2
    context = {"latest_post_list":latest_Post_list,'answer':answer}
    return render(request, 'index.html', {})
    
