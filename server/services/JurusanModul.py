from flask import jsonify,request
from flask_restful import Resource
from server.models import KUK,ElemenKompetensi,UjiKompetensi,Jurusan
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
	def get(self):
		return jsonify(list_kuk = [dict(idKUK=kuk.idKUK,pertanyaan=kuk.Pertanyaan,elemen=kuk.elemen) for kuk in KUK.query.all()],response=200)

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
	def get(self):
		return jsonify(list_elemen=[dict(idElemen=elemen.idElemen,nama=elemen.Nama,ujikompetensi=elemen.ujikompetensi) for elemen in ElemenKompetensi.query.all()],
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
		unit = UjiKompetensi.query.filter_by(KodeUnit=kodeUnit).first()
		if unit is not None:
			return jsonify(unit={'KodeUnit':unit.KodeUnit,'judul':unit.JudulUnit},response=200)
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
	def get(self):
		return jsonify(list_ujikompetensi=[dict(KodeUnit=unit.KodeUnit,JudulUnit=unit.JudulUnit) for unit in UjiKompetensi.query.all()],
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

class JurusanService(Resource):
	def get(self,kodeJurusan):
		jurusan = Jurusan.query.filter_by(idJurusan=kodeJurusan).first()
		if jurusan is not None:
			return jsonify(jurusan={'idJurusan':jurusan.idJurusan,'Nama':jurusan.Nama,'kompetensi':jurusan.kompetensi},response=200)
		else:
			return jsonify(response=204)
	
	def put(self,kodeJurusan):
		jurusan = Jurusan.query.filter_by(idJurusan=kodeJurusan).first()
		if jurusan is not None:
			jurusan.Nama = request.form['nama']
			jurusan.kompetensi = request.form['kompetensi']
			db.session.commit()
			return jsonify(response=201)
		else:
			return jsonify(response=204)

	def delete(self,kodeJurusan):
		jurusan = Jurusan.query.filter_by(idJurusan=kodeJurusan).first()
		if jurusan is not None:
			db.session.delete(jurusan)
			db.session.commit()
			return jsonify(response=202)
		else:
			return jsonify(response=204)

class JurusanServiceList(Resource):
	def get(self):
		return jsonify(list_jurusan=[dict(idJurusan=jurusan.idJurusan,nama=jurusan.Nama,kompetensi=jurusan.kompetensi) for jurusan in Jurusan.query.all()],response=200)

	def post(self):
		try:
			jurusan = Jurusan(id=request.form['idJurusan'],nama=request.form['nama'],kompetensi=request.form['kompetensi'])
			db.session.add(jurusan)
			db.session.commit()
			return jsonify(response=201)
		except Exception as e:
			return jsonify(response=204,error=e)