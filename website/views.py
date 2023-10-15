from django.shortcuts import render
from Products.models import ProductModel, Category, SubCategory


# Create your views here.
def Index(request):
    prod = ProductModel.objects.all()[:15]
    cat1 = Category.objects.get(id=1)
    cat2 = Category.objects.get(id=2)
    cat3 = Category.objects.get(id=7)
    cat4 = Category.objects.get(id=4)
    cat5 = Category.objects.get(id=5)
    cat6 = Category.objects.get(id=6)

    context = {'cat1': cat1,'cat2': cat2,'cat3': cat3, 'cat4': cat4, 'cat5': cat5, 'cat6': cat6, 'prod': prod}
    return render(request, 'website/index.html', context)


def ProductView(request, catname):
    catid = Category.objects.get(name=catname)
    print("Catid: ", catid)
    cat1 = Category.objects.get(id=1)
    cat2 = Category.objects.get(id=2)
    cat3 = Category.objects.get(id=7)
    cat4 = Category.objects.get(id=4)
    cat5 = Category.objects.get(id=5)
    cat6 = Category.objects.get(id=6)

    data = ProductModel.objects.filter(cat=catid)
    context = {'data': data, 'catid': catid, 'cat1': cat1,'cat2': cat2,'cat3': cat3, 'cat4': cat4, 'cat5': cat5, 'cat6': cat6}
    # context = {}
    return render(request, 'website/product.html', context)