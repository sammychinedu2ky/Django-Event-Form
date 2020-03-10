from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.db.models import Q
from .models import Detail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
# Create your views here.
def index(request):
    return render(request,'aihacks/index.html',)

class IndexView(generic.ListView):
    template_name = 'aihacks/index.html'
    def get_queryset(self):
        return Detail.objects.all()


def code(request):
   name =  request.POST['name']
   school = request.POST['school']
   email = request.POST['email']
   existing = Detail.objects.filter(Email=email)
   space = Detail.objects.filter(Q(Email='') | Q(Email__isnull = True))
   if(len(existing)==0 and len(space)>0):
        space[0].Email = email
        space[0].Attendee_University_Name = school
        space[0].Attendee_First_Name = name 
        space[0].save()
        
        return render(request,'aihacks/check.html',{'code':space[0]})
   elif len(existing)==1:
        
        return render(request,'aihacks/check.html',{'code':existing[0]})
   else:
        
        return render(request,'aihacks/check.html',{'code':'Not available'})
   


