from .models import Category


def navbar(request):
    category_list = Category.objects.all()

    nav_bar_category_list = {
        'category_list': category_list,
    }
    return nav_bar_category_list


def is_products_in_navbar_active(request):
    current_path = request.path
    my_list = ['product', 'category']
    for item in my_list:
        if item in current_path:
            result = {
                'is_active': True
            }
            return result
    result = {
        'is_active': False
    }
    return result


