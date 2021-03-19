from django.shortcuts import render
import logging

log = logging.getLogger(__name__)

def hello(request):
    log.info("In hello_app/views.py. This is the view function, where a request turns into a response.")
    params = {
        "name": "stranger",
        "color": "skyblue",
    }
    return render(request, 'hello_app/index.html', params)
