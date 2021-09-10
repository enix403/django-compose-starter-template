from django.shortcuts import render

from app.bootstrap.configmanager import ConfigManager

def index(request):
    return render(request, "main/index.html", {
        'debug_status': 'True' if ConfigManager.get_bool('runtime.debug') else 'False'   
    })