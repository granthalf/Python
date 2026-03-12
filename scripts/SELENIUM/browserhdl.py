import json
import sys
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

# Vérification des arguments
if len(sys.argv) < 2:
    print("Usage : python script.py <url>")
    sys.exit(1)

// change the default url you want to be used
if not sys.argv[1].strip():
	urlweb = "https://www.changeyoururlhere.com"
else:
	urlweb = sys.argv[1]

options = Options()
options.add_argument("--start-maximized")

// Driver available here: https://developer.microsoft.com/fr-fr/microsoft-edge/tools/webdriver/
service = Service("C:/Users/firstname.name/Documents/edgeheadless/msedgedriver.exe")

driver = webdriver.Edge(service=service, options=options)

driver.get(urlweb)
print("TITLE=    " + driver.title)

# Récupération des cookies
cookies = driver.get_cookies()

# Export dans un fichier texte
with open("cookies-recovery.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(cookies, indent=4))

# Filtrer uniquement les cookies HttpOnly
httponly_cookies = [c for c in cookies if c.get("httpOnly")]

# Export dans un fichier texte
with open("cookies-httponly.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(httponly_cookies, indent=4))

driver.quit()




