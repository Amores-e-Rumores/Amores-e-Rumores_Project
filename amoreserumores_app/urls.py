from django.conf.urls import url
from . import views


'''
urlpatterns = [
    url(r'^$', views.home_page, name='amoreserumores_app/home_page'),
    'django.views.generic.list_detail',
    url(r'^product/$', 'object_list', {'queryset': Product.objects.all()}),
    url(r'^product/(?P<slug>[-\W]+)/$', 'object_detail', {'queryset': Product.objects.all()})
]


urlpatterns = ('django.views.generic.list_detail', 
                url(r'^product/$', 'object_list', {'queryset': Product.objects.all()}),
                url(r'^product/(?P<slug>[-\W]+)/$', 'object_detail', {'queryset': Product.objects.all()}))
'''

'''urlpatterns = [
    url(r'^$', views.home_page, name='amoreserumores_app/home_page'),
    url(r'^product/$', views.ProductListView, name='amoreserumores_app/product_list'),
    url(r'^product/(?P<slug>[-\W]+)$', views.ProductDetailView, name='amoreserumores_app/product_detail'),
]
'''

urlpatterns = [
    url(r'^$', views.home_page, name='amoreserumores_app/home_page'),
    url(r'^produto/$', views.ProductList.as_view()),
    url(r'^produto/(?P<slug>[-\W]+)$', views.ProductDetail.as_view()),
]