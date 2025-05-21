# Customer Purchase Prediction System

This project provides a machine learning solution to predict customer purchase behavior based on various customer metrics. It includes a trained decision tree model and a web UI for easy interaction with the prediction system.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Using the Web UI](#using-the-web-ui)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Customer Purchase Prediction System analyzes customer attributes to predict whether they are likely to make a purchase. This solution helps businesses optimize their marketing strategies, improve customer targeting, and increase conversion rates.

## Project Structure

```
customer-purchase-prediction/
├── model.py                    # Script for training and saving the model
├── app.py                      # Web UI application (Flask)
├── templates/                  # HTML templates for the web interface
│   ├── index.html              # Main prediction form page
├── static/                    
│   └── styles.css              # Styling for the web interface
├── data/
│   └── customer_purchase_data.csv  # Training dataset
├── models/                     # Saved model and preprocessing files
    ├── purchase_model.pkl      # Trained decision tree model
    └── scaler.pkl              # StandardScaler for feature normalization
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/customer-purchase-prediction.git
   cd customer-purchase-prediction
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

The model has already been trained and saved, but if you want to retrain it:

```
python model.py
```

This will:
1. Load the customer purchase data
2. Preprocess features using StandardScaler
3. Train a Decision Tree Classifier
4. Evaluate model performance
5. Save the model and scaler for later use

### Using the Web UI

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter customer attributes in the form and submit to get a purchase prediction.

## Model Details

- **Algorithm**: Decision Tree Classifier
- **Features**: 
  - Age, Income, BrowsingTime, etc. (adjust based on your actual features)
- **Target Variable**: PurchaseStatus (binary: 0 = No Purchase, 1 = Purchase)
- **Performance Metrics**: 
  - Accuracy
  


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
