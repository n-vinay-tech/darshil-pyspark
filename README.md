# PySpark Coursework - Darshil's Online Course

This repository contains my coursework and projects for the PySpark online course by Darshil. The repository includes complete setup documentation, code examples, assignments, and projects covering Apache Spark data processing with Python.

## 📚 Course Information

**Instructor:** Darshil  
**Course:** PySpark Online Course  
**Student:** [Your Name]  
**Start Date:** [Course Start Date]  

## 🛠️ Environment Setup

### System Configuration
- **OS:** Windows 10/11
- **Python:** 3.9+ (recommended 3.11 for LTS)
- **Java:** 17 (LTS) via Eclipse Adoptium
- **Apache Spark:** 3.5.6 (Pre-built for Hadoop 3.3+)
- **Hadoop Utils:** Winutils.exe for Hadoop 3.x

### Prerequisites Checklist
- [x] Python 3.9+ installed
- [x] Java 17 (LTS) installed via Eclipse Adoptium
- [x] Apache Spark 3.5.6 downloaded and configured
- [x] Winutils.exe installed for Hadoop compatibility
- [x] Virtual environment created and activated
- [x] All required dependencies installed

## 🔧 Installation Guide

### Step 1: Install Java 17
1. Download JDK 17 (Temurin MSI) from Eclipse Adoptium
2. Install to default path:
   ```
   C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot
   ```
3. Set environment variables (System variables):
   - `JAVA_HOME = C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot`
   - Add `%JAVA_HOME%\bin` to **Path**
4. Verify installation:
   ```powershell
   java -version
   ```

### Step 2: Install Apache Spark 3.5.6
1. Download **Spark 3.5.6 (Pre-built for Hadoop 3.3+)**
2. Extract to:
   ```
   C:\spark\spark-3.5.6-bin-hadoop3
   ```
3. Set environment variables:
   - `SPARK_HOME = C:\spark\spark-3.5.6-bin-hadoop3`
   - Add `%SPARK_HOME%\bin` to **Path**
4. Verify installation:
   ```powershell
   spark-shell --version
   pyspark --version
   ```

### Step 3: Install Winutils.exe
1. Download `winutils.exe` from **Hadoop 3.x** build
2. Place in:
   ```
   C:\hadoop\bin\winutils.exe
   ```
3. Set environment variable:
   - `HADOOP_HOME = C:\hadoop`
   - Add `%HADOOP_HOME%\bin` to **Path**
4. Verify:
   ```powershell
   winutils.exe ls .
   ```

### Step 4: Create Python Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
```

### Step 5: Install Dependencies
Create `requirements.txt`:
```txt
# Core Data Processing
pyspark>=3.5.0
pyarrow>=15.0.0
pandas>=2.2.0
numpy>=1.26.0

# Dashboarding
streamlit>=1.35.0
plotly>=5.22.0

# Visualization
matplotlib>=3.9.0
seaborn>=0.13.0

# Jupyter Support
jupyter>=1.0.0
notebook>=7.0.0
ipykernel>=6.29.0

# AWS Integration
boto3>=1.34.0
s3fs>=2024.3.1
awscli>=1.32.0
redshift-connector>=2.0.918
```

Install dependencies:
```powershell
pip install -r requirements.txt
```

### Step 6: Test PySpark Installation
Create `pyspark_test.py`:
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestApp").getOrCreate()
print("✅ Spark Session started successfully")
print("Spark version:", spark.version)

df = spark.range(5)
df.show()

spark.stop()
```

Run test:
```powershell
python pyspark_test.py
```

Expected output:
```
✅ Spark Session started successfully
Spark version: 3.5.6
+---+
| id|
+---+
|  0|
|  1|
|  2|
|  3|
|  4|
+---+
```

## 📁 Repository Structure

```
pyspark-coursework/
├── README.md
├── requirements.txt
├── pyspark_test.py
├── setup/
│   ├── environment_setup.md
│   └── troubleshooting.md
├── lessons/
│   ├── lesson_01_introduction/
│   ├── lesson_02_dataframes/
│   ├── lesson_03_transformations/
│   ├── lesson_04_actions/
│   ├── lesson_05_sql_operations/
│   ├── lesson_06_joins/
│   ├── lesson_07_aggregations/
│   ├── lesson_08_window_functions/
│   ├── lesson_09_streaming/
│   └── lesson_10_optimization/
├── assignments/
│   ├── assignment_01/
│   ├── assignment_02/
│   └── final_project/
├── projects/
│   ├── data_pipeline_project/
│   ├── streaming_analytics/
│   └── aws_integration/
├── datasets/
│   ├── sample_data/
│   ├── csv_files/
│   └── json_files/
├── notebooks/
│   ├── exploration/
│   └── experiments/
└── utils/
    ├── spark_utils.py
    ├── data_generators.py
    └── aws_helpers.py
```

## 🎯 Learning Objectives

### Core PySpark Concepts
- [ ] Spark Architecture and Components
- [ ] RDDs vs DataFrames vs Datasets
- [ ] Lazy Evaluation and Execution Plans
- [ ] Transformations and Actions
- [ ] Spark SQL and DataFrame API

### Data Processing Techniques
- [ ] Data Loading and Saving (CSV, JSON, Parquet, Delta)
- [ ] Data Cleaning and Transformation
- [ ] Joins and Aggregations
- [ ] Window Functions
- [ ] User Defined Functions (UDFs)

