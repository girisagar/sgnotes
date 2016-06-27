from sortable import Sortable, sort
import random
from pprint import pprint as dekha


class User(Sortable):

    def __init__(self, name, uid):
	self.name = name
	self.uid = uid
	
def compute():
    ast = []
    for i in xrange(10):
	ast.append(User('name_'+str(i), random.choice(range(200,206))))
    return ast

st = compute()
#users = sort(st, fields=['uid', 'name'], reverse=True)
users = sort(st, fields=['uid', 'name']) # default reverse=False
named = [[u.uid,u.name] for u in users ]
dekha(named)

