# Espoo 2022 Data Engineering Capstone

This project analyzes and visualizes general statistics of Espoo, Finland for 2022 as part of the DataTribe Collective Capstone.

## Project Structure

```
grigorii-tishchuk/
├── README.md
├── dags/
├── scripts/
├── data/
│   └── Espooaluetietoa2022.csv
└── notebooks/
    └── analysis.ipynb
```

## Steps

1. **Ingest**: Load Espoo 2022 data from CSV.
2. **Transform**: Clean and reshape data using Pandas.
3. **Store**: Upload processed data to Google BigQuery.
4. **Visualize**: Build a Streamlit dashboard to explore trends (e.g., population, housing, employment).
5. **Orchestrate**: Automate the pipeline using Airflow (Cloud Composer).
6. **Package**: Use Poetry for dependency management.

## Business Case

Analyze Espoo's population structure, housing, and employment to identify key trends and support city planning.

## How to Run

1. Install dependencies:
    ```
    poetry install
    ```
2. Run the Jupyter notebook for data exploration:
    ```
    jupyter notebook notebooks/analysis.ipynb
    ```
3. (Optional) Run the Streamlit dashboard:
    ```
    streamlit run scripts/dashboard.py
    ```
4. (Optional) Trigger the Airflow DAG for orchestration.

## Data Source

- [Espooaluetietoa2022.csv](data/Espooaluetietoa2022.csv): Official statistics from the City of Espoo.

## Author

Grigorii Tishchuk

---
This project is part of the DataTribe Collective Data Engineering Capstone.