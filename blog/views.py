from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    context = {
        'page_name': 'blog-home'
    }
    return render(request, 'blog/home.html', context)



# class PostCreateView(CreateView):
#     model = Post
#     fields = ['title', 'comment', 'age']

@login_required
def blog(request):
    post = Post.objects.all()
    if request.method == "POST":
        context = {
            'post': post,
            'show_form': False,
            'message': 'You added a new post!',
            'page_name': 'blog'
        }
        try:
            new_post = Post.objects.create(
                author = User.objects.get('username'),
                age = User.objects.get('age'),
                title = request.POST.get('title'),
                comment = request.POST.get('comment'),
                date_posted = datetime.date.today()
            )
            new_post.save()
        except:
            context['message'] = 'There was an error adding your comment. Try again'
        return render(request, 'blog/blog.html', context)    
    else:
        context = {
            'post': post,
            'show_form': True,
            'page_name': 'blog',
        }
    return render(request, 'blog/blog.html', context)
