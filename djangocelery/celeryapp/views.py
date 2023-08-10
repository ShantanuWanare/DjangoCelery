from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse
from mailapp.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule
import json
# Create your views here.


def test(request):
    test_func.delay()
    return HttpResponse('done ')

def send_mail(request):
    send_mail_func.delay() 
    return HttpResponse('sent')

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=1, minute=5)
    task = PeriodicTask.objects.create(crontab=schedule, name='schedule_mail_task'+'60', task='mailapp.tasks.send_mail_func') #args=json.dumps([[2,3,]]))
    send_mail_func.delay()
    return HttpResponse('done')
