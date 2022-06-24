from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

context = {'debug_mode': settings.DEBUG}

@csrf_exempt
def index(request):
	return render(request, 'app/index.html', context)

