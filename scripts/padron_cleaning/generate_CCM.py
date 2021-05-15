from geopy.geocoders import Nominatim
from csv import reader, writer
from pathlib import Path
from json import load

root = Path("../databases/OUT/DCM/")
out = Path("../databases/OUT/CCM/")
comunas_rm_path = Path("../databases/OUT/comunas_rm.json")

comunas_rm = load(open(comunas_rm_path, encoding="utf-8"))
geo_locator = Nominatim(user_agent="BigSister")

error = 0
successful = 0
for comuna in comunas_rm:
    print(f"Current comuna: {comuna}")
    dcm = reader(open(root / f"DCM_{comuna}.csv", encoding="utf-8"))
    ccm = writer(open(out / f"CCM_{comuna}.csv", "w", encoding="utf-8", newline=""))

    for dcm_row in dcm:
        address, comuna, mesa = dcm_row

        print(f"Current address: {address}")

        location = geo_locator.geocode(f"{address}, {comuna}, Region Metropolitana, Chile")
        if location:
            ccm.writerow([location.latitude, location.longitude, dcm_row[1::]])
            successful += 1
        else:
            error += 1

print(f"error: {error}, successful: {successful}")
