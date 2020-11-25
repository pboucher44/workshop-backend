import os
from app import *


app.debug = False
#host = os.environ.get('IP', 'O.O.O.O')
port = int(os.environ.get('PORT', 8080))
app.run(port=port)