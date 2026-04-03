# ETL Pipeline Project

## Overview

This project implements an Extract, Transform, Load (ETL) pipeline that processes e-commerce customer and basket data. It extracts data from CSV files, cleans and transforms the data through validation steps, and loads the processed data into a PostgreSQL database for further analysis and reporting.

The pipeline is designed to handle customer transaction data, consolidating information from multiple sources into a unified, clean dataset ready for analytics and business intelligence tools like Power BI.

## Project Structure

```
ETL/
├── pipeline.py                 # Main ETL transformation script
├── load_data.py               # Database loading script
├── customer_details.csv       # Input: Customer information data
├── basket_details.csv         # Input: Transaction/basket data
├── clean_master_data.csv      # Output: Cleaned and merged dataset
├── docs/
│   └── screenshots/
│       └── powerbi/           # Power BI dashboard screenshots
└── README.md                  # Project documentation
```

## Files Description

| File | Description |
|------|-------------|
| `pipeline.py` | Extracts customer and basket data from CSV files, removes missing values, and performs an inner join to create a unified master dataset |
| `load_data.py` | Connects to PostgreSQL database and loads the cleaned master data into the `sales_data` table |
| `customer_details.csv` | Source data containing customer information including customer ID and related attributes |
| `basket_details.csv` | Source data containing transaction/basket information linked to customers by customer ID |
| `clean_master_data.csv` | Output file containing the merged and cleaned dataset |

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- PostgreSQL database (for the loading phase)

## Installation

### 1. Clone or Download the Project

Navigate to the project directory:

```bash
cd ETL
```

### 2. Install Required Dependencies

Install the required Python packages:

```bash
pip install pandas sqlalchemy psycopg2-binary
```

**Required packages:**
- `pandas` - Data manipulation and CSV processing
- `sqlalchemy` - Database abstraction layer
- `psycopg2-binary` - PostgreSQL adapter for Python

## Usage

### Step 1: Run the ETL Pipeline

Execute the main pipeline script to extract, transform, and clean the data:

```bash
python pipeline.py
```

**What happens:**
- Reads `customer_details.csv` and `basket_details.csv`
- Displays data summaries and previews
- Removes rows with missing values
- Performs an inner join on `customer_id`
- Outputs the cleaned master data to `clean_master_data.csv`
- Displays total row count in the merged dataset

### Step 2: Load Data to PostgreSQL

After the pipeline completes successfully, load the cleaned data into your PostgreSQL database:

```bash
python load_data.py
```

**What happens:**
- Reads the cleaned data from `clean_master_data.csv`
- Connects to the PostgreSQL database using the configured connection string
- Creates or replaces the `sales_data` table in the database
- Completes the ETL process

### Database Configuration

Before running `load_data.py`, update the PostgreSQL connection string with your credentials:

```python
connection_string = 'postgresql://username:password@localhost:5432/ecommerce_db'
```

**Connection string format:**
```
postgresql://username:password@host:port/database_name
```

## Data Flow

```
customer_details.csv  ──┐
                        ├──> pipeline.py ──> Data Cleaning & Merging ──> clean_master_data.csv ──> load_data.py ──> PostgreSQL
basket_details.csv ────┘                                                                                          Database
```

## Power BI Integration

Screenshots and visualizations of Power BI dashboards connected to this data are stored in:

```
docs/screenshots/powerbi/
```

To add your Power BI dashboard screenshots:
1. Export your visualization from Power BI
2. Save the image file to `docs/screenshots/powerbi/`
3. You can reference them in your documentation or presentations

Example naming convention:
- `sales_overview_dashboard.png`
- `customer_analytics.png`
- `transaction_summary.png`

## Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'pandas'`
- Solution: Install packages with `pip install pandas sqlalchemy psycopg2-binary`

**Issue:** `Connection refused` when connecting to PostgreSQL
- Solution: Verify PostgreSQL is running and update the connection string with correct host, port, and credentials

**Issue:** Missing values error during transformation
- Solution: The pipeline automatically removes rows with missing values. Check your source CSV files for data quality

**Issue:** Database table already exists
- Solution: The script uses `if_exists='replace'` to automatically overwrite existing tables

## Future Enhancements

- Add data validation and profiling reports
- Implement incremental data loading instead of full replacement
- Add error handling and logging
- Create automated scheduling with cron or task scheduler
- Extend to support additional data sources
- Add unit tests for data quality checks

## Contributing

To contribute to this project, please ensure that:
- Data quality checks are in place
- Changes are tested with sample data
- Documentation is updated accordingly

## License

This project is for internal use.

## Support

For issues or questions about the ETL pipeline, review the troubleshooting section or check the console output for detailed error messages.
