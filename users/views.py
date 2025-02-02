from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from sciences.models import Classes
from .models import Student


def home(request):
    form = Classes.objects.all()
    form1 = Student.objects.all()

    return render(request, 'home.html', {'form':form,'form1':form1})



def index(request):
    return render(request, 'index.html')



class TeacherView(TemplateView):
    template_name = "teacher.html"



class ClassesDetailView(DetailView):
    model = Classes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context



def classes_detail(request, id):
    sinf = get_object_or_404(Classes, id=id)
    form2 = sinf.oquvchi_sinf.all()
    print(form2)
    return render(request, 'detail.html', {'sinf': sinf, 'form2':form2})
