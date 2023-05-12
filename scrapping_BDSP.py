from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

url = "https://bdsp2.pertanian.go.id/bdsp/id/indikator"
driver.get(url)


# select subsektor
subsektor_dropdown = Select(driver.find_element("id","subsektor"))
subsektor_dropdown.select_by_visible_text("Perkebunan")

# select komoditi
komoditi_dropdown = Select(driver.find_element("id","komoditas"))
komoditi_dropdown.select_by_visible_text("KELAPA SAWIT")

# select level
level_dropdown = Select(driver.find_element("id","level"))
level_dropdown.select_by_visible_text("Provinsi")


# select provinsi

select_element = WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.ID, 'prov')))
select = Select(select_element)
select.select_by_visible_text("Aceh")

# select kabupaten
# kab_dropdown = Select(driver.find_element_by_id("kab"))
# kab_dropdown.select_by_visible_text("Aceh")

# select tahun
TAwal_dropdown = Select(driver.find_element("id","tahunAwal"))
TAwal_dropdown.select_by_visible_text("1971")

TAwal_dropdown = Select(driver.find_element("id","tahunAkhir"))
TAwal_dropdown.select_by_visible_text("2023")

# click search button
search_box = driver.find_element("id", "search")

search_box.send_keys('ChromeDriver')

search_box.click()


# tbody = driver.find_element(By.XPATH,'//*[@id="example"]/tbody')
# wait up to 10 seconds for the element to be present
wait = WebDriverWait(driver, 100)

# define the element using its XPath selector
element_xpath = '//*[@id="example"]/tbody'

# wait until the element is present
element = wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
data = []

for tr in element.find_elements(By.XPATH, '//tr'):
    row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
    data.append(row)

print(data)

# Close the browser
driver.quit()


df = pd.DataFrame(data)
df.to_csv('Kelapa_sawit_Aceh.csv', index=False)


