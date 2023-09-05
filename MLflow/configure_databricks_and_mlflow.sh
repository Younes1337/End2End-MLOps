#!/bin/bash

# Set the Databricks host URL
DATABRICKS_HOST="https://community.cloud.databricks.com/"

# Configure Databricks
databricks configure --host "$DATABRICKS_HOST"

# Set the tracking URI to Databricks
mlflow set_tracking_uri "databricks"

# Set the experiment path
mlflow set_experiment "/Users/younesmamma20@gmail.com/GPT2-LLM-FineTuning"