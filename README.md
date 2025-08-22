# Mini ETL con Python (WIP)

Pequeño pipeline ETL para consolidar archivos CSV desde múltiples fuentes, aplicar normalización y validaciones básicas, y generar un dataset limpio listo para análisis o BI.

## Objetivos
- Unificar varias fuentes CSV en un solo dataset.
- Estandarizar nombres de columnas y formatos.
- Aplicar validaciones simples (filas vacías, tipos básicos).
- Generar un archivo limpio con timestamp para trazabilidad.

## Estructura del proyecto
mini-etl-python/
├─ etl.py
├─ data/
│ ├─ raw/ # Coloca aquí tus CSV de origen
│ └─ clean/ # Salidas del ETL con timestamp
└─ README.md


## Requisitos
- Python 3.9+ (recomendado)
- Paquetes: pandas

Instalación rápida:
pip install pandas


## Uso rápido
1) Coloca uno o más archivos `.csv` en `data/raw/`.
2) Ejecuta el pipeline:
python etl.py

3) Revisa el archivo generado en `data/clean/` con nombre `dataset_final_YYYYMMDD_HHMMSS.csv`.

Si no hay archivos en `data/raw/`, el script te avisará.

## Funcionalidades
- [x] Consolidación de múltiples CSV
- [x] Normalización de nombres de columnas (minúsculas, guiones bajos)
- [x] Validaciones básicas (remover filas vacías en columna clave si existe)
- [x] Exportar dataset limpio con timestamp
- [ ] Logs detallados de calidad de datos
- [ ] Esquema de tipos por columna
- [ ] Tests unitarios básicos (pytest)
- [ ] Dockerfile para ejecución reproducible

## Configuración
- Directorios:
  - `RAW_DIR = data/raw`
  - `CLEAN_DIR = data/clean`

Ajusta estos valores en `etl.py` si lo necesitas.

## Roadmap
- Añadir reporte de calidad (conteo de nulos, duplicados, tipos).
- Permitir mapeo de tipos desde YAML/JSON.
- Integrar validaciones con Great Expectations (opcional).
- Publicar dataset final como Excel y/o parquet.
- Automatización con cron/Task Scheduler.

## Licencia
MIT (o la que prefieras)

## Estado
WIP — En desarrollo activo.
