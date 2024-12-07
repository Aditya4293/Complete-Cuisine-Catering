from django.db import models
from django.contrib.auth.models import User
from .events import Events
from .package import Package
from django.shortcuts import render, redirect
class Booking(models.Model):
    Book_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Events,on_delete=models.CASCADE,null=True)
    pack=models.ForeignKey(Package,on_delete=models.CASCADE,null=True)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    book_date = models.DateTimeField(auto_now_add=False, blank=False)
    address=models.CharField(max_length=250)
    note=models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)


    def __str__(self):
        return "%s %s %s %s" % (self.Book_id,self.pack, self.book_date,self.created_date)

def booking(request):
    event = Events.objects.all()
    pack = Package.objects.all()
    bookings = Booking.objects.all()
    context = {'event': event, 'pack': pack, 'bookings': bookings}
    #print(context)
    if request.method == 'POST':
        if request.user.is_authenticated:

            user = request.user
            eve = request.POST.get('event')
            pac = request.POST.get('pack')
            event_instance = Events.objects.get(pk=eve)
            pack_instance = Package.objects.get(pk=pac)
            print(event_instance, pack_instance)
            ck = request.POST['contact_number']
            zem = request.POST['email']
            bd = request.POST['book_date']
            add = request.POST['address']
            ne = request.POST['note']
            if event_instance and pack_instance:
                new_booking = Booking.objects.create(user=user, event=event_instance, pack=pack_instance, contact_number=ck, email=zem, book_date=bd, address=add, note=ne)
                new_booking.save()
                return redirect('profile')
    return render(request,'book.html',{'event':event,'pack':pack,'bookings':bookings})