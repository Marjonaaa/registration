from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import *




def home(request):
    post =Mickey.objects.all()
    context ={
        "post":post
    }
    return render(request,"index.html",context)
@login_required
def open(request,post_id):
    link = get_object_or_404(Mickey,pk=post_id)

    return render(request,"views.html",{"link":link})

def delete (request,id):
    delete = Mickey.objects.get(id=id)

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  NewUserForm

    def get_success_url(self):
        return reverse('home')