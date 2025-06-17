import pandas as pd

df = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5],
    'country': ['Argentina', 'Brasil', 'Argentina', 'Chile', 'Brasil'],
    'amount': [100, 200, 50, 300, 150]
})

df.to_parquet('raw_sales.parquet', index=False)

