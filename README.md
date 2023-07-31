# Face Detection
This is a simple flask app that used to face detection. Along with it login and signup with Sqlite3 database and password hashing are included.

>For Run this code

```
python app.py
```

### To initialize the database
```
flask --app app shell
from app import db
db.create_all()
```

Framework used Flask
