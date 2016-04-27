from django.shortcuts import render
from aceSystem.settings import RECO_MAILER_API, LMS_API, LMS_THANKYOU
import requests
import ast
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from models import *
import MySQLdb
from recoMailerSystem.utilities.getUrls import getImageUrl, getProjUrl
from datetime import date
from django.http import HttpResponseRedirect
# Create your views here.

def sendMail(user):
    # userId = request.GET.get('user',None)
    userId = user.unique_cookie_id

    req = requests.get(RECO_MAILER_API + userId)    

    if req.status_code == 200:
        recoProperties = ast.literal_eval(req.content)
        for recoProperty in recoProperties:
            recoProperty['imageUrl'] = getImageUrl(recoProperty['project_no'], recoProperty['project_name']).replace('https://www.', '')
            recoProperty['url'] = getProjUrl(recoProperty['project_no']).replace('https://www.', '')
            
            amenities = recoProperty['amenities'].split(',')

            recoProperty['amenitiesList']=[x for x in amenities if x]
            if len(recoProperty['amenitiesList'])>12:
                recoProperty['amenitiesList'] = recoProperty['amenitiesList'][:12]
                
            #ToDo
            priceLen = len(str(recoProperty['minimum_price']))
            if priceLen<8 and priceLen>5:
                recoProperty['price_string'] = str(recoProperty['minimum_price']/100000)+" L+"
            elif priceLen>7:
                recoProperty['price_string'] = str(recoProperty['minimum_price']/10000000.0)+" Cr+"
            else:
                recoProperty['price_string'] = recoProperty['minimum_price']
            

        mail = EmailMultiAlternatives(
          subject="Thank you for showing interest in HDFCRED",
          body="This is a simple text email body.",
          from_email="HDFC RED <recommendation@hdfcred.com>",
          to=[user.email],
          headers={"Reply-To": "support@hdfcred.com"}
        )
        
        content = {'recoProperties':recoProperties, 'userId':userId}
        email = loader.render_to_string('email.html', content)
        mail.attach_alternative(email, "text/html")
        
        mail.send()

from pymongo import MongoClient
import datetime

class MongoConnectionForWebsite:

    def __init__(self):
        url = 'mongodb://MLadmin:hdfcREDML@52.35.25.23:27017/websiteDataCapture'
        connection = MongoClient(url)
        db = connection.websiteDataCapture
        self.collection = db.redData

    def getLeads(self, timeDiff):
        # TODO query for getting all the filled leads in the past 
        
        UTCdiff = 0

        currentTime = datetime.datetime.now() - datetime.timedelta(minutes=UTCdiff)
        splitted = str(currentTime).split(':')
        currentTime = splitted[0] + ":" + splitted[1]
        lastTime = datetime.datetime.now() - datetime.timedelta(minutes=UTCdiff + timeDiff)
        splitted = str(lastTime).split(':')
        lastTime = splitted[0] + ":" + splitted[1]
        print "mongo query time: " + str(lastTime)+" to " + str(currentTime)
        leadFooterForm = self.collection.find({ "data_storage_element" : "get_in_touch" ,'email': '{ $exists: true, $ne:"" }', "successful_lead":"1", "tsDate" :{"$gte": lastTime , "$lt" : currentTime}}, {"_id":0, "mobilenumber":"1", "name":"1", "email":"1", "project_no":"1", "unique_cookie_id":"1", "tsDate":"1"})
        
        # lead2 = self.collection.find({ "data_storage_element" : "lead_popup" , "tsDate" :{"$gte": lastTime ,"$lt" : currentTime}})
        
        # print lead1
        leads = []

        for lead in leadFooterForm:
            lead['phone'] = lead.pop('mobilenumber')

            leads.append(lead)
        
        return leads

mongo = MongoConnectionForWebsite()

def cronJob(request):
    print "##########################time" + str(datetime.datetime.now())
    leads = mongo.getLeads(10)
    usersList = {}
    for lead in leads:
        usersList[lead['unique_cookie_id']]={'name':lead['name'],'phone':lead['phone'],'email':lead['email']}
        

    for leadUser,lead in usersList.iteritems():
        
        if User.objects.filter(unique_cookie_id=leadUser).exists():
            user = User.objects.get(unique_cookie_id=leadUser)
            
            if len(lead['name'].strip())!=0:
                user.name = lead['name']
            if len(lead['phone'].strip())!=0:
                user.phone=lead['phone']
            if len(lead['email'].strip())!=0:
                user.email=lead['email']
            user.save()
        else:
            user = User(unique_cookie_id=leadUser, name=lead['name'], phone=lead['phone'], email=lead['email'])
            user.save()

        sendMail(user=user)
        
    #no use, just for testing
    for lead in leads:
        if FilledLeads.objects.filter(user_id=lead['unique_cookie_id'], project_no=lead['project_no']).exists():
            pass
        else:
            filledLead = FilledLeads(user_id=lead['unique_cookie_id'], project_no=lead['project_no'])
            filledLead.save()


def sendMailTestApi(request):
    userId = request.GET.get('user', None)
    user = User.objects.get(unique_cookie_id=userId)
    sendMail(user=user)
     
def getProjectInfo(projectConfigNo):

    db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", db="REDADMIN2", cursorclass=MySQLdb.cursors.DictCursor)
    cur = db.cursor()
    cur.execute("select * from REDADMIN2.all_project_info where Project_config_No="+str(projectConfigNo))
    for row in cur.fetchall():
        pass
    
    #ToDo get data directly from 'cur' variable 
    return row


def enquire(request):
    userId = request.GET.get('user', None)
    projectId = request.GET.get('project', None)
#     projectConfigNo = request.GET.get('projectConfig', None)
#     project = getProjectInfo(projectConfigNo)
#     priceLen = len(str(project['Minimum_Price']))
#     
#     amenities = project['amenities'].split(',')
# 
#     project['amenitiesList']=[x for x in amenities if x]
#     if len(project['amenitiesList'])>12:
#         project['amenitiesList'] = project['amenitiesList'][:12]
#         
#     #ToDo
#     if priceLen<8 and priceLen>5:
#         project['price_string'] = str(project['Minimum_Price']/100000)+" L+"
#     elif priceLen>7:
#         project['price_string'] = str(project['Minimum_Price']/10000000.0)+" Cr+"
#     else:
#         project['price_string'] = project['Minimum_Price']
#     
#     project['imageUrl'] = getImageUrl(projectId, project['Project_Name'])
#     project['url'] = getProjUrl(projectId)

    user = User.objects.get(unique_cookie_id=userId)
    
    
    lms_url=LMS_API % (projectId,user.name,user.email,user.phone)
    response = requests.get(lms_url)
    if response.status_code==200:
        leadResponse = ast.literal_eval(response.content)
        
    newLead = Lead(project_no=projectId, user=user, lmsResponseNo=leadResponse['Project_Enquiry_No'])
    newLead.save()
    
    return HttpResponseRedirect(LMS_THANKYOU+str(leadResponse['Project_Enquiry_No']))
#     context = {'project':project}
#     return render(request, 'thankYou.html', context)

