from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'index.html')

def cooperation(request):
    return render(request, 'cooperation.html')

def farakhan(request):
    return render(request, 'farakhan.html')