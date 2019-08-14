from django.shortcuts import render
from newsletter.models import Signup
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count


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


def post(request):
    return render(request, 'post.html', {})