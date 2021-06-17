from typing import List
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import FormView
from .models import Driver
from .serializer import DriverSerializer
from rest_framework import generics

#form stuff:
from django.shortcuts import render
from .forms import WorkForm, RawWorkForm

def work_form_view(request):
    # form = WorkForm(request.POST or None)
    form = RawWorkForm()
    if request.method == 'POST':
        form = RawWorkForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "work_hours.html", context)


# Create your views here.

class HomePageView(ListView):
    template_name='home.html'
    model = Driver

class DriverDetailView(DetailView):
    template_name='details.html'
    model = Driver

class DriverCreateView(CreateView):
    template_name='create.html'
    model = Driver
    fields = ['author', 'work_clock', 'drive_clock']

# Working kinda...
class DriverUpdateView(FormView):
    template_name='update.html'
    model = Driver.objects.get()
    print(f'{model.work_clock} work clock is 1')
    form_class = RawWorkForm
    success_url = '/'

    def form_valid(self, form):
        # print(form.cleaned_data['work'])
        work = form.cleaned_data['work']
        # print(type(work))
        # print(type(self.model.work_clock))
        if self.model.work_clock > work:
            self.model.work_clock -= work
            print(f'result is: {self.model.work_clock}')
        else:
            print('In Violation!')
            self.model.work_clock = 0
            self.model.status = 'In Violation.'
        self.model.save()
        return super().form_valid(form)

class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all
    serializer_class = DriverSerializer      
