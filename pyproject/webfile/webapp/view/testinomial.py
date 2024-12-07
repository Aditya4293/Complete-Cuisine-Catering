from .contact import Contact
from django.shortcuts import render
def testimonial(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'testimonial.html', {'contacts': contacts})
