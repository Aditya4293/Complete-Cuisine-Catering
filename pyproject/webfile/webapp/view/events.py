from django.db import models
from django.shortcuts import render

class Events(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=100)
    image = models.ImageField()
    created_date=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return "%s %s %s %s" % (self.event_id,self.event_name,self.image , self.created_date)

# def view_event(request):
#     event=Events.objects.all()
#     pack=Package.objects.all()
#     context={'event':event,'pack':pack}
#     print(context)
#     return render(request,'event.html',{'event':event,'pack':pack})