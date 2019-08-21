from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Item, OrderItem, Order
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView, View, DetailView
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


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


def detail(request, slug):
    product = get_object_or_404(Item, slug=slug)
    context = {
        'product': product
    }

    return render(request, 'detail.html', context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'detail.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect('shop:basket.html')
        else:
            order.items.add(order_item)
            return redirect('shop:basket.html')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        return redirect('shop:basket.html')


class BasketView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'order': order,
            }
            return render(self.request, 'basket.html', context)
        except ObjectDoesNotExist:
            return redirect('/')























