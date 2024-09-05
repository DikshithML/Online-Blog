from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
def post_detail(request, slug):
 template_name = 'post_detail.html'
 post = get_object_or_404(Post, slug=slug)
 comments = post.comments.filter(active=True)
 new_comment = None
 # Comment posted
 if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)
 if comment_form.is_valid():
 # Create Comment object but don't save to database yet
    new_comment = comment_form.save(commit=False)