from server import db
from werkzeug.security import generate_password_hash, check_password_hash


class UjiKompetensi(db.Model):
	__tablename__ = 'UjiKompetensi'
	KodeUnit = db.Column(db.String(128),primary_key=True)
	JudulUnit = db.Column(db.String(128),nullable=False)

	def __init__(self, kode,judul):
		self.KodeUnit = kode
		self.JudulUnit = judul

	def __repr__(self):
		return self.KodeUnit

class Jurusan(db.Model):
	__tablename__ = 'Jurusan'
	idJurusan = db.Column(db.Integer,primary_key=True)
	Nama = db.Column(db.String(64),nullable=False)
	kompetensi = db.Column(db.String(128),db.ForeignKey('UjiKompetensi.KodeUnit'))

	def __init__(self,id,nama,kompetensi):
		self.idJurusan = id
		self.Nama = nama
		self.kompetensi = kompetensi

	def __repr__(self):
		return self.idJurusan

class ElemenKompetensi(db.Model):
	__tablename__ = 'ElemenKompetensi'
	idElemen = db.Column(db.Integer, primary_key=True,autoincrement=True)
	Nama = db.Column(db.String(128), nullable=False)
	ujikompetensi = db.Column(db.String(128),db.ForeignKey('UjiKompetensi.KodeUnit'))


	def __init__(self,nama,ujikompetensi):
		self.Nama = nama
		self.ujikompetensi = kompetensi

	def __repr__(self):
		return self.idElemen

class KUK(db.Model):
	__tablename__= 'KUK'
	idKUK = db.Column(db.Integer,primary_key=True,autoincrement=True)
	Pertanyaan = db.Column(db.String(255),nullable=False)
	elemen = db.Column(db.Integer,db.ForeignKey('ElemenKompetensi.idElemen'))

	def __init__(self,Pertanyaan,elemen):
		self.Pertanyaan = Pertanyaan
		self.elemen = elemen

	def __repr__(self):
		return self.idKUK



class Pekerjaan(db.Model):
	__tablename__ = 'Pekerjaan'
	idPekerjaan = db.Column(db.Integer, primary_key=True, autoincrement=True)
	NamaPerusahaan = db.Column(db.String(128), nullable=False)
	Jabatan = db.Column(db.String(128))
	Alamat = db.Column(db.String(255))
	KodePos = db.Column(db.String(8))
	NoTelepon = db.Column(db.String(13))
	NoFax = db.Column(db.String(32))
	Email = db.Column(db.String(64))

	def __init__(self,nama, jabatan, alamat, pos,telepon, fax, email):
		self.NamaPerusahaan = nama
		self.Jabatan = jabatan
		self.Alamat = alamat
		self.KodePos = pos
		self.NoTelepon = telepon
		self.NoFax = fax
		self.Email = email

class Asesi(db.Model):
	__tablename__ = 'Asesi'
	idAsesi = db.Column(db.Integer, primary_key=True, autoincrement=True)
	NamaLengkap = db.Column(db.String(64), nullable=False)
	TempatLahir = db.Column(db.String(255), nullable=False)
	JenisKelamin = db.Column(db.String(1), nullable=False)
	Kebangsaan = db.Column(db.String(64), nullable=False)
	Alamat = db.Column(db.String(255), nullable=False)
	KodePos = db.Column(db.String(8), nullable=False)
	NoHP = db.Column(db.String(13), nullable=False)
	NoHPRumah = db.Column(db.String(13))
	NoHPKantor = db.Column(db.String(13))
	Email = db.Column(db.String(64))
	PendidikanTerakhir = db.Column(db.String(128))
	StatusKompeten = db.Column(db.Boolean())
	StatusBekerja = db.Column(db.Boolean())
	idPekerjaan = db.Column(db.Integer,db.ForeignKey('Pekerjaan.idPekerjaan'))
	jurusan = db.Column(db.Integer,db.ForeignKey('Jurusan.idJurusan'))

	def __init__(self, nama, tempat, kelamin, bangsa, alamat, pos, nohp, rumah, kantor,email,pendidikan,statuskerja,pekerjaan,jurusan):
		self.NamaLengkap = nama
		self.TempatLahir = tempat
		self.JenisKelamin = kelamin
		self.Kebangsaan = bangsa
		self.alamat = alamat
		self.KodePos = pos
		self.NoHP = nohp
		self.NoHPRumah = rumah
		self.NoHPKantor = kantor
		self.Email = email
		self.PendidikanTerakhir = pendidikan
		self.StatusKompeten = False
		self.StatusBekerja = statuskerja
		self.bekerja = pekerjaan
		self.jurusan = jurusan

	def __repr__(self):
		return self.NamaLengkap

	def cekKompeten(self):
		return self.StatusKompeten

class Admin(db.Model):
	__tablename__ = 'Admin'
	kode = db.Column(db.Integer,primary_key=True,autoincrement=True)
	NamaLengkap = db.Column(db.String(64), nullable=False)
	Gelar = db.Column(db.String(16), nullable=False)
	Jabatan = db.Column(db.String(32))
	Username = db.Column(db.String(64),nullable=False)
	Password = db.Column(db.String(255),nullable=False)

	def __init__(self,nama,gelar,jabatan,username,password):
		self.NamaLengkap = nama
		self.Gelar = gelar
		self.jabatan = jabatan
		self.Username = username.upper()
		self.Password = generate_password_hash(password)

	def setPassword(self,password):
		self.password = generate_password_hash(password)

	def cekValid(self,password):
		return check_password_hash(self.Password,password)

class Pendaftaran(db.Model):
	__tablename__ = 'Pendaftaran'
	noPendaftaran = db.Column(db.Integer,primary_key=True,autoincrement=True)
	tanggal = db.Column(db.Date(),nullable=False)
	status = db.Column(db.Boolean(),nullable=False)
	asesi = db.Column(db.Integer,db.ForeignKey('Asesi.idAsesi'),nullable=False)
	admin = db.Column(db.Integer,db.ForeignKey('Admin.kode'),nullable=False)

	def __init__(self,asesi):
		self.tanggal = db.func.now()
		self.status = False
		self.asesi = asesi

	def setStatus(self,status):
		self.status = status

class Asesor(db.Model):
	__tablename__ = 'Asesor'
	idAsesor = db.Column(db.Integer,primary_key=True,autoincrement=True)
	Nama = db.Column(db.String(64), nullable=False)
	Gelar = db.Column(db.String(16),nullable=False)

	def __init__(self, nama, gelar):
		self.Nama = nama
		self.gelar = gelar

	def __repr__(self):
		return self.Nama

class Ujian(db.Model):
	__tablename__ = 'Ujian'
	idUjian = db.Column(db.Integer,primary_key=True,autoincrement=True)
	waktu = db.Column(db.DateTime(),nullable=False)
	tempat = db.Column(db.String(32))
	ruang = db.Column(db.String(32))
	status = db.Column(db.String(15))
	asesor = db.Column(db.Integer,db.ForeignKey('Asesor.idAsesor'))
	
	def __init__(self,waktu,tempat,ruang,asesor):
		self.waktu = waktu
		self.tempat = tempat
		self.ruang = ruang
		self.asesor = asesor



class DetailUjian(db.Model):
	__tablename__ = 'DetailUjian'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	nilai = db.Column(db.Integer,nullable=False)
	ujian = db.Column(db.Integer,db.ForeignKey('Ujian.idUjian'))
	asesi = db.Column(db.Integer,db.ForeignKey('Pendaftaran.noPendaftaran'))
	kuk = db.Column(db.Integer,db.ForeignKey('KUK.idKUK'))