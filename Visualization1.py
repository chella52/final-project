import matplotlib.pyplot as plt
import pandas as pd


class SalesAnalysis:
    """
    Class for performing sales analysis and visualization.
    """

    def __init__(self, df):
        """
        Initializes the SalesAnalysis object with the provided DataFrame.

        Args:
            df (pandas.DataFrame): DataFrame containing sales data.
        """
        self.df = df

    def total_revenue_by_region_and_sales_channel(self):
        """
        Plots the total revenue by region and sales channel.
        """
        # Step 1: Group the data by region
        grouped = self.df.groupby('Region')

        # Step 2: Calculate total revenue for online and offline sales for each region
        total_revenue = {region: group.groupby('SalesChannel')['TotalRevenue'].sum() for region, group in grouped}

        # Step 3: Plot the bar chart for total revenue of online and offline sales for each region
        regions = list(total_revenue.keys())
        offline_revenue = [total_revenue[region].get('Offline', 0) for region in regions]
        online_revenue = [total_revenue[region].get('Online', 0) for region in regions]
        x = range(len(regions))

        fig, ax = plt.subplots(figsize=(12, 6))
        bar_width = 0.35
        ax.bar(x, offline_revenue, width=bar_width, label='Offline')
        ax.bar([i + bar_width for i in x], online_revenue, width=bar_width, label='Online')

        ax.set_xlabel('Region')
        ax.set_ylabel('Total Revenue')
        ax.set_title('Total Revenue by Region and Sales Channel')
        ax.set_xticks([i + bar_width/2 for i in x])
        ax.set_xticklabels(regions, rotation=45)
        ax.legend()

        plt.tight_layout()
        plt.show()

    def top_item_types_by_region(self):
        """
        Plots the top 5 item types sold for each region.
        """
        # Step 1: Group the data by region
        grouped = self.df.groupby('Region')

        # Step 4: Plot the top 5 item types sold for each region
        fig, axs = plt.subplots(2, 4, figsize=(20, 10))
        fig.subplots_adjust(hspace=0.5)

        # Loop over the first 7 regions
        for i, (region, group) in enumerate(list(grouped)[:7]):
            row_index = i // 4
            col_index = i % 4
            ax = axs[row_index, col_index]

            top_items = group.groupby('ItemType')['UnitsSold'].sum().nlargest(5).reset_index()
            ax.bar(top_items['ItemType'], top_items['UnitsSold'])
            ax.set_title(f'Top 5 Items in {region}')
            ax.set_xlabel('Item Type')
            ax.set_ylabel('Units Sold')
            ax.tick_params(axis='x', rotation=45)

        # Remove the empty subplot in the last position
        fig.delaxes(axs[1, 3])

        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Load the dataset
    from retrieve import df
    sales_analysis = SalesAnalysis(df)

    # Plot total revenue by region and sales channel
    sales_analysis.total_revenue_by_region_and_sales_channel()

    # Plot top item types by region
    sales_analysis.top_item_types_by_region()

