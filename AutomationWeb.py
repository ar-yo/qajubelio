from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Lokasi ChromeDriver Di Lokall
driver_path = 'C:/chromedriver/chromedriver.exe'

# Inisialisasi Chrome WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
# Navigasi ke halaman login Jubelio
driver.get('https://app.jubelio.com/login')

# Temukan elemen input email
email_input = driver.find_element(By.NAME, 'email')

# Isi input email dengan alamat email pengguna
email_input.send_keys('qa.rakamin.jubelio@gmail.com')

# Temukan elemen input password
password_input = driver.find_element(By.NAME, 'password')

# Isi input password dengan kata sandi pengguna
password_input.send_keys('Jubelio123!')

# Tekan tombol "Enter" untuk login
password_input.send_keys(Keys.RETURN)


# Tunggu halaman beranda dimuat user menu
driver.implicitly_wait(10)
dashboard_element = driver.find_element(By.ID, 'user_menu')

if dashboard_element : 
    print("success login...")
   # Navigasi ke halaman pengaturan stok persediaan Jubelio
driver.get("https://app.jubelio.com/home/inventory")

# Temukan elemen yang berisi teks "Penyesuaian Persediaan"
button_element = driver.find_element(By.XPATH, '//span[text()="Penyesuaian Persediaan"]')

# Klik tombol "Penyesuaian Persediaan"
button_element.click()

# Temukan elemen input dengan placeholder "Scan"
input_element = driver.find_element(By.XPATH, '//input[@placeholder="Scan"]')

# Isi input "Scan" dengan teks "LaptopGamingNitro"
input_element.send_keys("LaptopGamingNitro")

# Temukan tombol "Scan"
scan_button = driver.find_element(By.XPATH, '//button[contains(@class, "ladda-button")]//span[text()="Scan"]')

# Klik tombol "Scan"
scan_button.click()

# Temukan tombol "Simpan"
simpan_button = driver.find_element(By.XPATH, '//button[contains(@class, "ladda-button")]//span[text()="Simpan"]')

# Klik tombol "Simpan"
simpan_button.click()

# Tutup browser
driver.quit()
