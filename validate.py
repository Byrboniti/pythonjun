import re



def valid(request:str):
    list_data = request.split('&')
    result_dict = {}
    for i in list_data:
        key = i.split('=')[0]
        value = i.split('=')[1]
        if re.fullmatch(r"[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])",value) or re.fullmatch(
            r"(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((19|20)\d\d)", value):
             result_dict[key]="order_date"
        elif re.fullmatch(r"^((\+7|7|8)+([0-9]){10})$", value):
            result_dict[key]="user_phone"
        elif re.fullmatch(r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$",value):
             result_dict[key]="lead_email"
        elif type(value) == str:
             result_dict[key]="text"
        else:
            result_dict[key] = "FIELD_TYPE"
    if len(result_dict) == len(list_data):
        return result_dict

# print(valid("f_name1=rewer-96@mail.ru&f_name2=+79161103850"))

# search(valid("f_name1=rewer-96@mail.ru&f_name2=+79161103850&f_name3=19.08.1996&f_name4=texttt"))