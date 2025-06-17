SELECT
  order_id,
  country,
  amount
FROM read_parquet('raw_sales.parquet')

