from django.shortcuts import render


# Create your views here.
def index(request):
    '''get the latest 3 blogs'''
   
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html') 

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'service.html')



