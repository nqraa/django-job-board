from django.shortcuts import render

# Create your views here.

from .models import job

def job_list(request):
    job_list = job.objects.all()
    context = {'jobs' : job_list}
    return render(request,'job/job_list.html',context)





def job_details(request ,id):
    job_details = job.objects.get(id=id)
    context = {'job' : job_details}
    return render(request,'job/job_details.html',context)