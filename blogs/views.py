from django.shortcuts import render

from .models import Post

# Create your views here.
def blogs_view(request,**kwargs):
    obj = Post.objects.all()[:5]
    context = {"blog_post":[]}

    for data in obj:
        context['blog_post'].append({
            'title'     :data.title,
            'text'      :data.text,
            'image'     :str(data.image).split("/",2)[2],
            'featured'  :data.featured
        })
    return render(request,"blogs.html",context)