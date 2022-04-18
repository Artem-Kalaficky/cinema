from django.shortcuts import render

def cms(request):
    return render(request, 'cms/layout/base.html')
