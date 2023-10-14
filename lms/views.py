from django.shortcuts import redirect,render

def index(request):
    return render(request,'index.html')
def frontend(request):
    return render(request,'frontend.html')

def backend(request):
    return render(request,'backend.html')

def videob(request):
    return render(request,'premiere.html')

def blochchain(request):
    return render(request,'blockchain.html')