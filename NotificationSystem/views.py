from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Notification System API. Go to /admin/ or /api/")
