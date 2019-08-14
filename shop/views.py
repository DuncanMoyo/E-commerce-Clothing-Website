from django.shortcuts import render, get_object_or_404, reverse, redirect
from newsletter.models import Signup
from blog.models import Post, PostView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from blog.forms import CommentForm


def get_category_count():
    queryset = Post \
        .objects \
        .values('category__title') \
        .annotate(Count('category__title'))
    return queryset


def index(request):

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    return render(request, 'index.html', {})


def blog(request):
    category_count = get_category_count()
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count': category_count,
    }

    return render(request, 'blog.html', context)


def post(request, id):
    category_count = get_category_count()
    post = get_object_or_404(Post, id=id)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={'id': post.id}))

    context = {
        'category_count': category_count,
        'post': post,
        'form': form,
    }
    return render(request, 'post.html', context)

