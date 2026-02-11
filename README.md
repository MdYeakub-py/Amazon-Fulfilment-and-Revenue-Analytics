# 📊 Amazon Fulfilment & Revenue Analytics

An end-to-end data analytics project that ingests Amazon sales data, processes it using Python ETL, stores it in MySQL using a star schema, and visualizes KPIs and insights in Power BI.

This project demonstrates skills in:
- Data Engineering (ETL, Data Modeling)
- SQL & Database Design (Star Schema)
- Business Intelligence (Power BI Dashboards)
- Business Analytics (Cohort Analysis & Forecasting)

---

## 🧱 Architecture Overview

CSV (Kaggle) → Python ETL → MySQL (Star Schema) → Power BI Dashboards

---

## 📁 Data Source

- Dataset: Amazon Sales Report  
- Source: Kaggle  
- Description: Order-level e-commerce data including fulfillment type, shipping level, product attributes, revenue, and logistics status.

---

## 🔄 ETL Pipeline (Python)

### Step 1: Extract
- Load raw CSV using pandas.
- Standardize column names.
- Parse dates and numeric fields.

### Step 2: Transform
- Clean text fields (trim spaces, normalize status values).
- Normalize order status (Shipped / Cancelled).
- Convert B2B field to boolean.
- Handle missing values.
- Generate surrogate keys for dimensions.

### Step 3: Load
- Load cleaned data into MySQL:
  - fact_orders
  - dim_date
  - dim_product
  - dim_region

---

## 🗄️ Data Modeling (Star Schema)

### Fact Table
- fact_orders (order_id, order_date, revenue, qty, fulfillment, courier_status, etc.)

### Dimension Tables
- dim_date (year, month, day, weekday)
- dim_product (sku, category, size, style)
- dim_region (city, state, postal code, country)

This structure enables fast analytics and scalable BI reporting.

---

## 📈 Power BI Dashboards

### 1️⃣ Overview Page
**KPIs**
- Total Revenue  
- Total Orders  
- Shipped Orders  
- Cancelled Orders  
- Cancellation Rate  
- Average Order Value (AOV)

**Insights**
- Revenue trend over time  
- Fulfillment split (Amazon vs Merchant)  
- Top states & SKUs by revenue  

---
![Amazon Fulfilment and Revenue Analytics New_page-0001](https://github.com/user-attachments/assets/f71393eb-2a8b-44c4-9bea-e7b49dd1aed2)

### 2️⃣ Product Insights Page
**Goal:** Identify high-performing and problematic products.

**Visuals**
- Revenue by Category & Size  
- Cancelled Orders by SKU  
- SKU-level performance table (Orders, Revenue, Cancel Rate)

---
![Amazon Fulfilment and Revenue Analytics New_page-0002](https://github.com/user-attachments/assets/c4060208-5d48-4aba-9d20-442426a9264c)

### 3️⃣ Geography Insights Page
**Goal:** Understand regional performance.

**Visuals**
- Revenue by State  
- Top Cities by Revenue  
- City-wise Orders, Revenue & Cancellation Rate

---
![Amazon Fulfilment and Revenue Analytics New_page-0003](https://github.com/user-attachments/assets/04242d04-be24-477d-85a3-3668eea90fee)

### 4️⃣ Fulfilment & Logistics Page
**Goal:** Analyze operational efficiency.

**Visuals**
- Ship Service Level distribution  
- Courier Status performance  
- Fulfillment vs AOV vs Cancel Rate  
- Heatmap: Service Level vs Courier Status

---
![Amazon Fulfilment and Revenue Analytics New_page-0004](https://github.com/user-attachments/assets/c0656374-1ed5-47e4-a5f2-e25cdde46a45)

### 5️⃣ Customer Cohort Analysis Page
**Goal:** Measure customer retention behavior.

**KPIs**
- Total Customers  
- Repeat Customers  
- Retention Rate  
- Avg Orders per Customer  

**Visuals**
- Cohort Heatmap (Retention by Month Index)

---![Amazon Fulfilment and Revenue Analytics New_page-0005](https://github.com/user-attachments/assets/62737939-d515-47da-9890-0c26c5b27660)


### 6️⃣ Forecasting Page
**Goal:** Predict future sales trends.

**KPIs**
- Current Month Revenue  
- Current Month Orders  
- MoM Growth %  
- Forecasted Next Month Revenue  

**Visuals**
- Revenue Trend with Forecast  
- Orders Trend  
- Revenue vs Cancellation Trend

---![Amazon Fulfilment and Revenue Analytics New_page-0006](https://github.com/user-attachments/assets/f3bcba33-abbb-4a9a-967b-8d3a66d3bd93)


## ▶️ How to Run This Project

1. Download dataset from Kaggle  
2. Set up MySQL and create schema  
3. Run Python ETL script  
4. Connect Power BI to MySQL  
5. Refresh Power BI model

---

## 🧪 Tools & Tech

- Python (pandas, SQLAlchemy)
- MySQL
- Power BI
- SQL
- Kaggle Dataset

---

## 🚀 Key Business Insights

- Expedited shipping shows lower cancellation rates  
- Certain SKUs drive a disproportionate share of revenue (Pareto effect)  
- Urban cities generate higher AOV  
- Customer retention drops significantly after Month 1  
- Seasonal patterns affect revenue forecasting

---

## 🔒 Security Note

Database credentials are managed via environment variables and not hardcoded.

---

## 📌 Future Improvements

- Add ML-based forecasting (ARIMA/Prophet)
- Automate ETL using Airflow
- Add RFM segmentation
- Deploy Power BI Service with scheduled refresh

---

## 🙋‍♂️ About Me

I'm passionate about data, product thinking, and solving real-world problems with business intelligence. If you're interested in collaborating or want to discuss the dashboard, feel free to connect!


💼 https://mdyeakub-py.github.io/Personal_Portfolio-/

🔗 https://www.linkedin.com/in/mdyeakub35/

📧 mdyeakub.cse@gmail.com

🐱 GitHub: https://github.com/MdYeakub-py

---

Thanks for checking out my Amazon Fulfilment & Revenue Analytics – Power BI Dashboard project! 🍽️📊
---
