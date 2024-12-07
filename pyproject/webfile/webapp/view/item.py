from django.db import models
from .category import Category
from django.shortcuts import render
class Item(models.Model):
    i_id=models.AutoField(primary_key=True)
    i_name=models.CharField(max_length=100)
    description=models.TextField()
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    created_date=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return "%s %s %s" % (self.i_name, self.description, self.price)

def view_item(request):
    itm=Item.objects.all()
    context={'itm':itm}
    print(context)
    return render(request,'menu.html',{'itm':itm})

def selected_item(request,cat):
    citm = Item.objects.filter(cat_id=cat).all()
    context={'citm':citm}
    print(context)
    return render(request,'maincourse.html', {'citm': citm})

def sel_item(request,cat):
    sitm = Item.objects.filter(cat_id=cat).all()
    context={'sitm':sitm}
    print(context)
    return render(request,'drinks.html', {'sitm': sitm})

def sele_item(request,cat):
    ditm = Item.objects.filter(cat_id=cat).all()
    context={'ditm':ditm}
    print(context)
    return render(request,'dessert.html', {'ditm': ditm})
