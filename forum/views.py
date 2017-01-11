from django.shortcuts import render

# Create your views here.

def article_list(request):
    if request.method == 'GET':
        return render(request,'article_list.html',locals())

