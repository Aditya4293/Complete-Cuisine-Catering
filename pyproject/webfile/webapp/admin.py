from django.contrib import admin
from .view.customer import Customer
from .view.contact import Contact
from .view.category import Category
from .view.item import Item
from .view.events import Events
from .view.package import Package,Package1
from .view.booking import Booking
# Register your models here.

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Events)
admin.site.register(Package)
admin.site.register(Package1)
admin.site.register(Booking)