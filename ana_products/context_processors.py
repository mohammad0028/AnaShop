from .models import Category
from ana_account.models import MyCustomUserModel


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


# this function is for getting current user to display his/her avatar and username
# at shared/Header if he/she has logged in (search this_user to find its returning value(current user))
def get_current_user(request):
    if request.user.is_authenticated:
        curr_user_id = request.user.id
        curr_user = MyCustomUserModel.objects.filter(id=curr_user_id).first()
        curr_user = {
            'this_user': curr_user
        }
        return curr_user
    else:
        return {}
