#  Laptop Price Predictor

A **Machine Learning web application** that predicts the **price of laptops** based on their specifications such as brand, RAM, CPU, GPU, screen size, and storage.  
The model is trained with real-world laptop data and deployed using **Flask**.  

## project deployment link - https://laptop-price-prediction-1-plgp.onrender.com/

## Project Overview

In this project, I:

- **Cleaned & Preprocessed Data** – handled categorical & numerical features (Company, RAM, CPU, GPU, etc.)  
- **Engineered Features** – calculated **PPI (Pixels Per Inch)** from screen size & resolution to capture display quality  
- **Built ML Model** – trained an **XGBoost regression pipeline** for accurate price prediction  
- **Saved Model with Pickle** – used `.pkl` files for reusability without retraining  
- **Developed Web App (Flask)** – created a user-friendly form to input laptop specs and get price instantly  
- **Designed Frontend** – clean HTML/CSS interface with dropdowns for brands, CPU, GPU, and storage options  

---

## How This Project is Helpful

- Helps users **estimate laptop prices** before buying or selling  
- Useful for **e-commerce websites** to suggest fair pricing  
- Beneficial for **students & tech enthusiasts** to understand how specs impact price  
- Can be extended into a **recommendation system** for best laptops within budget  

---

#### Tech Stack

- Python 3.x
- Flask – Web framework
- Scikit-learn – ML utilities
- XGBoost – ML model for regression
- Pandas, Numpy – Data processing
- HTML, CSS – Frontend           
