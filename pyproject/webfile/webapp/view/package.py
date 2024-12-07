from django.db import models
from .events import Events
from .item import Item

from django.shortcuts import render
from multiselectfield import MultiSelectField

class Package(models.Model):
    #item=Item.objects.get(i_name=i_name)
    pack_id=models.AutoField(primary_key=True)
    pack_name=models.CharField(max_length=100)
    event=models.ForeignKey(Events,on_delete=models.CASCADE)
    image=models.ImageField()
    price=models.DecimalField(max_digits=9,decimal_places=2)
    no_of_person=models.IntegerField()
    items=models.ForeignKey(Item,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return "%s" % (self.pack_name)

class Package1(models.Model):
    #item=Item.objects.get(i_name=i_name)
    pack_id=models.AutoField(primary_key=True)
    pack_name=models.CharField(max_length=100)
    items=models.CharField(max_length=100)
    def __str__(self):
        return "%s %s %s" % (self.pack_id,self.pack_name, self.items)
def view_event(request):
    event=Events.objects.all()
    pack=Package.objects.all()

    context={'event':event,'pack':pack}
    print(context)
    return render(request,'event.html',{'event':event,'pack':pack})



# def book_event(request):
#      event=Events.objects.all()
#      pack=Package.objects.all()
#      context={'event':event,'pack':pack}
#      print(context)
#      return render(request,'book.html',{'event':event,'pack':pack})


# def view_package(request):
#     pack=Package.objects.all()
#     context={'pack':pack}
#     print(context)
#     return render(request,'event.html',{'pack':pack})