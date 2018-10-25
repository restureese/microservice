from flask_admin.contrib.sqla import ModelView
from server.models import KUK,ElemenKompetensi,UjiKompetensi,Skema
from server import admin,db

admin.add_view(ModelView(KUK, db.session))
admin.add_view(ModelView(ElemenKompetensi, db.session))
admin.add_view(ModelView(UjiKompetensi, db.session))
admin.add_view(ModelView(Skema, db.session))