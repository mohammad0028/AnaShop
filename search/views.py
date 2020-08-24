from django.shortcuts import render
from django.views.generic import ListView
from ana_products.models import Product


# Create your views here.


class SearchProductsView(ListView):
    template_name = 'search_products.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')

        if query is None or len(query) == 0:
            return Product.objects.get_active_products()
        elif query is not None:
            return Product.objects.search(query)
        else:
            return Product.objects.get_active_products()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(SearchProductsView, self).get_context_data(*args, **kwargs)
        # context['active_pro_list'] = Product.objects.get_active_products()
        for key, value in context.items():
            print(key, value)
        return context
