from django.shortcuts import render

# Database model
from web.models import Friends


# Create your views here.
def index(request):
    user = Friends.objects.all()
    return render(request, 'index.html', locals())
