# Azure Healthcare Data Pipeline

This project demonstrates a healthcare data pipeline built on Azure using Data Factory, Data Lake, Databricks, and Azure SQL.

## Tech Stack

- Azure Data Factory (Orchestration)
- Azure Data Lake Storage (Raw & Processed Data)
- Azure Databricks (Transformation/Analytics)
- Azure SQL Database (Reporting Layer)
- Infrastructure as Code (Bicep)
- Python (ETL scripts, Databricks jobs)

## Structure

- `pipelines/` – Azure Data Factory pipeline definition
- `src/` – ETL Python scripts
- `infra/` – Bicep templates for infrastructure deployment
- `notebooks/` – Databricks notebooks for analysis
- `config/` – Pipeline configuration
- `tests/` – Unit tests

## Getting Started

1. Deploy infrastructure:
    ```bash
    az deployment sub create --location <region> --template-file infra/main.bicep --parameters infra/parameters.json
    ```
2. Configure Azure Data Factory using `pipelines/adf_pipeline.json`.
3. Run ETL scripts locally or as Databricks jobs.
4. Explore and analyze data using provided notebooks.
