import requests

URL = "https://excel-sheet-splitter-nwfuusmt5cakadaupkfxrl.streamlit.app/"

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print("✅ Uygulama aktif, Keep-Alive başarılı!")
    else:
        print(f"⚠️ Bağlantı başarısız! Hata Kodu: {response.status_code}")
except Exception as e:
    print(f"❌ Hata oluştu: {e}")
