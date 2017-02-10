from django.db import models
from django.utils.timezone import datetime, now
# Create your models here.

class Catalog(models.Model):    #practical, base structure
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)


class Product(models.Model):    #basic set of fields that represent common properties
    category = models.ForeignKey('CatalogCategory', related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='product_photo', blank=True)
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=20)


class CatalogCategory(models.Model):    #Connects catalog to category
    catalog = models.ForeignKey('Catalog', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __unicode__(self):
        if self.parent:
            return u'%s: %s - %s' % (self.catalog.name, self.parent.name, self.name)
        return u'%s: %s' % (self.catalog.name, self.name)

    
class ProductDetail(models.Model):
    '''
    O "ProductDetail" Model representa informacao unica a um produto especifico.
    Esse eh um design generico que pode ser usado para extender a informacao 
    contida em "Product" Model com detalhes especificos extras.
    '''
    product = models.ForeignKey('Product', related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s - %s' % (self.product, self.attribute, self.value) 


class ProductAttribute(models.Model):
    '''
    O "ProductAttribute" Model representa uma classe de caracteristicas encontradas
    entre um grupo de produtos. Nao guarda dados de valores relacionados aos
    atributos, mas apenas descreve qual tipo de caracteristica do produto que
    estamos querendo capturar. Atributos possiveis incluem coisas como materiais,
    cores tamanhos, e mais.
    '''
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name
