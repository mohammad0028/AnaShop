from django.utils.text import slugify
import math

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''
# from yourapp.utils import random_string_generator


import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# print(random_string_generator())

# print(random_string_generator(size=50))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


# ---------------------------------------------------------------------------------------------------

# this function returns data as a dictionary that its keys are number of carousel_numbers(int)
# and its values is a list(len=3) of images from Images model


def carousel_content_maker(pro_imgs):
    product_images = pro_imgs
    images_count = len(product_images)
    carousel_count = math.ceil(images_count / 3)
    data = {}
    for carousel_number in range(1, carousel_count + 1):
        for i in range(1, 4):
            if len(product_images) == 0:
                break
            elif i == 1:
                data[carousel_number] = [product_images.pop(0)]
            else:
                data[carousel_number].append(product_images.pop(0))
    return data


# ---------------------------------------------------------------------------------------------------

