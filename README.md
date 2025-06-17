# DBT

DBT instalado
	pip install dbt-core



Adaptadores

	pip install dbt-duckdb (parquet en localhost)

## Project init

	dbt init my_dbt_duckdb_project
	(elegir opción duckdb)

## Profile dbt

en .dbt/profiles.yml

my_dbt_duckdb_project:
  target: parquetduckdb
  outputs:
    parquetduckdb:
      type: duckdb
      path: /Users/hordia/dev/courses/dbt-demo-parquet/mi_duckdb.db
      # alternativa en memoria RAM: path: ':memory:'
      threads: 1

## Observación
1️⃣ models/staging/stg_sales.sql
sql
Copy
Edit
SELECT
  order_id,
  country,
  amount
FROM read_parquet('raw_sales.parquet')

IMPORTANTE: DuckDB puede leer el parquet directo desde el path sin definir fuentes.

lee el archivo parquet directamente como input


# Ejecutar

cd my_dbt_duckdb_project

	dbt debug               # verifica configuraciones
	dbt run                 # ejecuta los modelos
	dbt build               # (opcional, incluye tests, por ejemplo para calidad)

