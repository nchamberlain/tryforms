from django.shortcuts import render, redirect
from .forms import ExampleForm, ClientForm

# Create your views here.
def contact(request):
    form = ExampleForm()
    return render(request, "main/contact.html", {'form': form})

def client(request):
    form = ClientForm()
    return render(request, "main/client.html", {"form": form})