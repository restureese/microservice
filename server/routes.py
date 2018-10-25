from flask import request,jsonify
from flask_restful import Resource
from server.services.SkemaModul import KUKService,KUKServiceList,ElemenKompetensiService,ElemenKompetensiServiceList
from server.services.SkemaModul import UjiKompetensiService,UjiKompetensiServiceList,SkemaService,SkemaService,SkemaServiceList
from server import api,db


#Skema
api.add_resource(SkemaService,'/Skema/<string:kodeSkema>')
api.add_resource(SkemaServiceList,'/Skema/')

#uji kompetensi
api.add_resource(UjiKompetensiService,'/Skema/kompetensi/all/<kodeUnit>')
api.add_resource(UjiKompetensiServiceList,'/Skema/kompetensi/<kodeSkema>')

#elemen
api.add_resource(ElemenKompetensiService,'/Skema/kompetensi/elemen/all/<idElemen>')
api.add_resource(ElemenKompetensiServiceList,'/Skema/kompetensi/elemen/<kodeUnit>')

#kuk
api.add_resource(KUKService,'/Skema/kompetensi/elemen/kuk/all/<id_kuk>')
api.add_resource(KUKServiceList,'/Skema/kompetensi/elemen/kuk/<idElemen>')