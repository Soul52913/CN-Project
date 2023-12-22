import shelve
import datetime

def member_info(name, age):
   print("Member info:", name, age)

user = ['testA', 'testB', 'testC']
info = {'name':'testA', 'comment':'Goodbye World!'}
with shelve.open('commentBoard') as db:
    db['user'] = user

    db['comments'].append({'user': user, 'comment': comment, 'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
   
with shelve.open('demo') as data:
    data['name'] = name   #持久化列表
    data['info'] = info   #持久化字典
    data['func'] = member_info
   