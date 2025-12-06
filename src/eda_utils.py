import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set professional aesthetics for all plots
sns.set_theme(style="whitegrid", palette="viridis")

class EDAPlotter:
    """Utility class for generating standardized visualizations."""
    def __init__(self, df: pd.DataFrame):
        self.df = df
        
    def plot_univariate_distribution(self, column: str, bins: int = 30, title_suffix: str = "") -> None:
        """Plots the distribution of a single numerical feature."""
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[column].dropna(), kde=True, bins=bins, color='teal')
        plt.title(f'Distribution of {column.replace("_", " ").title()} {title_suffix}', fontsize=14)
        plt.xlabel(column.replace("_", " ").title(), fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.tight_layout()
        plt.savefig(f"../reports/figures/hist_{column}.png")
        plt.close()

    def plot_risk_by_category(self, x_col: str, y_col: str, sort: bool = True) -> None:
        """Plots the average metric (like Loss Ratio) by a categorical feature."""
        risk_df = self.df.groupby(x_col)[y_col].mean().reset_index()
        risk_df.columns = [x_col, 'mean_metric']
        
        if sort:
            risk_df = risk_df.sort_values(by='mean_metric', ascending=False)
            
        plt.figure(figsize=(12, 7))
        # Use color='teal' for consistency or stick to 'viridis' palette
        sns.barplot(x=x_col, y='mean_metric', data=risk_df, color=sns.color_palette("viridis")[0])
        
        plt.axhline(self.df[y_col].mean(), color='red', linestyle='--', linewidth=1, label=f'Overall Average {y_col.title()}')
        plt.legend()

        plt.title(f'Average {y_col.replace("_", " ").title()} by {x_col.replace("_", " ").title()}', fontsize=16)
        plt.xlabel(x_col.replace("_", " ").title(), fontsize=12)
        plt.ylabel(y_col.replace("_", " ").title(), fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f"../reports/figures/bar_{y_col}_vs_{x_col}.png")
        plt.close()


    def plot_correlation_heatmap(self, numerical_cols: list) -> None:
        """Generates a professional correlation heatmap."""
        plt.figure(figsize=(12, 10))
        corr = self.df[numerical_cols].corr(numeric_only=True)
        mask = np.triu(corr)
        
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f",
                    linewidths=.5, linecolor='black', mask=mask)
        
        plt.title("Correlation Matrix of Key Numerical Variables", fontsize=16)
        plt.tight_layout()
        plt.savefig(f"../reports/figures/correlation_matrix.png")
        plt.close()