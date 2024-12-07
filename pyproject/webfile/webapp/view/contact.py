from django.db import models
from django.shortcuts import render, redirect
class Contact(models.Model):
    s_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    note=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return "%s %s %s" % (self.s_id,self.name, self.note)
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        note = request.POST['note']
        new_contact = Contact(name=name, note=note)
        new_contact.save()
        return render(request, 'index.html')
    return render(request,'contact.html')