from django.http import HttpResponse
# Create your views here.

def faculty_home(request):
    return HttpResponse("<h1>Welcome to Faculty Home Page</h1>")

def faculty_profile(request):
    return HttpResponse("Welcome to Faculty Profile Page")