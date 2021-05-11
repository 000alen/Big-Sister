import pathlib
import json

root = pathlib.Path(".")
comunas_chile_path = root.parent / "comunas_chile.json"
comunas_rm_path = root.parent / "comunas_rm.json"
padron_rm_json_path = root.parent / "padron_rm.json"

comunas_chile = json.load(open(comunas_chile_path))
comunas_rm = json.load(open(comunas_rm_path))
padron_rm_json = json.load(open(padron_rm_json_path))
