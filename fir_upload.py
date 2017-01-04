import requests
import json
import os


file_path = input('Select the BINARY:')
changelog = input('log:')

fir_url = "http://api.fir.im/apps"
headers = {"Content-Type": "application/json"}
body = {"type":"ios",
        "bundle_id":"",
        "api_token":"",
        }
rsp = requests.post(fir_url,headers = headers,json=body)

print(rsp.status_code)

rsp_json = json.loads(rsp.text)

# print('binary = '+rsp_json['cert']['binary']['token'])

update_headers = {'Content-Type': 'multipart/form-data; boundary=----WebKi',
                  # 'Content - Disposition': 'form - data;name = \'MGISRelease.ipa\''
                  }
# file_handle = open(file_path,'rb')
# try:
#     data = file_handle.read()
# finally:
#     file_handle.close()

# binary_body = {'key':rsp_json['cert']['binary']['key'],
#                'token':rsp_json['cert']['binary']['token'],
#                'file':file_path,
#                'x:name':'LiveYes',
#                'x:build':'1.0.0.1',
#                'x:release_type':'Adhoc',
#                'x:changelog':changelog}

update_url = rsp_json['cert']['binary']['upload_url']
# print('update_url:'+update_url)
# update_rsp = requests.post(update_url,json=binary_body,headers=update_headers)
# print(update_rsp.text)

cmd_curl = 'curl   -F    \"key='+ rsp_json['cert']['binary']['key']+'\"'
       # -F "token=xxxxx"             \
       # -F "file=@aa.apk"            \
       # -F "x:name=aaaa"             \
       # -F "x:version=a.b.c"         \
       # -F "x:build=1"               \
       # -F "x:release_type= Adhoc"   \  #type=ios 使用
       # -F "x:changelog=first"       \
       # http://upload.qiniu.com'

os.system(cmd_curl)

