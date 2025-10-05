import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def load_and_analyze_data():
    """Load and perform basic analysis on R&D expenditure data"""
    
    # Load the dataset
    df = pd.read_csv('data/rds2011_12_Table_17.csv')

    # Display basic information about the dataset
    print("Dataset Info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nDataset shape:", df.shape)

    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())
    
    return df

def create_plots(df):
    """Create all required visualizations"""
    
    # Data cleaning - remove rows with all NaN values in R&D columns
    rd_columns = ['Research & Development Expenditure in 2005-06', 
                  'Research & Development Expenditure in 2006-07',
                  'Research & Development Expenditure in 2007-08',
                  'Research & Development Expenditure in 2008-09',
                  'Research & Development Expenditure in 2009-10']

    # Filter out summary rows for clearer analysis of individual sectors
    individual_sectors = df[~df['Sub Sectors and Economic Activity'].str.contains('Total|GDP|Ratio', na=False)]

    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    
    # 1. Line Plot - Total R&D Expenditure Trend by Main Sectors
    print("\nCreating Line Plot: Total R&D Expenditure Trend...")
    create_line_plot_trend(df, rd_columns)
    
    # 2. Bar Plot - Average R&D Expenditure by Main Sectors
    print("Creating Bar Plot: Average R&D Expenditure by Sector...")
    create_bar_plot_avg(individual_sectors, rd_columns)
    
    # 3. Line Plot - R&D Expenditure Growth for Top Sub-sectors
    print("Creating Line Plot: R&D Expenditure Growth for Top Sub-sectors...")
    create_line_plot_growth(individual_sectors, rd_columns)
    
    # 4. Pie Chart - Sector-wise Distribution
    print("Creating Pie Chart: Sector-wise Distribution...")
    create_pie_chart(df, rd_columns)
    
    # 5. Growth Trends Analysis
    print("Creating Growth Trends Analysis...")
    create_growth_trends(df, individual_sectors, rd_columns)

