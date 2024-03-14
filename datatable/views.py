from django.shortcuts import render

# Create your views here.

def datatable_main(request):
    context ={}         
    return render(request, "index.html", {'context':context})