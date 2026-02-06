# Overview

This repository contains AquaFlow, a Python-based urban water intelligence system developed to analyze, predict, and simulate Chennai’s water supply, demand, leakage, and system stress.

The project integrates machine learning, geospatial analysis, and open government datasets to create a digital twin of Chennai’s water infrastructure, supporting data-driven and sustainable water governance

# Features

City-wide water supply and demand analysis

Reservoir-wise inflow and outflow forecasting

Leakage detection using pressure and flow anomalies

Rainfall prediction using LSTM models

Zone-wise water stress simulation

Scenario-based climate and policy analysis

Interactive monitoring dashboards


# Modules
## Water Source Analysis

Surface reservoirs and lakes

Desalinated seawater plants

Groundwater and recycled water sources

Source contribution estimation in MLD

## Dam Level and Reservoir Stress Models

Inflow and outflow imbalance detection

Reservoir stress severity scoring

City-level aggregation

Early warning alert generation

## Leakage Detection Module

Pressure and flow-rate monitoring

Detection of abnormal flow patterns

Classification of zones into:

 - Normal zones

 - Leak-detected zones

 - Burst-risk zones

## Rainfall Prediction and Trend Analysis

Historical rainfall analysis (1901–2021)

LSTM-based 12-month rainfall forecasting

Seasonal pattern identification

Input layer for water simulation models

## Scenario-Based Water Simulation

Climate scenarios (Normal, Drought, Wet Year)

Population growth scenarios

Groundwater extraction stress modeling

Policy-based supply allocation

Zone-wise deficit and surplus estimation

# Data Sources

Chennai Metro Water Supply and Sewerage Board

Government open data portals

Kaggle water leakage datasets

Historical rainfall datasets

Municipal infrastructure data (KML to GeoJSON)

# Tech Stack

Python

Machine Learning (LSTM, anomaly detection)

Geospatial processing tools

Data visualization dashboards
