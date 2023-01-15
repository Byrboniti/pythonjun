from tinydb import TinyDB, Query

db = TinyDB('db.json')

User = Query()


def insert():
    db.insert({"name": "MyForm", "user_phone": "phone", "order_date": "date", "lead_email": "email"})


# insert()

def search(data: dict):
    list_for_comp = []
    for i in data:
        for d in db:
            try:
                list_for_comp.append(d[data[i]])
            except:
                pass
    if len(d) == len(list_for_comp) + 1:
        return d['name']
    else:
        return
