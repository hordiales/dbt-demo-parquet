# DBT

DBT instalado
	pip install dbt-core



Adaptadores

	pip install dbt-duckdb (parquet en localhost)

## Project init

	dbt init my_dbt_duckdb_project
	(elegir opción duckdb)


# Ejecutar

	dbt debug               # verifica configuraciones
	dbt seed                # sube raw_sales a DB (ingestar tabla desde csv)
	dbt run                 # ejecuta los modelos
	dbt build               # (opcional, incluye tests, por ejemplo para calidad)

