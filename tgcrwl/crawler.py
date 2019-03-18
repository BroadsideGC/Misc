import json
import time

import socks
from telethon.sync import TelegramClient

if __name__ == "__main__":
    api_id = None
    api_hash = ''

    client = TelegramClient('tgcrawler', api_id, api_hash)
    client.start(phone='')

    print(client.is_user_authorized())
    req_count = 200
    sh_id = None
    file_name = 'sh_messages_tg.json'
    messages = []
    loaded=0
    try:
        d = json.load(open(file_name, encoding='utf-8'))
        messages = d['items']
        loaded = d['items'][-1]['id']
    except:
        print('No file, create new')
        messages = []

    process = True
    # msg_it = client.iter_messages(sh_id, limit=200000)
    min = loaded
    max = loaded + req_count
    while process:
        process = False
        t = client.get_messages(sh_id, limit=0).total
        offset = loaded + req_count + 1
        msgs = client.get_messages(sh_id, offset_id=offset, min_id=loaded, limit=200)
        loaded += req_count

        for m in reversed(msgs):
            process = True
            msg = {
                'id': m.id,
                'from_id': m.from_id,
                'body': m.message,
                'date': time.mktime(m.date.timetuple())
            }
            messages.append(msg)
        if loaded % 4000 == 0:
            print("Loaded {}/{} messages, {} percent".format(loaded, t, loaded / t * 100))
            with open(file_name, 'w', encoding='utf-8') as ofile:
                json.dump(messages, ofile, indent=4, ensure_ascii=False)

    with open(file_name, 'w', encoding='utf-8') as ofile:
        json.dump(messages, ofile, indent=4, ensure_ascii=False)
