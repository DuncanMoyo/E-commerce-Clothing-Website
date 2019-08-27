from django.shortcuts import render, get_object_or_404, reverse, redirect
from newsletter.models import Signup
from blog.models import Post, PostView, Author
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from blog.forms import CommentForm, PostForm
from shop.models import Item


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def get_category_count():
    queryset = Post \
        .objects \
        .values('category__title') \
        .annotate(Count('category__title'))
    return queryset


def index(request):
    latest = Post.objects.order_by('-timestamp')[:2]
    latest_items = Item.objects.order_by('timestamp')[:5]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'latest': latest,
        'latest_items': latest_items,
    }

    return render(request, 'index.html', context)


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


def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form,
        'title': title,
    }

    return render(request, 'post_create.html', context)

# TODO
#  load crispy tags and update requirements.txt
# TODO
#  have tags working just like the search logic
# TODO
#  get allauth for the login details, get pages from Github
# TODO
#  find a solution to js static issue
# TODO
#  getting replies for comments
#  https://stackoverflow.com/questions/44837733/how-to-make-add-replies-to-comments-in-django
# TODO
#  find a way to have breadcrumb working properly


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    title = 'Update'
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form,
        'title': title
    }

    return render(request, 'post_create.html', context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse('post-list'))
