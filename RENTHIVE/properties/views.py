from django.shortcuts import render
from .models import Property

# Create your views here.
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})
