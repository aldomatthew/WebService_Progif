from flask import Flask, redirect, url_for,render_template,request,jsonify
from flask_dance.contrib.google import make_google_blueprint, google
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
#DATA DUMMY
DaftarProyek = [
    {
		"Nama Proyek": "PercepataninfrastrukturKawasanEkonomiKhususLhokseumawe",
		"Lokasi": "Aceh",
		"Sektor": "Kawasan",
		"Pulau":"Sumatera",
		"Latitude": "4.695135",
		"Longtitude": "96.749397",
        "Nilai_Proyek": "9Trilyun"
	},
    {
    		"Nama Proyek": "PercepataninfrastrukturKawasanEkonomiKhususLhokseumawe",
    		"Lokasi": "Aceh",
    		"Sektor": "Kawasan",
    		"Pulau":"Sumatera",
    		"Latitude": "4.695135",
    		"Longtitude": "96.749397",
            "Nilai_Proyek": "9Trilyun"
    },
	{
		"Nama Proyek": "PembangunanJaringanIrigasiDiLhokGuci",
		"Lokasi": "Aceh",
		"Sektor": "Irigasi",
		"Pulau":"Sumatera",
		"Latitude": "4.695135",
		"Longtitude": "96.749397",
        "Nilai_Proyek": "1Trilyun"
	},
	{
		"Nama Proyek": "PembangunanJaringanIrigasiDIJamboAyeKanan",
		"Lokasi": "Aceh",
		"Sektor": "Irigasi",
		"Pulau": "Sumatera",
		"Latitude": "4.695135",
		"Longtitude": "96.749397",
        "Nilai_Proyek":"800Milyar"
	},
    {
		"Nama Proyek": "PenyelenggaraanKeretaApiRingan/LightRailTransit(LRT)TerintegrasidiWilayahJakarta",
		"Lokasi": "Bogor",
		"Sektor": "Kereta Api",
		"Pulau": "Jawa",
		"Latitude": "Kereta",
		"Longtitude": "Jawa",
        "Nilai_Proyek": "856Milyar"
	},
	{
		"Nama Proyek": "PembangunanRumahSusunPembangunan2322unitRumahSusunSewadiPasarMinggu(DKIJakarta)",
		"Lokasi": "DKI Jakarta",
		"Sektor": "Perumahan",
		"Pulau": "Jawa",
		"Latitude": "-6.21462",
		"Longtitude": "106.84513",
        "Nilai_Proyek": "123Milyar"
	},
	{
		"Nama Proyek": "National Capital Integrated Coastal Development (NCICD) Tahap A",
		"Lokasi": "DKI Jakarta",
		"Sektor": "Tanggul Laut",
		"Pulau": "Jawa",
		"Latitude": "-6.21462",
		"Longtitude": "106.84513",
        "Nilai_Proyek": "600Trilyun"
	},

    {
      "Nama Proyek": "Mass Rapid Transit (MRT) Jakarta Koridor North-South",
      "Lokasi": "DKI Jakarta",
      "Sektor": "Kereta",
      "Pulau": "Jawa",
      "Latitude": "-6.21462",
      "Longtitude": "106.84513",
      "Nilai_Proyek": "890Milyar"
    },
    {
      "Nama Proyek": "Mass Rapid Transit (MRT) Jakarta Koridor East-West",
      "Lokasi": "DKI Jakarta",
      "Sektor": "Kereta",
      "Pulau": "Jawa",
      "Latitude": "-6.21462",
      "Longtitude": "106.84513",
      "Nilai_Proyek": "120Milyar"
    },
    {
      "Nama Proyek": "Kereta Api Jakarta-Surabaya",
      "Lokasi": "DKI Jakarta",
      "Sektor": "Kereta",
      "Pulau": "Jawa",
      "Latitude": "-6.21462",
      "Longtitude": "106.84513",
      "Nilai_Proyek": "234M"
    },
    {
      "Nama Proyek": "Kereta api ekspres SHIA (Soekarno Hatta-Sudirman)",
      "Lokasi": "DKI Jakarta",
      "Sektor": "Kereta",
      "Pulau": "Jawa",
      "Latitude": "-6.21462",
      "Longtitude": "106.84513",
      "Nilai_Proyek": "150M"
    },
    {
      "Nama Proyek": "Jalan Tol Ulujami-Tanah Abang 8",
      "Lokasi": "7km (bagian dari 6 ruas tol DKI Jakarta)",
      "Sektor": "DKI Jakarta",
      "Pulau": "Jawa",
      "Latitude": "Jawa",
      "Longtitude": "-6.21462",
      "Nilai_Proyek": "500M"
    },
    {
      "Nama Proyek": "Jalan Tol Sunter-Pulo Gebang 9",
      "Lokasi": "44km (bagian dari 6 ruas tol DKI Jakarta)",
      "Sektor": "DKI Jakarta",
      "Pulau": "Jalan",
      "Latitude": "Jawa",
      "Longtitude": "-6.21462",
      "Nilai_Proyek": "400M"
    }
]

app.secret_key = "supersekrit"
blueprint = make_google_blueprint(
    client_id="826481383940-t366qv38g4t917spphfec9vvl4e58ps1.apps.googleusercontent.com",
    client_secret="vKoL5IKtaB6ShkqD-CZ9KHfn",
    scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
    ]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    return redirect("home")

@app.route("/home")
def register():
    return render_template("index.html")

@app.route("/dokumentasi")
def ujicoba():
    return render_template("documentation.html")#Masih belum ada

#############GET REQUEST #################
#Succes - 200
@app.route("/daftarproyek", methods=['GET'])
def returnAll():
    return jsonify({"DaftarProyek": DaftarProyek })

