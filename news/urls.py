from django.urls import path
from .views import news_page, category, contact

urlpatterns = [
    path('', news_page, name='news_page'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    # path('single/', single, name='single'),

]