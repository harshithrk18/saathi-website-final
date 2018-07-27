from django.shortcuts import render
from saathiweb.forms import AppointmentForm

# Create your views here.
def index(request):
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'saathiweb/index.html',{'form':form})
