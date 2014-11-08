import gflags
import httplib2
import os
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

FLAGS = gflags.FLAGS

flow= OAuth2WebServerFlow(
    client_id='654508866595-nuioh4ltmvm0k1823dp1a4klbdtlhbum.apps.googleusercontent.com',
    client_secret='sN4IdQC-m0srLHB7mfRofoQP',
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='http://localhost:8080/')

storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None:
    auth_uri = flow.step1_get_authorize_url()
    
#auth_uri = FLOW.step1_get_authorize_url()
#code = raw_input('Enter verification code: ').strip()
#print auth_uri
#credentials = FLOW.step2_exchange(code)

http = httplib2.Http()
http = credentials.authorize(http)

service = build(serviceName='calendar', version='v3', http=http,
       developerKey='AIzaSyANOof1QKLwpAZU3fsRKsyQsVrMEXXgi7I')
