# install package pip install phonenumbers
import phonenumbers
from test import number

from phonenumbers import geocoder # geocoder function of phonenumbers

ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber, "en"))
# To know service provider
from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber,"en"))

