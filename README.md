# Server

- Commands

```
virtualenv env
.\env\Scripts\activate.ps1
pip install -r requirements.txt
```

- Commands For Database

```
python
from app import app
from models import db
db.create_all(app=app)
exit()
```
