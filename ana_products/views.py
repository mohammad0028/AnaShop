import itertools

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Product, Category, SubCategory, Images, Comment, Answer

from .utils import carousel_content_maker


# from django.urls import path

# Create your views here.


class CategoryPage(ListView):
    template_name = 'products/category_page.html'

    # every classBaseView should have a querySet or the model should be identified(as below):
    model = Category
    '''
        def get_queryset(self):
            qs = Category.objects.all()
            return qs
    '''

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(CategoryPage, self).get_context_data(*args, **kwargs)
        category_id = Category.objects.get(slug=self.kwargs['slug']).pk
        subcat_list = SubCategory.objects.filter(category=category_id)
        products_list = Product.objects.filter(category=category_id)
        data = {}
        for item in subcat_list:
            data[item] = []
        for product in products_list:
            data[product.subcategory].append(product)

        context['subcategory_list'] = data

        return context


def all_products_page(request):
    pro_list = Product.objects.get_active_products().order_by('id')
    # paginator
    paginator = Paginator(pro_list, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator
    }
    return render(request, 'products/products_list.html', context)

    # second way(below):
    # pro_list = Product.objects.get_active_products().order_by('id')
    # page_number = request.GET.get('page', 1)
    #
    # paginator = Paginator(pro_list, 3)
    # try:
    #     page_obj = paginator.page(page_number)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    # context = {
    #     'page_obj': page_obj,
    #     'paginator': paginator
    # }
    # return render(request, 'products/products_list.html', context)


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


# the second way to get data from url is like below:
# def product_detail(request, title=None,'*args, **kwargs):
#     product = get_object_or_404(Product, title=title)
def product_detail(request, *args, **kwargs):
    pure_title = kwargs['title'].replace('-', ' ')
    product = Product.objects.get_product_by_title(pure_title)
    product_id = product.id
    product_category = product.category
    suggested_products = Product.objects.filter(category=product_category)
    suggested_products = list(suggested_products)
    suggested_products.remove(product)
    suggested_products = my_grouper(3, suggested_products)
    product_images = list(Images.objects.filter(product=product_id))

    if product is None or not product.active:
        raise Http404('not found !')

    # product gallery carousel content get grouped by this function
    carousel_data = carousel_content_maker(product_images)

    # this function is down this page: this func saves the comment_form_data to comment model in database
    comment_reply_function(request, product_id)

    # getting comments of this product
    all_comments = product.comments.filter(active=True)

    context = {
        'product': product,
        'carousel_content': carousel_data,
        'suggested_products': suggested_products,
        'all_comments': all_comments
    }
    return render(request, 'products/product_detail.html', context)


# to group suggested products in product detail function
def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def comment_reply_function(request, product_id):
    if request.method == 'POST':
        the_name = request.POST.get('hidden_input_form_name')
        if the_name == 'comment_form':
            current_comment = Comment()
            current_comment.writer_name = request.POST.get('form_name')
            current_comment.body = request.POST.get('form_comment')
            current_comment.product = Product.objects.get(pk=product_id)
            current_comment.save()

        elif the_name == 'reply_form':
            current_reply = Answer()
            current_reply.writer_name = request.POST.get('user_name')
            current_reply.body = request.POST.get('reply')
            comment_id = request.POST.get('comment_id')
            current_reply.reply_to = Comment.objects.get(pk=comment_id)
            current_reply.save()

