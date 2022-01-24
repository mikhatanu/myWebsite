from django.shortcuts import render

from .models import Profile

# Create your views here.
def aboutMe_view(request,**kwargs):
    data = Profile.objects.get(id=1)
    context = {
        'name'     :data.name,
        'summary'  :data.summary,
        'image'    :str(data.image).split("/",2)[2],
    }
    return render(request,"about.html", context)