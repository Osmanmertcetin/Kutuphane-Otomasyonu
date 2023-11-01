import pypyodbc

db = pypyodbc.connect('Driver={SQL Server};'
                      'Server=Server Adınız;'
                      'Database=Database Adınız;'
                      'Trusted_Connection=yes;')

imlec = db.cursor()

imlec.execute('create table kayıtlı_kişiler(id int identity,kullanıcı_adı varchar(20),şifre varchar(20),üyelik_tipi varchar(10),ad varchar(20),soyad varchar(20),tel_no varchar(20),adres varchar(50),eposta varchar(25),üyelik_tarihi varchar(10),doğum_tarihi varchar(10))')
imlec.execute('create table kitaplar(kitap_id int identity, kitap_adı varchar(25),yazar varchar(25),basım_evi varchar(25),basım_yılı varchar(5),toplam_adet int,mevcut_adet int)')
imlec.execute('create table kitap_geçmişi(kitap_id int,kullanıcı_id int,ad varchar(20),soyad varchar(20),kitap_adı varchar(25),alma_tarihi varchar(10),teslim_tarihi varchar(10))')
imlec.execute('INSERT INTO kayıtlı_kişiler (kullanıcı_adı,şifre,üyelik_tipi) VALUES(?,?,?)',("admin",123,"yönetici"))
db.commit()

db.close()