### Advanced Topics
- [ ] Spark Streaming and Structured Streaming
- [ ] Performance Optimization
- [ ] Memory Management and Caching
- [ ] Partitioning Strategies
- [ ] AWS Integration (S3, Redshift)

### Project Development
- [ ] End-to-end Data Pipelines
- [ ] Real-time Analytics
- [ ] Dashboard Development with Streamlit
- [ ] Cloud Deployment and Scaling

## 📝 Course Progress Tracker

### Module 1: Fundamentals
- [ ] Introduction to Apache Spark
- [ ] PySpark Installation and Setup
- [ ] First PySpark Application
- [ ] Understanding Spark Architecture

### Module 2: DataFrames and SQL
- [ ] Creating DataFrames
- [ ] DataFrame Operations
- [ ] Spark SQL Basics
- [ ] Working with Different Data Formats

### Module 3: Data Transformations
- [ ] Filtering and Selecting Data
- [ ] Adding and Modifying Columns
- [ ] Handling Missing Data
- [ ] Data Type Conversions

### Module 4: Aggregations and Joins
- [ ] GroupBy Operations
- [ ] Aggregate Functions
- [ ] Inner and Outer Joins
- [ ] Complex Join Scenarios

### Module 5: Advanced Operations
- [ ] Window Functions
- [ ] User Defined Functions
- [ ] Broadcasting and Accumulators
- [ ] Performance Tuning

### Module 6: Streaming and Real-time Processing
- [ ] Introduction to Spark Streaming
- [ ] Structured Streaming
- [ ] Processing Kafka Streams
- [ ] Real-time Analytics

### Module 7: AWS Integration
- [ ] Reading from S3
- [ ] Writing to S3
- [ ] Redshift Integration
- [ ] EMR Deployment

### Module 8: Final Project
- [ ] Project Planning
- [ ] Implementation
- [ ] Testing and Optimization
- [ ] Presentation

## 💻 Quick Start Commands

### Activate Environment
```powershell
.\venv\Scripts\activate
```

### Start PySpark Shell
```powershell
pyspark
```

### Start Jupyter Notebook
```powershell
jupyter notebook
```

### Run Streamlit Dashboard
```powershell
streamlit run dashboard.py
```

### Common PySpark Commands
```python
# Create Spark Session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Read CSV
df = spark.read.option("header", "true").csv("path/to/file.csv")

# Show data
df.show()

# Stop Spark session
spark.stop()
```

## 📊 Sample Datasets

### Included Sample Data
- **sales_data.csv** - E-commerce sales transactions
- **employee_data.json** - Employee records with nested structures
- **sensor_data.parquet** - IoT sensor readings
- **customer_data.csv** - Customer demographics and behavior

### External Dataset Sources
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [AWS Open Data](https://aws.amazon.com/opendata/)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)

## 🔍 Troubleshooting

### Common Issues and Solutions

**Issue: `java.lang.UnsupportedClassVersionError`**
- **Solution:** Ensure Java 17 is installed and `JAVA_HOME` is correctly set

**Issue: `HADOOP_HOME` not found**
- **Solution:** Verify winutils.exe is in `C:\hadoop\bin\` and `HADOOP_HOME` is set

**Issue: PySpark not starting**
- **Solution:** Check that `SPARK_HOME` and `PYTHONPATH` are correctly configured

**Issue: Permission denied errors**
- **Solution:** Run PowerShell as Administrator for initial setup

## 📚 Learning Resources

### Official Documentation
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark API Reference](https://spark.apache.org/docs/latest/api/python/)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)

### Additional Learning Materials
- [Spark: The Definitive Guide](https://databricks.com/p/ebook/spark-the-definitive-guide)
- [Learning Spark 2nd Edition](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/)
- [Databricks Academy](https://academy.databricks.com/)

## 🎨 Dashboard Development

### Streamlit Integration
This course includes building interactive dashboards using Streamlit with PySpark backends:

```python
import streamlit as st
from pyspark.sql import SparkSession

# Streamlit + PySpark example
st.title("PySpark Data Dashboard")
spark = SparkSession.builder.appName("StreamlitApp").getOrCreate()
# Dashboard code here
```

## ☁️ AWS Integration

### S3 Configuration
```python
# Reading from S3
df = spark.read.csv("s3a://bucket-name/path/to/file.csv")

# Writing to S3
df.write.mode("overwrite").csv("s3a://bucket-name/output/")
```

### Redshift Connection
```python
# Redshift connector setup
df.write \
  .format("com.databricks.spark.redshift") \
  .option("url", "jdbc:redshift://cluster-endpoint:5439/database") \
  .option("dbtable", "table_name") \
  .option("tempdir", "s3a://bucket/temp/") \
  .save()
```

## ✅ Setup Verification Status

- [x] Java 17 working
- [x] Spark 3.5.6 installed and verified
- [x] Winutils configured properly
- [x] Python virtual environment created
- [x] PySpark tested successfully
- [x] Streamlit + AWS libraries installed
- [x] Jupyter Notebook environment ready

## 🤝 Course Community

### Getting Help
- Course discussion forums
- Stack Overflow ([pyspark] tag)
- Apache Spark Community

### Contributing to Coursework
1. Fork this repository
2. Create feature branch (`git checkout -b feature/new-lesson`)
3. Commit changes (`git commit -am 'Add lesson notes'`)
4. Push to branch (`git push origin feature/new-lesson`)
5. Create Pull Request

## 📄 License

This coursework repository is for educational purposes as part of Darshil's PySpark course.

**Happy Learning! 🚀**

*Last Updated: [2025-08-31]*