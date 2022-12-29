from django.shortcuts import render

def html1(request):
    return render(request,'htmlfile1.html')

def html2(request):
    return render(request,'htmlfile2.html')
