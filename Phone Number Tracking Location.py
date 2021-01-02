# install package pip install phonenumbers
import phonenumbers
from test import number

from phonenumbers import geocoder # geocoder function of phoneying

ch_nmber = phonenumbers.parse(number,"CH") # variable = package phone number with parse for parameter C is for country and H for history
print(geocoder.description_for_number(ch_nmber, "en")) # geocoder connect with number description with parameter with variable and language
# To know service provider
from phonenumbers import carrier # carrier use for service provider name
service_nmber = phonenumbers.parse(number, "RO") # RO stand for roaming
print(carrier.name_for_number(service_nmber,"en")) # call carrier function and language name



