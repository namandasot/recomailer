from django.shortcuts import render
from aceSystem.settings import RECO_MAILER_API
import requests
import ast

# Create your views here.

def sendMail(request):
    userId = request.GET.get('user',None)
    print userId

    req = requests.get(RECO_MAILER_API+userId)    
    print req.status_code
    if req.status_code == 200:
        recoProperties = ast.literal_eval(req.content)
        
        
    
    
