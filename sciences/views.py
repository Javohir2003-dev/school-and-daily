from django.shortcuts import render

from .models import Classes

def classes_view(request):
    form = Classes.objects.all()
    
    return render(request, 'classes.html', {'form':form})
