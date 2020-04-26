from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import pandas as pd
import time
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'polls/home.html')

@csrf_exempt
def index(request):
    df = pd.read_csv('/home/srinidhimadhusudhan/PycharmProjects/mysite/mysite/polls/data.csv')
    data = df.to_json(orient='split', index=False)
    return JsonResponse(data, safe=False)