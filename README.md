# Data Engineering Project

## Project Overview

This project highlights my exploration in data engineering. The primary objective is to generate synthetic data and integrate it with various tools such as Snowflake, dbt, Airflow, and AWS services like EC2, S3, Lambda, SNS, and more. Additionally, the project aims to utilize and demonstrate proficiency in these technologies.

## Goals

1. Enable companies to develop a data strategy using an ELT approach.
2. Develop an automated data pipeline using a modern data stack, including notions of DevOps.
3. Showcase skills in data engineering.

## Project Structure

Navigate through the project's structure:

- `airflow/`: Folder containing Airflow DAG and related files.
- `aws`: Code for the Lambda function.
- `dbt/`: Folder containing dbt models and configurations.
- `samples`: Airflow logs for each task, AWS lambda and DBT linage.
- `src`: Python scripts for generating fake data and sample of the data in CSV.


## Pipeline Diagram

![Screenshot 2024-](https://github.com/MostafaNabilll/end2end_pipeline/assets/60539423/3b775837-f366-4435-be39-9af84583e350)



# Contents

- [The Generated Data](#the-generated-data)
- [Used Tools](#used-tools)
- [Conclusion](#conclusion)
- [Key Highlights](#key-highlights)
- [Remaining Tasks](#remaining-tasks)

## The Generated Data

### Data Components

- **Denormalized data**: Stored as CSV files, containing all the necessary data, generated through a Python script.
- **Product data**: The product dataset is created using a Python script and stored as a CSV file.
- **Vet data**: The Vet dataset is created using a Python script and stored as a CSV file.

### Objectives

1. Implement multiple CTEs for the data mart.
2. Utilize a Snowflake schema for effective organization.
3. Serve transformed data for insights.
4. Automate the whole process with Airflow.
5. Create a dashboard with Tableau.

## Used Tools

**Motivation**

Simulating a modern data stack, showcasing familiarity with various technologies.

- Stack
  - Docker, Docker-Compose.
  - AWS Services - EC2, S3, IAM, Lambda, SNS, Secret Manager.
  - Snowflake as Data Warehouse.
  - Python, Pandas, and Databases.
  - Airflow.
  - dbt Core.
  - Data modeling, Snowflake architecture, normalizations.

- More specifically, the following technologies were utilized throughout the project:
  - Docker Compose: Used to initiate Apache Airflow for scheduling and orchestration.
  - Airflow: Orchestrated the data pipeline extraction process, running Python, Snowflake, and Bash Operators to perform different tasks.
  - dbt (Data Build Tool): Utilized for the intermediate and data mart layers, enabling the implementation of CTEs, normalizations, and a Snowflake schema.

![Model databases](https://github.com/MostafaNabilll/end2end_pipeline/assets/60539423/1374714b-b70e-4a16-999c-d6641df87b78)

## Conclusion

Encountered learning opportunities and challenges, testing fundamental technical skills for a data engineer.

## Key Highlights:

1. Integration of different technologies.
2. Database building and modeling challenges.

## Remaining Tasks

1. Add different data sources like APIs.
2. Dive deep into different services like API gateway, CloudWatch.
3. Implement a CI/CD.
4. Implement an Infrastructure as Code like Terraform.
5. Integrate Tableau for dashboard visualization.
