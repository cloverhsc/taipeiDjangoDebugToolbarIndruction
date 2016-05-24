from django.shortcuts import render

# Database model
from web.models import Friends


# Create your views here.
def index(request):
    if request.POST:
        if request.POST['weight']:      # if get weight
            user = Friends.objects.filter(weight__lt=request.POST['weight'])
            return render(request, 'index.html', {'content': user})
        else:
            # if weight is null. show all
            user = Friends.objects.all()
            return render(request, 'index.html', {'content': user})
    else:
        # default show all.
        user = Friends.objects.all()
        return render(request, 'index.html', {'content': user})
