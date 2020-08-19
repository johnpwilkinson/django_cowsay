from django.shortcuts import render
from .forms import Cow_Say_What
from .models import Cow_Say_What_Model
from django.shortcuts import render, HttpResponseRedirect, reverse
import subprocess

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Cow_Say_What(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p1 = subprocess.run(['cowsay', data.get('message')], capture_output=True, text=True)
            Cow_Say_What_Model.objects.create(
                message=data.get('message'),
                cow_output=p1.stdout
            )
            return HttpResponseRedirect(reverse('homepage'))
            
    form = Cow_Say_What()
    current_cow = Cow_Say_What_Model.objects.all().order_by('-id')[0]
    return render(request, 'index.html', {"form" : form, "cows" : current_cow})

def message_list(request):
    my_messages = Cow_Say_What_Model.objects.all().order_by('-id')[0:10]
    return render(request, 'messages.html', {'messages': my_messages})