from flask_restful import Resource
from server.models import Asesi
from server import db,api

class AsesiService(Resource):
	def get(self,id_asesi):
		asesi = Asesi.query.filter_by(id=id_asesi).first()
		if asesi is not None:
			return jsonify(asesi={'id':asesi.id,'nama':asesi.nama},response=200)
		else:
			return jsonify(response=204)
	
	def put(self,id_asesi):
		asesi = Asesi.query.filter_by(id=request.form['id']).first()
		if asesi is not None:
			asesi.nama = request.form['nama']
			db.session.commit()
			return jsonify(response=201)
		else:
			return jsonify(response=204)

	def delete(self,id_asesi):
		asesi = Asesi.query.filter_by(id=request.form['id']).first()
		if asesi is not None:
			db.session.delete(asesi)
			db.session.commit()
			return jsonify(response=202)
		else:
			return jsonify(response=204)

class AsesiServiceList(Resource):
	def get(self):
		return jsonify(list_asesi = [dict(id=asesi.id,nama=asesi.nama) for asesi in Asesi.query.all()])

	def post(self):
		try:
			a = Asesi(id=request.form['id'],nama=request.form['nama'])
			db.session.add(a)
			db.session.commit()
			return jsonify(response=201)
		except Exception as e:
			return jsonify(response=304,error=e)
			
api.add_resource(AsesiService,'/asesi/<id_asesi>')
api.add_resource(AsesiServiceList,'/asesi/')