# Singapore HDB Resale Price Prediction

This repository contains a Streamlit web application for predicting resale prices of HDB flats in Singapore. The model used for predictions is a RandomForestRegressor trained on relevant features.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Introduction

The Singapore HDB Resale Price Prediction app allows users to predict the resale prices of HDB flats based on several input features such as the month of resale, number of rooms, storey, floor area, and lease commencement date.

## Features

- **User Input:** Users can input the month, number of rooms, storey, floor area in square meters, and lease commencement year.
- **Prediction:** The app uses a pre-trained RandomForestRegressor model to predict the resale price based on user inputs.
- **Streamlit Interface:** A user-friendly interface built with Streamlit.

## Installation

To run this app locally, you need to have Python installed. Follow these steps:

## Usage
Open your web browser and navigate to http://localhost:8501.
Enter the required input features in the sidebar:
Month (format: YYYY-MM)
Number of Rooms
Storey
Floor Area (sqm)
Lease Commencement Year
Click the "Predict" button to get the predicted resale price.

This app is hosted in streamlit Cloud platform.
https://singapore-hdb-analysis-bjotfvxf9ffmsnxjforfwb.streamlit.app/

