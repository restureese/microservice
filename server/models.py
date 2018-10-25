from server import db
from werkzeug.security import generate_password_hash, check_password_hash



class Skema(db.Model):
	__tablename__ = 'Skema'
	idSkema = db.Column(db.Integer,primary_key=True)
	Nama = db.Column(db.String(128),nullable=False)

	def __init__(self,id,nama,kompetensi):
		self.idSkema = id
		self.Nama = nama
		self.kompetensi = kompetensi

	def __repr__(self):
		return self.idSkema


class UjiKompetensi(db.Model):
	__tablename__ = 'UjiKompetensi'
	kodeUnit = db.Column(db.String(128),primary_key=True)
	judulUnit = db.Column(db.String(128),nullable=False)
	Skema = db.Column(db.Integer,db.ForeignKey('Skema.idSkema'))
	def __init__(self, kode,judul,Skema):
		self.kodeUnit = kode
		self.judulUnit = judul
		self.Skema = Skema

	def __repr__(self):
		return self.kodeUnit



class ElemenKompetensi(db.Model):
	__tablename__ = 'ElemenKompetensi'
	idElemen = db.Column(db.Integer, primary_key=True,autoincrement=True)
	Nama = db.Column(db.String(128), nullable=False)
	ujikompetensi = db.Column(db.String(128),db.ForeignKey('UjiKompetensi.kodeUnit'))


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
	StatusBekerja = db.Column(db.Boolean())
	NamaPerusahaan = db.Column(db.String(128), nullable=False)
	Jabatan = db.Column(db.String(128))
	AlamatPerusahaan = db.Column(db.String(255))
	KodePosPerusahaan = db.Column(db.String(8))
	NoTeleponPerusahaan = db.Column(db.String(13))
	NoFaxPerusahaan = db.Column(db.String(32))
	EmailPerusahaan = db.Column(db.String(64))
	Skema = db.Column(db.Integer,db.ForeignKey('Skema.idSkema'))

	def __init__(self, nama, tempat, kelamin, bangsa, alamat, pos, nohp, rumah, kantor,email,pendidikan,statuskerja,pekerjaan,Skema):
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
		self.Skema = Skema

	def __repr__(self):
		return self.NamaLengkap

	def cekKompeten(self):
		return self.StatusKompeten

	def setDataPerusahaan(self,nama, jabatan, alamat, pos,telepon, fax, email):
		self.NamaPerusahaan = nama
		self.Jabatan = jabatan
		self.AlamatPerusahaan = alamat
		self.KodePosPerusahaan = pos
		self.NoTeleponPerusahaan = telepon
		self.NoFaxPerusahaan = fax
		self.EmailPerusahaan = email

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
	Tanggal = db.Column(db.Date(),nullable=False)
	Status = db.Column(db.Boolean(),nullable=False)
	asesi = db.Column(db.Integer,db.ForeignKey('Asesi.idAsesi'),nullable=False)
	admin = db.Column(db.Integer,db.ForeignKey('Admin.kode'),nullable=False)

	def __init__(self,asesi):
		self.tanggal = db.func.now()
		self.Status = False
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
	ujian = db.Column(db.Integer,db.ForeignKey('Ujian.idUjian'))
	asesi = db.Column(db.Integer,db.ForeignKey('Pendaftaran.noPendaftaran'))

class NilaiUjian(db.Model):
	__tablename__ = 'NilaiUjian'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	asesi = db.Column(db.Integer,db.ForeignKey('DetailUjian.asesi'))
	kuk = db.Column(db.Integer,db.ForeignKey('KUK.idKUK'))
	nilai = db.Column(db.Integer,nullable=False)
	bukti = db.Column(db.String(128))
	status = db.Column(db.String(128))