from django.shortcuts import render

def conditions(request):
    d={'a':2000,'b':200,'c':5000}
    return render(request,'conditions.html',d)

def loop(request):
    d={'name':'PRAGNA❤️'}
    return render(request,'loop.html',d)