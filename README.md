# 🌱 Plants Dashboard Project

## Project Overview
The **Plants Dashboard Project** is a business intelligence initiative designed to **transform raw plant sales and account data into actionable insights**.  

The project focuses on solving the problem of **understanding sales performance, profitability, and geographic trends** for different plant types and clients.  

By combining **Python data engineering** with **Power BI visual analytics**, the project delivers a ready dashboard containing **data-driven decisions**.  

The dashboard provides:

- **Key KPIs:** Total Sales, Total Quantity, Gross Profit, Profit Margin  
- **Trend Analysis:** Monthly sales and profit trends; performance by Product Family and Product Type  
- **Product Drill-down:** Hierarchy from Product Family → Product Group → Product Name; interactive species-level insights  
- **Geospatial Analysis:** Map showing Sales by Account location, color-coded by Sales or Profit Margin  
- **Filters / Slicers:** Country, Product Type, Product Size, Date (Year/Month/Quarter)  
- **Advanced DAX Metrics:** Profit Margin by Product Family, Top 5 products by sales, Year-over-Year growth  

This end-to-end workflow ensures actionable insights for inventory, marketing, and sales strategy.

---

## Problem Statement
Plant distributors often face challenges such as:

- Identifying the **most profitable plant species and families**  
- Understanding **regional variations in sales and profit**  
- Recognizing **top-performing clients/accounts**  
- Using **historical trends** to inform inventory and marketing strategies  

The dashboard **solves these problems** by integrating Python data processing with interactive Power BI visualizations.

---

## Dataset
The project uses a relational dataset typical of a business intelligence environment:

1. **Plants_FACT.csv** – transactional data including Sales, Quantity, Price, COGS, Date, and Account IDs  
2. **PlantsHierarchy_DIM.csv** – product details including Family, Group, Species, Size, and Type  
3. **Accounts_DIM.csv** – account and geographic information including Country, Latitude/Longitude, and Address  

After processing, a cleaned dataset is generated: `Plants_Dashboard_Cleaned.csv`, ready for visualization and analytics.

---

## Workflow

### 1. Python Data Preparation
- **Libraries:** `pandas`, `os`  
- **Steps:**  
  - Load and inspect datasets  
  - Clean data: trim strings, fill missing Account IDs, parse dates  
  - Compute KPIs:  
    ```python
    fact['Gross_Profit'] = fact['Sales_USD'] - fact['COGS_USD']
    fact['Profit_Margin'] = fact['Gross_Profit'] / fact['Sales_USD'] * 100
    ```  
  - Merge Fact and Dimension tables into a **single dataset for Power BI**  
  - Export `Plants_Dashboard_Cleaned.csv`  

---

### 2. Power BI Dashboard
- **Key Visualizations:**  
  - KPIs, trend charts, product hierarchy drill-down, geographic maps  
- **Filters & Slicers:** Country, Product Type, Product Size, Date  
- **Advanced DAX Metrics:** Profit Margin by Product Family, Top 5 products by sales, Year-over-Year growth  

---

### 3. Insights & Impact
- Identified the **most profitable plant families and species**  
- Highlighted **geographic regions with high revenue**  
- Enabled **interactive drill-down** to understand account-level performance  
- Equipped stakeholders with **data-driven insights** for inventory, sales, and marketing strategies  

---

---

### Key Learnings

- Built an **end-to-end business intelligence workflow**, transforming raw transactional data into executive-ready insights  
- Strengthened ability to design **solution-oriented dashboards** that support decision-making rather than simply reporting metrics  
- Developed practical experience with **hierarchical analysis and drill-down design** for product-level performance evaluation  
- Applied **geospatial analysis** to uncover regional performance patterns and revenue concentration  
- Improved dashboard usability through **thoughtful layout, KPI prioritization, and mobile optimization**

---

### 4. Project Structure

```text
Plant_Dashboard/
├── .gitignore
├── README.md
├── data/
│   ├── PlantsHierarchy_DIM.csv
│   ├── Plants_FACT.csv
│   ├── Accounts_DIM.csv
│   └── Plants_Dashboard_Cleaned.csv
├── scripts/                 # Python scripts for data cleaning and KPI calculations
│   └── prepare_data.py
├── .vscode/
└── .venv/
---

