import pyrogram , pyromod

from pyromod import listen

from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='plugins')
tok = '7157644857:AAFF5YNsgIzFuGYvcf5elKvsRS3f6Y3dJkM' ## توكنك 
id = 5108562302 ## ايديك
db = dt("data.sqlite", 'fuck')
if not db.get("checker"):
  db.set('checker', None)
if not db.get("admin_list"):
  db.set('admin_list', [id, ])
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('sessions'):
  db.set('sessions', [])
if not db.get('force'):
  db.set('force', ['trprogram'])
x = Client(name='loclhosst', api_id=9886513, api_hash='f8835482f0740d5aaa27c8e07013f4a9', bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)

x.run()
