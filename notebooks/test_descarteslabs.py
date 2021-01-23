import descarteslabs as dl
import matplotlib.pyplot as plt
import my_secrets

DESCARTESLABS_CLIENT_ID = my_secrets.getClientID()
DESCARTESLABS_CLIENT_SECRET = my_secrets.getClientSecret()

matches = dl.places.find('new-mexico_taos')
print(matches)