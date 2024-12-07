from .import views
from .view import customer,contact,item,package,booking,testinomial
from django.conf import settings
from django.conf.urls.static import static
from .views import index

from django.urls import path

urlpatterns = [
    path('event/',package.view_event,name='view_event'),
    path('book/',booking.booking,name='booking'),

    path('',views.index),
    #path('404/',views.four),
    path('about/',views.about),
    path('blog/',views.blog),
    path('contact/',contact.contact),
    path('Signup/',customer.Signup),
    #path('login/',customer.login),

    #path('profile/',views.profile),
    path('menu/',item.view_item,name='view_item'),
    path('service/',views.service),
    path('team/',views.team),
    path('testimonial/',testinomial.testimonial),
    path('selected_item/<int:cat>',item.selected_item,name='selected_item'),
    path('sel_item/<int:cat>', item.sel_item, name='sel_item'),
    path('sele_item/<int:cat>', item.sele_item, name='sele_item'),
    path('login/',customer.login, name='login'),
    path('profile/',customer.profile, name='profile'),
    path('logout/',customer.logout_view, name='logout'),
    path('', index, name='index'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)