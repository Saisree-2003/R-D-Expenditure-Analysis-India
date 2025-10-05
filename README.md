# R-D-Expenditure-Analysis-India
Analysis of R&D expenditure patterns across economic sectors in India (2005-2010)

# R&D Expenditure Analysis in India (2005-06 to 2009-10)

## Project Overview
This project analyzes Research & Development (R&D) expenditure patterns across different economic sectors in India from 2005-06 to 2009-10. The analysis provides insights into sector-wise R&D investments, growth trends, and distribution patterns.

## Data Source
- **Dataset**: R&D Statistics 2011-12, Table 17
- **Source**: [data.gov.in](https://data.gov.in)
- **Publisher**: Department of Science and Technology, Government of India
- **Time Period**: 2005-06 to 2009-10
- **Citation**: Ministry of Science and Technology (2011). "R&D Statistics at a Glance 2011-12". Government of India.

## Dataset Description
The dataset contains R&D expenditure data across four main sectors:
- **(A) Agriculture, Forestry & Fishing, Mining & Quarrying**
- **(B) Manufacturing, Construction, Electricity Gas & Water Supply**
- **(C) Transport & Communication**
- **(D) Public Administration & Defence and other Services**

## Key Findings

### 1. Sector-wise R&D Expenditure Trends
- **Public Administration & Defence** shows the highest R&D expenditure
- **Agriculture & Mining** sector demonstrates consistent growth
- **Transport & Communication** has the lowest R&D investment among major sectors

### 2. Growth Patterns
- Overall R&D expenditure showed positive growth across all years
- Highest growth observed between 2007-08 and 2008-09
- Consistent year-over-year increase in total R&D spending

### 3. Distribution Analysis
- Public Administration dominates with the largest share of R&D expenditure
- Manufacturing sector shows significant variation across sub-sectors
- Service sector within Public Administration shows substantial R&D investment

## Installation and Usage

### Requirements
```bash
pip install -r requirements.txt


Run Analysis
bash
python analysis.py
Project Structure
text
R&D-Expenditure-Analysis-India/
├── analysis.py          # Main analysis script
├── requirements.txt     # Python dependencies
├── data/               # Dataset directory
│   └── rds2011_12_Table_17.csv
├── plots/              # Generated visualizations
│   ├── line_plot_rd_trend.png
│   ├── bar_plot_avg_expenditure.png
│   ├── line_plot_growth_top_subsectors.png
│   ├── pie_chart_sector_distribution.png
│   └── growth_trends.png
├── notebooks/          # Jupyter notebooks
└── README.md          # Project documentation
Plots Generated
Line Plot: Total R&D expenditure trends by sector

Bar Plot: Average R&D expenditure by sector

Line Plot: Growth trends of top 10 sub-sectors

Pie Chart: Sector-wise distribution of total R&D expenditure

Growth Trends: Overall expenditure trend and growth rates

License
MIT License - see LICENSE file for details.

Acknowledgments
Data provided by data.gov.in

Department of Science and Technology, Government of India
