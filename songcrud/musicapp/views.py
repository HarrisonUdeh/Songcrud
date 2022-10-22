
from django.http import HttpResponse


def index(request):
    return HttpResponse('Welcome to Musicapp')
# Create your views here.
