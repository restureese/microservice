from flask import request,jsonify
from flask_restful import Resource
from server.services.JurusanModul import KUKService,KUKServiceList,ElemenKompetensiService,ElemenKompetensiServiceList
from server.services.JurusanModul import UjiKompetensiService,UjiKompetensiServiceList,JurusanService,JurusanService,JurusanServiceList
from server import api,db


#jurusan
api.add_resource(JurusanService,'/jurusan/<kodeJurusan>')
api.add_resource(JurusanServiceList,'/jurusan/')

#uji kompetensi
api.add_resource(UjiKompetensiService,'/jurusan/kompetensi/<kodeUnit>')
api.add_resource(UjiKompetensiServiceList,'/jurusan/kompetensi/')

#elemen
api.add_resource(ElemenKompetensiService,'/jurusan/kompetensi/elemen/<idElemen>')
api.add_resource(ElemenKompetensiServiceList,'/jurusan/kompetensi/elemen/')

#kuk
api.add_resource(KUKService,'/jurusan/kompetensi/elemen/kuk/<id_kuk>')
api.add_resource(KUKServiceList,'/jurusan/kompetensi/elemen/kuk/')