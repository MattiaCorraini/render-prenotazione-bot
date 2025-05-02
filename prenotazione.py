from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 30)

try:
    driver.get("https://prenotabiblio.sba.unimi.it/portalePlanning/biblio/prenota/calendario/92/25")

    durata_select_elem = wait.until(EC.element_to_be_clickable((By.ID, "durata")))
    select = Select(durata_select_elem)
    select.select_by_visible_text("1 ora")
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", durata_select_elem)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", durata_select_elem)

    giorno_5 = wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[@role='button' and contains(@aria-label, '5') and contains(@aria-description, 'selezionabile')]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", giorno_5)
    driver.execute_script("arguments[0].click();", giorno_5)

    prenota_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-cypress='Prenota']")))
    driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", prenota_btn)
    driver.execute_script("arguments[0].click();", prenota_btn)

    fascia_oraria = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[contains(@class, 'disponibile') and starts-with(@aria-label, '09:00')]"
    )))
    driver.execute_script("arguments[0].click();", fascia_oraria)

    inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input")))

    inputs[0].clear()
    inputs[0].send_keys("RSSMRA75T90A562S")
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", inputs[0])
    driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", inputs[0])

    inputs[1].clear()
    inputs[1].send_keys("Mario Rossi")
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", inputs[1])
    driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", inputs[1])

    inputs[2].clear()
    inputs[2].send_keys("mario.rossi@example.com")
    driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", inputs[2])
    driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", inputs[2])

    time.sleep(5)
finally:
    driver.quit()
