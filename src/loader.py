import pandas as pd
import numpy as np

class DataLoader:
    """Handles data ingestion, standardization, and type optimization."""
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    # In src/loader.py, modify the load_data method:

    # In src/loader.py

    def load_data(self) -> pd.DataFrame:
        """Loads data using the known pipe '|' delimiter."""
        # CRITICAL FIX: Explicitly set the pipe '|' as the delimiter (sep='|')
        # We also use the 'python' engine for better handling of potentially inconsistent lines
        try:
            self.df = pd.read_csv(
                self.filepath, 
                sep='|',                 # Use pipe as delimiter
                low_memory=False, 
                # on_bad_lines='skip'    # Use this if you have pandas 1.3+ to skip corrupted rows
            )
        except Exception as e:
            # Reverting to the old, less robust read method if the explicit one fails
            print(f"FATAL ERROR: Failed to load data with pipe delimiter: {e}. Check file encoding.")
            # If the pipe fails, the file might be corrupted or encoded strangely.
            self.df = pd.DataFrame() 
            
        return self.df

    def clean_column_names(self) -> pd.DataFrame:
        """Standardizes column names to snake_case."""
        self.df.columns = [
            col.strip().lower().replace(' ', '_').replace('.', '_').replace('-', '_')
            for col in self.df.columns
        ]
        return self.df

    def optimize_dtypes(self) -> pd.DataFrame:
        """Optimizes memory and ensures 'transactionmonth' is datetime."""
        # 1. Force TransactionMonth to datetime type first
        if 'transactionmonth' in self.df.columns:
            # Use format specified in the original data to ensure correct parsing
            # Assuming 'YYYY-MM-DD' or similar format, but coerce errors
            self.df['transactionmonth'] = pd.to_datetime(self.df['transactionmonth'], errors='coerce')

        # 2. Optimize other column types
        for col in self.df.select_dtypes(include='object').columns:
            # If the number of unique values is less than 50% of the total rows, convert to category
            if self.df[col].nunique() / len(self.df) < 0.5:
                self.df[col] = self.df[col].astype('category')
                
        # The TransactionMonth column is already processed above
        return self.df