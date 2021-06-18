from typing import List
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import FormView
from .models import Driver
from .serializer import DriverSerializer
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist

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
## You must comment out DriverUpdateView before you migrate the db. Then comment back in.
class DriverUpdateView(FormView):

    template_name='update.html'
    # add a try/except for model because there isnt always a 'driver' instance at the beginning.
    try:
        driver = Driver.objects.all()
        # For the purpose of this exercise, this api does not need to account for multiple drivers simultaneously
        
        if driver:
            model = driver[0]
            # print(f'model is: {model}')
          
            form_class = RawWorkForm
            success_url = '/'

            def form_valid(self, form):
                # print(f'form is {form}')
                work = form.cleaned_data['work']
                drive = form.cleaned_data['drive']
                off = form.cleaned_data['off']
                # print(f'off is {off}')
                # print(f'work_clock is {self.model.work_clock}')

                if off >= 10:
                    self.model.work_clock = 14
                    self.model.drive_clock = 10
                    self.model.work_status = 'OK'
                    self.model.drive_status = 'OK'
                    self.model.save()
                    # print(f'off 10 work_clock is {self.model.work_clock}')
                else:
                    all_times = work + drive + off
                    # print(f'all times is {all_times}')

                    if (self.model.work_clock > all_times):
                        self.model.work_clock -= all_times

                        # print(f'result is: {self.model.work_clock}')
                    else:
                        # print('In Violation!')
                        self.model.work_clock = 0
                        self.model.work_status = 'In Violation.'

                    if self.model.drive_clock > drive:
                        self.model.drive_clock -= drive
                    else:
                        self.model.drive_clock = 0
                        self.model.drive_status = 'In Violation.'

                    self.model.save()
                return super().form_valid(form)

    ## This except is not currently working...
    except ObjectDoesNotExist: 
        pass
    

class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer      
