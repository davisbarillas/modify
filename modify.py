#!/bin/sh
import os
import requests
from config import SHIFTLEFT_ORG_ID, SHIFTLEFT_ACCESS_TOKEN

url = 'https://www.shiftleft.io/api/v4/orgs/{}/apps'.format(SHIFTLEFT_ORG_ID)
headers = {'Authorization':'Bearer {}'.format(SHIFTLEFT_ACCESS_TOKEN)}
r = requests.get(url, headers=headers)
apps = r.json()['response']
#print(apps)

app_id_list = []
for app in apps:
  if 'id' in app:
    app_id = app['id']
    #print(app_id)
    app_id_list.append(app_id)
    #print(app_id_list)

for apps in app_id_list:
  os.system('sl modify-findings --app %s' % apps)

