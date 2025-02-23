from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# ChromeDriver'ın doğru yolunu ekleyin
chrome_driver_path = "C:\\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Sayfayı aç
driver.get("https://www.hepsiemlak.com/yildirim-millet-satilik")

# Sayfanın tamamen yüklenmesini bekle
wait = WebDriverWait(driver, 10)

try:
    # Verileri al
    fiyatlar = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list-view-price")))
    basliklar = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list-view-header")))
    size_list = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "celly.squareMeter.list-view-size")))

    # Verileri listelere ekle
    data = []
    for i in range(len(fiyatlar)):
        fiyat = fiyatlar[i].text.strip()
        baslik = basliklar[i].text.strip() if i < len(basliklar) else "Bilinmiyor"
        size = size_list[i].text.strip() if i < len(size_list) else "Bilinmiyor"

        data.append([baslik, fiyat, size])

    # Pandas DataFrame ile tablo oluştur
    df = pd.DataFrame(data, columns=["Başlık", "Fiyat", "Metrekare"])

    # Tabloyu yazdır
    print(df)

except Exception as e:
    print("Hata:", e)

# Tarayıcıyı kapat
driver.quit()


