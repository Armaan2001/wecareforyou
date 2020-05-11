from django.shortcuts import render

# Create your views here.
def confessions(request):
    return render(request, 'confessions.html')