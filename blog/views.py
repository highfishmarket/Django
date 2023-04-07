from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostList(ListView):
    model = Post
    # view 연결 1번 방법
    # template_name = 'blog/index.html'
    # 2번 방법 파일 이름을 ~~~_list.html

# FBV
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )