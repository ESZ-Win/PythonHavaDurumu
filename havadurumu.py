#Bu Program Emir Salih Zümrüt tarafından yazılmıştır
#Bazı sorunları çözmede chatgpt den yardım aldım.
import tkinter as tk
from PIL import ImageTk, Image
import requests

# Hava Durumu Bilgilerini Almak İçin Gerekli değişkenler
key = ""
url = "https://api.openweathermap.org/data/2.5/weather"
iconu = "https://openweathermap.org/img/wn/{}@2x.png"

# Hava Durumu Almak İçin Fonksiyon
def DurumAl(sehir):
    parametre = {'q': sehir, 'appid': key, 'lang': 'tr'}
    veri = requests.get(url, params=parametre).json()
    if veri:
        sehir = veri['name'].capitalize()
        ulke = veri['sys']['country']
        sıcak = int(veri['main']['temp'] - 273.15)
        icon = veri['weather'][0]['icon']  # İkon kodunu al
        description = veri['weather'][0]['description']
        hız = veri['wind']['speed']
        nem = veri['main']['humidity']
        return (sehir, ulke, sıcak, icon, description,hız,nem)

def Main():
    sehir = sehirs.get()
    hava = DurumAl(sehir)
    if hava:
        yerbilgiLabel['text'] = '{},{}'.format(hava[0], hava[1])
        sıcaklıkLabel['text'] = '{} C'.format(hava[2])
        durumLabel['text'] = "Hava Durumu: {}".format(hava[4])
        hızLabel['text'] = "Rüzgar Hızı: {}".format(hava[5])
        nemLabel['text'] = "Nem: {}".format(hava[6])
        #İcon işlemlei
        icon_url = iconu.format(hava[3])  # İkon kodunu URL'ye yerleştir
        icon_image = Image.open(requests.get(icon_url, stream=True).raw)
        icona = ImageTk.PhotoImage(icon_image)
        iconLabel.configure(image=icona)
        iconLabel.image = icona  # Referansı sakla

# Uygulamanın Ana Hatları
program = tk.Tk()
program.geometry("300x500")
program.resizable(False, False)  # Boyutu Değiştirilemez yapan komut
program.title("Hava Durumu Uygulaması")

# Bilgi Alma
sehirs = tk.Entry(program, justify="center")  # Yazıyı merkeze aldık (justify=center)
sehirs.pack(fill=tk.BOTH, ipady=10, padx=18, pady=5)

# Arama Butonu
aramaLabel = tk.Button(program, text="Arama", font=("Arial", 15), command=Main)
aramaLabel.pack(fill=tk.BOTH, ipady=7, padx=20)

# İkon
iconLabel = tk.Label(program)
iconLabel.pack()

# Şehir ve Ülke Bilgileri
yerbilgiLabel = tk.Label(program, font=("Arial", 15))
yerbilgiLabel.pack()

# Sıcaklık Bilgisi
sıcaklıkLabel = tk.Label(program, font=("Arial", 15))
sıcaklıkLabel.pack()

# Durum Bilgisi Açık Kapalı vesaire
durumLabel = tk.Label(program, font=("Arial", 15))
durumLabel.pack()
#Rüzgar Hızı
hızLabel =  tk.Label(program, font=("Arial", 15))
hızLabel.pack()
#Nem
nemLabel = tk.Label(program,font=("Arial",15))
nemLabel.pack()
program.mainloop()
