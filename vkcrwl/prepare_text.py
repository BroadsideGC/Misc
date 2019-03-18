import json

if __name__ == "__main__":
    file_name = 'sh_messages_tg.json'
    messages = json.load(open(file_name, encoding='utf-8'))['items']
    p = []
    for m in messages:
        if not m.get('action'):
            pm = {
                'from_id': m['from_id'],
                'date': m['date'],
                'body': m['body']
            }
            p.append(pm)
    current = 0
    p2 = []
    while current < len(p):
        curr = current + 1
        pm = {
            'from_id': p[current]['from_id'],
            'body': p[current]['body']
        }
        time = p[current]['date']
        while curr < len(p) and p[curr]['from_id'] == p[current]['from_id'] and p[curr]['date'] - time < 35:
            print('Merge {} and {}'.format(p[current], p[curr]))
            pm['body'] += '\n' + p[curr]['body']
            time = p[curr]['date']
            curr += 1
        p2.append(pm)
        current = curr
        print(pm)
        print(current)

    prepared = p2
    with open('prepared_{}'.format(file_name), 'w', encoding='utf-8') as ofile:
        json.dump(prepared, ofile, indent=4, ensure_ascii=False)
