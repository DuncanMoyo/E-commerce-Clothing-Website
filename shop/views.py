from django.shortcuts import render
from shop.models import Item
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def category(request):
    product_list = Item.objects.all()
    paginator = Paginator(product_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'product_list': product_list,
        'page_request_var': page_request_var,
        'queryset': paginated_queryset,
    }

    return render(request, 'category.html', context)