#Succes - 200
@app.route("/daftarproyek/Sektor/<string:Sektor>", methods=['GET'])
def returnSektor(Sektor):
    sektor_search = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek["Sektor"] == Sektor] #Searching di Dalam list DaftarProyek
    return jsonify({'DaftarProyek': sektor_search})

#Succes - 200
@app.route("/daftarproyek/Pulau/<string:Pulau>",endpoint="pulau/index",methods=['GET'])
def returnPulau(Pulau):
    pulau_search = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek["Pulau"] == Pulau]
    return jsonify({'DaftarProyek': pulau_search})

#Succes - 200
@app.route("/daftarproyek/SektorPulau/<string:Sektor>/<string:Pulau>",endpoint="pulausektor/index" ,methods=['GET'])
def returnSektorPulau(Sektor,Pulau):
    sektor_pulau_search = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek["Pulau"] == Pulau and DaftarProyek["Sektor"] == Sektor]
    return jsonify({'DaftarProyek': sektor_pulau_search})

#Succes - 200
@app.route("/daftarproyek/SektorLokasi/<string:Sektor>/<string:Lokasi>",endpoint="sektorlokasi/index" ,methods=['GET'])
def returnPulauLokasi(Sektor,Lokasi):
    sektor_lokasi_search = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek["Sektor"] == Sektor and DaftarProyek["Lokasi"] == Lokasi]
    return jsonify({'DaftarProyek': sektor_lokasi_search})

#Success -200
@app.route("/daftarproyek/PulauNilaiProyek/<string:Pulau>/<string:Nilai_Proyek>", endpoint="pulaunilai/index", methods=['GET'])
def returnPulauNilai(Pulau,Nilai_Proyek):
    pulau_nilaiproyek = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek["Pulau"] == Pulau and DaftarProyek["Nilai_Proyek"] == Nilai_Proyek]
    return jsonify({'DaftarProyek': pulau_nilaiproyek})
#Success -200
@app.route("/daftarproyek/LokasiNilaiProyek/<string:Lokasi>/<string:Nilai_Proyek>", endpoint="lokasinilai/index", methods=['GET'])
def returnLokasiNilai(Lokasi,Nilai_Proyek):
    lokasi_nilaiproyek = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek["Lokasi"] == Lokasi and DaftarProyek["Nilai_Proyek"] == Nilai_Proyek]
    return jsonify({'DaftarProyek': lokasi_nilaiproyek})

#succes - 200
@app.route("/daftarproyek/SektorNilaiProyek/<string:Sektor>/<string:Nilai_Proyek>", endpoint="sektornilai/index", methods=['GET'])
def returnSektorNilai(Sektor,Nilai_Proyek):
    sektor_nilaiproyek = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek["Sektor"] == Sektor and DaftarProyek["Nilai_Proyek"] == Nilai_Proyek]
    return jsonify({'DaftarProyek': sektor_nilaiproyek})

##############POST REQUEST####################
#Not Succes - 404 Bad Request
@app.route("/daftarproyek/isiproyek", methods=['POST'])
def addProyek():
    daftar_proyek = {
                     "Nama Proyek" : request.json['Nama Proyek'],
                     "Lokasi" : request.json['Lokasi'],
                     "Sektor" : request.json['Sektor'],
                     "Pulau" : request.json['Pulau'],
                     "Latitude" : request.json['Latitude'],
                     "Longtitude" : request.json['Longtitude'],
                     "Nilai_Proyek" : request.json['Nilai_Proyek']
    }
    DaftarProyek.append(daftar_proyek)
    return jsonify({"daftar_proyek": daftar_proyek }),201
###########PUT REQUEST############
#Not Succes - 404 Bad Request
@app.route('/daftarproyek/baru/<string:NamaProyek>',methods=['PUT'])
def updateProyek(NamaProyek):
    proyek1 = [DaftarProyek for DaftarProyek in DaftarProyek if DaftarProyek['Nama Proyek'] == NamaProyek]
    proyek1[0]['Nama Proyek'] = request.json.get('Nama Proyek',proyek1[0]['Nama Proyek'])
    return jsonify({'DaftarProyek':proyek1[0]})

##########DELETE REQUEST################
#Succes
@app.route("/daftarproyek/deleteLokasi/<string:Lokasi>", methods=['DELETE'])
def delProyek(Lokasi):
    proyek = [proyek for proyek in DaftarProyek if proyek["Lokasi"] == Lokasi]
    DaftarProyek.remove(proyek[0])
    return jsonify({'hasil':proyek})
#succes
@app.route("/daftarproyek/deleteSektor/<string:Sektor>", methods=['DELETE'])
def delSektork(Sektor):
    proyek_ = [proyek_ for proyek_ in DaftarProyek if proyek_["Sektor"] == Sektor]
    DaftarProyek.remove(proyek_[0])
    return jsonify({'hasil':proyek_})
#succes
@app.route("/daftarproyek/deleteSektorLokasi/<string:Sektor>/<string:Lokasi>", endpoint="delete/sektorlokasi", methods=['DELETE'])
def delSektork(Sektor,Lokasi):
    proyek_ = [proyek_ for proyek_ in DaftarProyek if proyek_["Sektor"] == Sektor and proyek_["Lokasi"] == Lokasi]
    DaftarProyek.remove(proyek_[0])
    return jsonify({'hasil':proyek_})
#succes
@app.route("/daftarproyek/deleteNamaProyek/<string:NamaProyek>", endpoint="delete/namaproyek", methods=['DELETE'])
def delSektork(NamaProyek):
    proyek_ = [proyek_ for proyek_ in DaftarProyek if proyek_["Nama Proyek"] == NamaProyek]
    DaftarProyek.remove(proyek_[0])
    return jsonify({'hasil':proyek_})

if __name__ == "__main__":
    app.run()

#https:login/google/authorized
