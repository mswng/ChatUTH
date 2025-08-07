from django.shortcuts import render

# Create your views here.


def TrangChu(request):
    return render(request, 'index.html')