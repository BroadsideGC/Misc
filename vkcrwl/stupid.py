import json
import re

if __name__ == "__main__":
    file_name = 'sh_messages_tg.json'
    messages = json.load(open(file_name, encoding='utf-8'))
    p = []

    with open('st_{}'.format(file_name), 'w', encoding='utf-8') as ofile:
        for m in messages:
            if m['body']:
                text = m['body']
                ofile.write(m['body'].lower() + '.\n')
