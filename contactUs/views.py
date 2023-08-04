from django.shortcuts import redirect, render

from contactUs.models import ContactModel

# Create your views here.


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        subject = request.POST["subject"]
        email = request.POST["email"]
        message = request.POST["message"]
        ContactModel.objects.create(name=name,subject=subject,email=email,message=message)
        return redirect('/contact')
    else:
        return render(request, 'contact/contact.html')
