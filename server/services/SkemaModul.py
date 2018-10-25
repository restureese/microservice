from flask import jsonify,request
from flask_restful import Resource
from server.models import KUK,ElemenKompetensi,UjiKompetensi,Skema
from server import db,api


class KUKService(Resource):
	"""Class untuk melayani data tunggal seperti menampilkan, edit serta hapus kuk"""

	#fungsi untuk mengembalikan satu kuk
	def get(self,id_kuk):
		kuk = KUK.query.filter_by(idKUK=id_kuk).first()
		if kuk is not None:
			return jsonify(kuk={'idKUK':kuk.idKUK,'pertanyaan':kuk.Pertanyaan,'elemen':kuk.elemen},response=200)
		else:
			return jsonify(response=204)

	#fungsi untuk mengedit kuk
	def put(self,id_kuk):
		kuk = KUK.query.filter_by(idKUK=request.form['id_kuk']).first()
		if kuk is not None:
			kuk.Pertanyaan = request.form['pertanyaan']
			kuk.elemen = request.form['elemen']
			db.session.commit()
			return jsonify(response=201)
		else:
			return jsonify(response=204)
	
	#fungsi untuk menghapus kuk
	def delete(self,id_kuk):
		kuk = KUK.query.filter_by(idKUK=request.form['id_kuk']).first()
		if kuk is not None:
			db.session.delete(kuk)
			db.session.commit()
			return jsonify(response=202)
		else:
			return jsonify(response=204)

class KUKServiceList(Resource):
	"""class untuk melayani data yang banyak"""
	
	#mengembalikan semua service list
	def get(self,idElemen):
		return jsonify(list_kuk = [dict(idKUK=kuk.idKUK,pertanyaan=kuk.Pertanyaan) for kuk in KUK.query.filter_by(elemen=idElemen).all()],response=200)

	#menambah kuk
	def post(self):
		try:
			kuk = KUK(idKUK=request.form['idKUK'],Pertanyaan=request.form['pertanyaan'],elemen=request.form['elemen'])
			db.session.add(kuk)
			db.session.commit()
			return jsonify(response=201)
		except Exception as e:
			return jsonify(response=304,error=e)


class ElemenKompetensiService(Resource):
	"""class untuk melayani data tunggal dari elemen kompetensi"""


	def get(self,idElemen):
		elemen = ElemenKompetensi.query.filter_by(idElemen=idElemen).first()
		if elemen is not None:
			return jsonify(elemen={'idElemen':elemen.idElemen,'Nama':elemen.Nama,'ujikompetensi':elemen.ujikompetensi},response=200)
		else:
			return jsonify(response=204)

	def put(self,idElemen):
		elemen = ElemenKompetensi.query.filter_by(idElemen=idElemen).first()
		if elemen is not None:
			elemen.Nama = request.form['nama']
			elemen.ujikompetensi = request.form['ujikompetensi']
			db.session.commit()
			return jsonify(response=201)
		else:
			return jsonify(response=204)

	def delete(self,idElemen):
		elemen = ElemenKompetensi.query.filter_by(idElemen=idElemen).first()
		if elemen is not None:
			db.session.delete(elemen)
			db.session.commit()
			return jsonify(response=202)
		else:
			return jsonify(response=204)

class ElemenKompetensiServiceList(Resource):
	def get(self,kodeUnit):
		return jsonify(list_elemen=[dict(idElemen=elemen.idElemen,nama=elemen.Nama) for elemen in ElemenKompetensi.query.filter_by(ujikompetensi=kodeUnit).all()],
			response=200)

	def post(self):
		try:
			elemen = ElemenKompetensi(nama=request.form['nama'],ujikompetensi=request.form['ujikompetensi'])
			db.session.add(elemen)
			db.session.commit()
			return jsonify(response=201)
		except Exception as e:
			return jsonify(response=304,error=e)

class UjiKompetensiService(Resource):
	def get(self,kodeUnit):
		unit = UjiKompetensi.query.filter_by(kodeUnit=kodeUnit).first()
		if unit is not None:
			return jsonify(unit={'KodeUnit':unit.kodeUnit,'judul':unit.judulUnit},response=200)
		else:
			return jsonify(response=204)

	def put(self,kodeUnit):
		unit = UjiKompetensi.query.filter_by(KodeUnit=kodeUnit).first()
		if unit is not None:
			unit.JudulUnit = request.form['judulunit']
			db.session.commit()
			return jsonify(response=201)
		else:
			return jsonify(response=204)

	def delete(self,kodeUnit):
		unit = UjiKompetensi.query.filter_by(KodeUnit=kodeUnit).first()
		if unit is not None:
			db.session.delete(unit)
			db.session.commit()
			return jsonify(response=202)
		else:
			return jsonify(response=204)

class UjiKompetensiServiceList(Resource):
	def get(self,kodeSkema):
		return jsonify(list_ujikompetensi=[dict(KodeUnit=unit.kodeUnit,JudulUnit=unit.judulUnit) for unit in UjiKompetensi.query.filter_by(Skema=kodeSkema).all()],
			response=200)

	def post(self):
		try:
			print(request.form['kodeUnit'])
			unit = UjiKompetensi(kode=request.form['kodeUnit'],judul=request.form['judul'])

			db.session.add(unit)
			db.session.commit()
			return jsonify(response=201)
		except Exception as e:
			return jsonify(response=304,error=e)

class SkemaService(Resource):
	def get(self,kodeSkema):
		skema = Skema.query.filter_by(idSkema=kodeSkema).first()
		if skema is not None:
			return jsonify(Skema={'idSkema':skema.idSkema,'Nama':skema.Nama},response=200)
		else:
			return jsonify(response=204)
	
	def put(self,kodeSkema):
		Skema = Skema.query.filter_by(idSkema=kodeSkema).first()
		if Skema is not None:
			Skema.Nama = request.form['nama']
			Skema.kompetensi = request.form['kompetensi']
			db.session.commit()
			return jsonify(response=201)
		else:
			return jsonify(response=204)

	def delete(self,kodeSkema):
		Skema = Skema.query.filter_by(idSkema=kodeSkema).first()
		if Skema is not None:
			db.session.delete(Skema)
			db.session.commit()
			return jsonify(response=202)
		else:
			return jsonify(response=204)

class SkemaServiceList(Resource):
	def get(self):
		return jsonify(list_Skema=[dict(idSkema=Skema.idSkema,nama=Skema.Nama) for Skema in Skema.query.all()],response=200)

	def post(self):
		try:
			Skema = Skema(id=request.form['idSkema'],nama=request.form['nama'],kompetensi=request.form['kompetensi'])
			db.session.add(Skema)
			db.session.commit()
			return jsonify(response=201)
		except Exception as e:
			return jsonify(response=204,error=e)