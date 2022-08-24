from django.shortcuts import render
from main.models import Good

# Create your views here.
def show_index(request):
    product = Good.objects.all()
    context = {
        "pr": product
    }
    return render(request, 'index.html', context=context)