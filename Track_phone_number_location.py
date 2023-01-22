#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phonenumbers

import folium



# In[4]:


from test import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

YourLocation = geocoder.description_for_number(ch_nmber, "en")


from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))



Key = "0d1ac0da26004d6bb065912d9e302a47"

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(YourLocation)

results = geocoder.geocode(query)
print(results)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
                   
folium.Marker([lat, lng], popup= YourLocation).add_to((myMap))

#save map in html file
                   
myMap.save("mylocation.html")


 


# In[ ]:




