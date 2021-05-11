from BigSister import comunas_rm
from BigSister.utils import get_comuna_name


for identifier in comunas_rm:
    print(get_comuna_name(identifier))
