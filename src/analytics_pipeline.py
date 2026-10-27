import pandas as pd
import numpy as np

def generate_sample_data(n_records=1000):
    np.random.seed(42)
    data = {
        'order_id': [f"ORD-{1000 + i}" for i in range(n_records)],
        'product_category': np.random.choice(['Agri-Chemicals', 'Fertilizers', 'Seeds', 'Packaging'], n_records),
        'quantity_ordered': np.random.randint(10, 500, n_records),
        'lead_time_days': np.random.normal(7, 2, n_records).round(1),
        'delivery_status': np.random.choice(['Delivered', 'In-Transit', 'Delayed'], n_records, p=[0.8, 0.15, 0.05])
    }
    return pd.DataFrame(data)

def analyze_supply_chain(df):
    print("=== Supply Chain & Logistics Analytics Summary ===")
    print(f"Total Transactions Analyzed: {len(df)}")
    category_summary = df.groupby('product_category').agg({
        'quantity_ordered': ['sum', 'mean'],
        'lead_time_days': 'mean'
    }).round(2)
    print("\nCategory Performance Matrix:")
    print(category_summary)
    
    delayed_rate = (df['delivery_status'] == 'Delayed').mean() * 100
    print(f"\nOverall Delay Rate: {delayed_rate:.2f}%")
    return category_summary

if __name__ == '__main__':
    df = generate_sample_data(2500)
    summary = analyze_supply_chain(df)
    print("\nETL pipeline completed successfully.")
