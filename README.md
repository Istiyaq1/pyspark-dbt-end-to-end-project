# End-to-End Data Engineering Project using PySpark, Databricks & dbt

## Project Overview

This project demonstrates an end-to-end data engineering pipeline built using Apache PySpark, Databricks and dbt.

The pipeline follows a Medallion Architecture (Bronze, Silver and Gold) to ingest, transform and prepare data for analytics and business reporting.

It also implements incremental data loading and Slowly Changing Dimension (SCD) Type 2 to manage historical data changes.

## Architecture

**Data Flow:**

Source CSV Files → Bronze → Silver → Gold → Business Analytics

### Architecture Components

1. **Source Layer**
   - CSV datasets stored in Databricks Unity Catalog Volumes.
   - Includes customers, drivers, locations, payments, trips and vehicles.

2. **Bronze Layer – PySpark**
   - Ingest raw source data.
   - Load data into Bronze tables.
   - Use reusable Python utility functions.

3. **Silver Layer – PySpark**
   - Transform and clean ingested data.
   - Apply data preparation and transformation logic.
   - Store processed data in Silver tables.

4. **Gold Layer – dbt**
   - Build analytics-ready models.
   - Apply SQL transformations using dbt.
   - Organize models for business reporting.

5. **Advanced dbt Implementations**
   - Incremental data loading.
   - SCD Type 2 using dbt snapshots.
   - Reusable Jinja macros.
   - dbt model organization and testing.

## Technologies Used

| Category | Technology |
|---|---|
| Processing | Apache PySpark |
| Platform | Databricks |
| Data Architecture | Medallion Architecture |
| Data Transformation | dbt |
| Query Language | SQL |
| Programming | Python |
| Templating | Jinja |
| Data Storage | Databricks Unity Catalog |
| Version Control | Git & GitHub |

## Repository Structure

```text
pyspark-dbt-end-to-end-project/
│
├── notebooks/
│   ├── Bronze_Ingestion.py
│   ├── Silver_Transformation.py
│   └── custom_utils.py
│
├── dbt_project/
│   ├── analyses/
│   ├── macros/
│   ├── models/
│   │   ├── business/
│   │   ├── gold/
│   │   ├── silver/
│   │   └── sources/
│   ├── seeds/
│   ├── snapshots/
│   ├── tests/
│   ├── dbt_project.yml
│   └── README.md
│
└── README.md
```

## Key Data Engineering Concepts Implemented

- Medallion Architecture (Bronze, Silver and Gold).
- Batch data ingestion using PySpark.
- Data transformation using PySpark and SQL.
- Incremental data loading with dbt.
- SCD Type 2 using dbt snapshots.
- Jinja templating and reusable macros.
- Data modeling for analytical workloads.
- Git-based version control.

## Project Setup

### Prerequisites

- Databricks workspace.
- Unity Catalog access.
- Python and PySpark.
- dbt with the appropriate Databricks adapter.
- Git and GitHub.

### Execution Flow

1. Configure the Databricks workspace and Unity Catalog.
2. Upload source CSV files into the appropriate Volume.
3. Execute the Bronze ingestion notebook.
4. Execute the Silver transformation notebook.
5. Configure dbt sources and models.
6. Execute dbt models.
7. Execute dbt snapshots for historical tracking.
8. Validate the resulting Gold and business models.

**Note:** Database connections, credentials, catalog names and schemas must be configured for the target environment. Credentials are not included in this repository.

## Author

**Istiyaq**

GitHub: [Istiyaq1](https://github.com/Istiyaq1)

---

*This project was developed as a hands-on implementation of modern data engineering concepts using PySpark, Databricks and dbt.*