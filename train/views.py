from django.shortcuts import render

# Create your views here.

def TrainVideo(request):
    if request.method == 'GET':
        return render(request,'video.html',locals())