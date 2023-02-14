from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
# Create your views here.




#******************** Front View ********************#
def home(request):
    return render(request, 'frontview/home.html')

def aboutme(request):
    data = AboutMe.objects.all()
    return render(request, 'frontview/aboutme.html',{'data':data})

def aboutweb(request):
    return render(request, 'frontview/aboutweb.html')

def contact(request):
    if request.method == 'POST':
        cap = CaptchaForm(request.POST)
        if cap.is_valid():
            form = ContactMeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('contact')
            else:
                return HttpResponseRedirect("Bad Request")
        else:
            return HttpResponseRedirect("Bad Request")
    else:
        form = ContactMeForm()
        cap = CaptchaForm()
        return render(request, 'frontview/contact.html', {'form':form, 'cap':cap})





#******************** Dashboard View ********************#

def dashboard(request):
    return render(request, 'dashboard/index.html')