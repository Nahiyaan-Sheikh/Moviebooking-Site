from django.shortcuts import render
from django.http import HttpResponse

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")



def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')
def regisconfirmation(request):
    return render(request, 'regisconfirmation.html')