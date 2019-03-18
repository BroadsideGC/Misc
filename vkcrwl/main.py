import json

import requests
import time
import vk

if __name__ == "__main__":
    auth_token = ""
    v = '5.74'
    # session = vk.AuthSession(access_token=auth_token)
    session = vk.AuthSession()
    vk_api = vk.API(session)
    req_count = 200
    sh_id = 22
    peer_id = None
    response = vk_api.messages.getHistory(offset=0, count=req_count, peer_id=peer_id, rev=1, v=v)
    print('In dialog {} messages'.format(response['count']))
    total = response['count']

    file_name = 'sh_messages.json'
    try:
        messages = json.load(open(file_name, encoding='utf-8'))
    except:
        print('No file, create new')
        messages = []
    count = len(messages)
    left = total - count
    while left > 0:
        time.sleep(1)
        response = vk_api.messages.getHistory(offset=count, count=req_count, peer_id=peer_id, rev=1, v=v)
        m = response['items']
        left -= len(m)
        count += len(m)
        messages.extend(m)
        print("Downloaded {} messages, status: {}/{}, {} left, {} percent, {} seconds remaining".format(len(m), count,
                                                                                                        total, left,
                                                                                                        count / total * 100,
                                                                                                        left / req_count))
        if count % 5000 == 0:
            with open(file_name, 'w', encoding='utf-8') as ofile:
                json.dump(messages, ofile, indent=4, ensure_ascii=False)

    with open(file_name, 'w', encoding='utf-8') as ofile:
        json.dump(messages, ofile, indent=4, ensure_ascii=False)
