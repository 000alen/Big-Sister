# Big-Sister
Descargar [raw_padron_rm/](https://drive.google.com/drive/folders/1Xm0ZDjFSqIOI98CFnCOqA5fOttcvZqf0?usp=sharing)

Descargar [raw_resultados_rm/](https://drive.google.com/drive/folders/1neTYxtrzMGfdBsvfTE4_Y8gezdAE4F5-?usp=sharing)

## Uso
Para ejecutar `BigSister` se debe ejecutar el siguiente comando `python -m BigSister`, o bien ejecutar `run.bat` o `run.sh` según corresponda.

## Objetivos
- Comparación con elecciones pasadas
- Muestreo de la participación dentro de la comuna

## To-do list
### Alen
- [ ] Geocoding
- [ ] Cartopy

### Juan Pablo
- [ ] Limpieza, formateo y extracción de datos relevantes de raw_resultados_rm

### Mixto
- [ ] Mapa de densidad probabilística

## Scripts
### `clean_raw_padron_rm.py`
Script que limpia y filtra `raw_padron_rm/`. Genera `databases/DCM/`.

### `clean_raw_resultados_rm_core.py`
Script que limpia y filtra `raw_resultados_rm/`.

### `clean_raw_resultados_rm_diputados.py`
Script que limpia y filtra `raw_resultados_rm/`.

### `clean_raw_resultados_rm_presidencial_1v.py`
Script que limpia y filtra `raw_resultados_rm/`.

### `clean_raw_resultados_rm_presidencial_2v.py`
Script que limpia y filtra `raw_resultados_rm/`.

## Bases de datos
### `comunas_rm.json`
Archivo `.json` que contiene los identificadores de las comunas de toda la Región Metropolitana con sus respectivos nombres.

### `raw_padron_rm/`

### `raw_resultados_rm/`

### `databases/DCM/`

### `databases/CCM/`
