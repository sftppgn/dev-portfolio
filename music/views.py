from django.shortcuts import render
from django.http import HttpResponse
from . import write_func

# Create your views here.
#def closeFile(request):
#    write_func.closeFile()
def home(request):
    return render(request, 'music/music.html') 
def music(request):
    #testvar="test123"
    #content={
    #    'test':testvar
    #}
    #content=write_func.write("0en")

    context=write_func.getTempDict()
    filename=write_func.getTempFilename()
    return render(request, 'music/music.html', context) 

def closeFile(request):
    write_func.closeFile()
    context=write_func.getTempDict()
    return render(request, 'music/music.html', context) 

def writeFile(request):
    note=(str(request.POST.get('note')))
    write_func.write(note)
    context=write_func.getTempDict()
    return render(request, 'music/music.html', context) 