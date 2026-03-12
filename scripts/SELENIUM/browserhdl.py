import json
import sys
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

// Reminder:
// CMD, go to Python Dir (in case of PATH issue)
// python -m pip list

// Install SELENIUM:
// pip install selenium

# Check parameter
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

# Easy, we get cookies
cookies = driver.get_cookies()

# Export them into a text file
with open("cookies-recovery.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(cookies, indent=4))

# Filter ony HttpOnly cookies
httponly_cookies = [c for c in cookies if c.get("httpOnly")]

# Export into a text file
with open("cookies-httponly.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(httponly_cookies, indent=4))

driver.quit()




