from django.shortcuts import render

# Database model
from web.models import User


# Create your views here.
def index(request):
    user = User.objects.all()
    return render(request, 'index.html', locals())