def create_line_plot_trend(df, rd_columns):
    """Create line plot for R&D expenditure trends"""
    total_rows = df[df['Sub Sectors and Economic Activity'].str.contains('Total R&D Expenditure', na=False)]
    years = ['2005-06', '2006-07', '2007-08', '2008-09', '2009-10']

    plt.figure(figsize=(12, 8))
    for idx, row in total_rows.iterrows():
        sector = row['Sectors']
        expenditures = [row[rd_columns[0]], row[rd_columns[1]], row[rd_columns[2]], 
                       row[rd_columns[3]], row[rd_columns[4]]]
        plt.plot(years, expenditures, marker='o', label=sector, linewidth=2)

    plt.title('Total R&D Expenditure Trend by Sector', fontweight='bold', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('R&D Expenditure (Rs Crore)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tick_params(axis='x', rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('plots/line_plot_rd_trend.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_bar_plot_avg(individual_sectors, rd_columns):
    """Create bar plot for average R&D expenditure"""
    sector_avg = {}
    for sector in individual_sectors['Sectors'].unique():
        if pd.notna(sector) and sector != 'Total ':
            sector_data = individual_sectors[individual_sectors['Sectors'] == sector]
            avg_exp = sector_data[rd_columns].mean().mean()
            sector_avg[sector] = avg_exp

    plt.figure(figsize=(10, 6))
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'gold']
    bars = plt.bar(sector_avg.keys(), sector_avg.values(), color=colors)

    # Customize x-axis labels
    x_labels = [str(label).replace('(A)', 'A:').replace('(B)', 'B:')
                       .replace('(C)', 'C:').replace('(D)', 'D:')[:40] 
                for label in sector_avg.keys()]

    plt.xticks(range(len(x_labels)), x_labels, rotation=45, ha='right')
    plt.title('Average R&D Expenditure by Sector (2005-06 to 2009-10)', fontweight='bold', fontsize=14)
    plt.xlabel('Sector', fontsize=12)
    plt.ylabel('Average R&D Expenditure (Rs Crore)', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'Rs {height:,.0f} Cr',
                 ha='center', va='bottom', fontweight='bold', fontsize=10)

    plt.ylim(0, max(sector_avg.values()) * 1.15)
    plt.tight_layout()
    plt.savefig('plots/bar_plot_avg_expenditure.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Print values for reference
    print("\nAverage R&D Expenditure by Sector (Rs Crore):")
    for sector, avg in sector_avg.items():
        print(f"{sector}: Rs {avg:,.0f} Crore")

def create_line_plot_growth(individual_sectors, rd_columns):
    """Create line plot for top sub-sectors growth"""
    years = ['2005-06', '2006-07', '2007-08', '2008-09', '2009-10']
    top_subsectors = individual_sectors.nlargest(10, rd_columns[4])

    plt.figure(figsize=(14, 8))
    colors = plt.cm.tab10(np.linspace(0, 1, len(top_subsectors)))
    line_styles = ['-', '--', '-.', ':'] * 3

    for idx, (_, row) in enumerate(top_subsectors.iterrows()):
        subsector_name = row['Sub Sectors and Economic Activity']
        expenditures = [row[rd_columns[0]], row[rd_columns[1]], row[rd_columns[2]], 
                       row[rd_columns[3]], row[rd_columns[4]]]
        
        plt.plot(years, expenditures, 
                 marker='o', 
                 linewidth=2.5,
                 linestyle=line_styles[idx % len(line_styles)],
                 color=colors[idx],
                 markersize=6,
                 label=subsector_name[:30] + '...' if len(subsector_name) > 30 else subsector_name)

    plt.title('R&D Expenditure Growth: Top 10 Sub-sectors', fontweight='bold', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('R&D Expenditure (Rs Crore)', fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    plt.tick_params(axis='x', rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('plots/line_plot_growth_top_subsectors.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_pie_chart(df, rd_columns):
    """Create pie chart for sector distribution"""
    total_rows = df[df['Sub Sectors and Economic Activity'].str.contains('Total R&D Expenditure', na=False)]
    years = ['2005-06', '2006-07', '2007-08', '2008-09', '2009-10']
    
    sector_totals = {}
    for sector in total_rows['Sectors'].unique():
        if pd.notna(sector):
            sector_total = total_rows[total_rows['Sectors'] == sector][rd_columns].sum().sum()
            sector_totals[sector] = sector_total

    pie_labels = [str(label).replace('(A)', 'A:').replace('(B)', 'B:')
                         .replace('(C)', 'C:').replace('(D)', 'D:')[:15] 
                  for label in sector_totals.keys()]

    plt.figure(figsize=(10, 8))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    plt.pie(sector_totals.values(), labels=pie_labels, autopct='%1.1f%%', 
            startangle=90, colors=colors, explode=(0.05, 0.05, 0.05, 0.05))
    plt.title('Sector-wise Distribution of Total R&D Expenditure', fontweight='bold', fontsize=14)
    plt.tight_layout()
    plt.savefig('plots/pie_chart_sector_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_growth_trends(df, individual_sectors, rd_columns):
    """Create growth trends analysis"""
    years = ['2005-06', '2006-07', '2007-08', '2008-09', '2009-10']
    
    # Calculate growth rates
    total_row = df[df['Sub Sectors and Economic Activity'].str.contains('R&D Expenditure.*A\\+B\\+C\\+D', na=False)]
    if not total_row.empty:
        total_expenditures = total_row[rd_columns].iloc[0]
        growth_rates = []
        for i in range(1, len(total_expenditures)):
            growth = ((total_expenditures.iloc[i] - total_expenditures.iloc[i-1]) / total_expenditures.iloc[i-1]) * 100
            growth_rates.append(growth)
            print(f"Growth from {years[i-1]} to {years[i]}: {growth:.2f}%")
    else:
        total_expenditures = individual_sectors[rd_columns].sum()
        growth_rates = []
        for i in range(1, len(total_expenditures)):
            growth = ((total_expenditures.iloc[i] - total_expenditures.iloc[i-1]) / total_expenditures.iloc[i-1]) * 100
            growth_rates.append(growth)
            print(f"Growth from {years[i-1]} to {years[i]}: {growth:.2f}%")

    # Create growth trends plot
    plt.figure(figsize=(15, 6))

    # Overall R&D growth
    plt.subplot(1, 2, 1)
    plt.plot(years, total_expenditures, marker='o', linewidth=3, color='blue', markersize=8, markerfacecolor='red')
    plt.title('Overall R&D Expenditure Trend', fontweight='bold', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('R&D Expenditure (Rs Crore)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)

    for i, (year, value) in enumerate(zip(years, total_expenditures)):
        plt.annotate(f'{value:,.0f}', (year, value), textcoords="offset points", 
                     xytext=(0,10), ha='center', fontweight='bold')

    # Growth rates
    plt.subplot(1, 2, 2)
    growth_years = [f"{years[i]}-{years[i+1][-2:]}" for i in range(len(growth_rates))]
    bars = plt.bar(growth_years, growth_rates, color=['green' if x >= 0 else 'red' for x in growth_rates])
    plt.title('Year-over-Year Growth Rates', fontweight='bold', fontsize=14)
    plt.xlabel('Period', fontsize=12)
    plt.ylabel('Growth Rate (%)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.1f}%',
                 ha='center', va='bottom' if height >= 0 else 'top')

    plt.tight_layout()
    plt.savefig('plots/growth_trends.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Main function to run the analysis"""
    print("Starting R&D Expenditure Analysis...")
    
    # Create directories if they don't exist
    import os
    os.makedirs('plots', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Load and analyze data
    df = load_and_analyze_data()
    
    # Create all plots
    create_plots(df)
    
    print("\nAnalysis completed!")
    print("\nAll plots have been saved in the 'plots' directory:")
    print("1. line_plot_rd_trend.png - Main sectors R&D trends")
    print("2. bar_plot_avg_expenditure.png - Average expenditure by sector")
    print("3. line_plot_growth_top_subsectors.png - Growth of top 10 sub-sectors")
    print("4. pie_chart_sector_distribution.png - Sector distribution")
    print("5. growth_trends.png - Overall growth trends and rates")

if __name__ == "__main__":
    main()
