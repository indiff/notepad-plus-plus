#!/usr/local/bin/python3
import requests
import os
# 上传文件到企业微信
# https://developer.work.weixin.qq.com/document/path/91770#%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%8E%A5%E5%8F%A3
def upload_file(key, file_path):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
    # files = {'file': (open(file_path, "rb"), 'application/octet-stream')}
    #files = {'file': (open(file_path, "rb")}
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    print( f"file size: {file_size}" )
    if file_size < 5:
        print( "文件大小需要超过5字节！" )
    files = {file_name: open(file_path, "rb"), 'Content-Type':'application/octet-stream'}
    response = requests.post(url, files=files,headers={'Content-Type': 'multipart/form-data'})
    print( response.json() )
    # assert response.json()['errmsg'] == 'ok'
    return response.json().get('media_id')

# 发送文件消息
def send_file_message(key, media_id):
    if media_id != None and media_id.strip() != '':
        url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        data = {
            "msgtype": "file",
            "file": {
                "media_id": media_id
            }
        }
        response = requests.post(url, json=data)
        print(response.json())
        return response.json()
    else:
        return f"error {media_id}"
    


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python send.py filePath")
    else:
        file_path = sys.argv[1].strip()
        my_key = sys.argv[2].strip()
        if my_key and len(my_key) > 10:
            key_flag = True
        else:
            key_flag = False
            for key in ("ENV_MY_KEY1_VAR", "secrets.MY_KEY", "vars.MY_KEY1","MY_KEY", "MY_KEY1"):
                my_key = os.getenv(key)
                if my_key and len(my_key) > 10:
                    key_flag = True
                    print(f"Get my_key right by {key}!")
                    break
                else:
                    key_flag = False
                    print(f"Get my_key failed by {key}!")
        if not key_flag:
            print("Exit without key!")
            sys.exit(0)
        # 比较并输出结果
        # 示例使用
        #file_path = 'test.txt'
        #file_path = '佛本是道.txt'
        media_id = upload_file(my_key, file_path)
        send_file_message(my_key, media_id)

    
    
    
