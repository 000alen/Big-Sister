# Big-Sister
[Descargar PadronCSV](https://drive.google.com/drive/folders/1Xm0ZDjFSqIOI98CFnCOqA5fOttcvZqf0?usp=sharing)

## Uso
Para ejecutar `BigSister` se debe ejecutar el siguiente comando `python -m BigSister`, o bien ejecutar `run.bat` o `run.sh` según corresponda.

## `comunas_chile.json`
Archivo `.json` que contiene los identificadores de las comunas de todo Chile con sus respectivos nombres.

## `comunas_rm_json`
Archivo `.json` que contiene los identificadores de las comunas de toda la Región Metropolitana con sus respectivos nombres.

## `padron_rm.json`
Archivo `.json` que contiene la información de cada uno de los archivos `.csv` disponibles en el padrón de la Región Metropolitana. El formato de las entradas es el siguiente `identifier: [begin, end, page]`. Para obtener el nombre del archivo `.csv` correspondiente se usa el siguiente formato `f"{identifier}__{begin}__{end}_p{page}.csv"`.
