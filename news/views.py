from django.shortcuts import render


# Create your views here.
def news_page(request):
    return render(request, 'news/index.html')


def category(request):
    return render(request, 'news/category.html')


def contact(request):
    return render(request, 'news/contact.html')
