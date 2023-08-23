from django.shortcuts import render

from web.models import Category, Order, Size, Product

def index(request):

    categories = Category.objects.all().order_by('-id')[:4]

    products = Product.objects.all()

    context = {
        "title": "Decom Home Page",
        "categories": categories,
        "products": products,

        
    }
    return render(request, 'web/index.html', context=context )



def category(request,id):

    category = Category.objects.get(id=id)

    categories = Category.objects.all().order_by('-id')[:4]

    products = Product.objects.filter(category=category)

    context = {
        "title": "Decom Category Page",
        "categories": categories,
        "products": products,

        
    }
    return render(request, 'web/category.html', context=context )



def product(request,id):

    product = Product.objects.get(id=id)


    context = {
        "title": "Decom Category Page",
        "product": product,

        
    }
    return render(request, 'web/product.html', context=context )


def buynow(request,id):

    product = Product.objects.get(id=id)

    if request.method == 'POST':
        pass

    else:
        context = {
        "title": "Decom Category Page",
        "product": product,

        
    }

    
    return render(request, 'web/buynow.html', context=context )


