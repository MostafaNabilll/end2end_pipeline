FROM apache/airflow:2.8.1

USER root

# Update and upgrade system packages
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /awscliv2.zip /aws

USER airflow

# Copy the requirements file into the container
COPY requirements.txt /opt/airflow/requirements.txt

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# Install additional Python packages
RUN pip install --no-cache-dir apache-airflow-providers-amazon \
    apache-airflow-providers-snowflake
