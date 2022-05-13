from alertMe import sendAlert
from accessConsulate import login, navigate, takeScreenshot
import time
import os

driver = login()
for i in range(6):
    if i == 5:
        message = navigate(driver, i)
    else:
        new_driver = navigate(driver, i)
    time.sleep(3)
name = takeScreenshot(new_driver)
sendAlert(name, message)
if message == "Al momento non ci sono date disponibili per il servizio richiesto":
    pass
else:
    sendAlert(name, message)

# Clean the folder of the screenshot
if os.path.exists(name):
  os.remove(name)
else:
  pass