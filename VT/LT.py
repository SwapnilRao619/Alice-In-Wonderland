import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
import tkinter as tk
from tkinter import messagebox
import webbrowser

def generate_map():
    key = "1257afda104c4938af67f36ead1d2242"
    number = entry.get()

    try:
        check_number = phonenumbers.parse(number)
        number_location = geocoder.description_for_number(check_number, "en")
        service_provider = carrier.name_for_number(check_number, "en")

        geocoder_obj = OpenCageGeocode(key)
        query = str(number_location)
        results = geocoder_obj.geocode(query)
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        map_location = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=number_location).add_to(map_location)
        map_location.save("mylocation.html")
        webbrowser.open("mylocation.html")

        messagebox.showinfo("Success", f"Phone Number Location: {number_location}\nService Provider: {service_provider}\nLatitude: {lat}\nLongitude: {lng}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Phone Number Location Tracker")

label = tk.Label(root, text="Enter a phone number with the country code:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate Map", command=generate_map)
button.pack()

service_provider_label = tk.Label(root, text="Service Provider:")
service_provider_label.pack()

latitude_label = tk.Label(root, text="Latitude:")
latitude_label.pack()

longitude_label = tk.Label(root, text="Longitude:")
longitude_label.pack()

root.mainloop()