# Crop-Recommendation-System
Developed a web application to predict the variety of crop using parameters like Phosphorous, NItrogen, Potassium, Humidity, pH of soil, Rainfall and Temperature values . Project helps the farmers to take decision based upon suggested crop variety to increase their production

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Features

- Data Collection: Collects crop data based on soil and environmental parameters.
- Model Training: Trains a machine learning model using LightGBM.
- Prediction: Predicts the best crop to plant based on user inputs.
- Pickle File Generation: Generates a pickle file for the trained model.
- Web Interface: Provides a user-friendly web interface using Flask.

## Requirements

- Python 3.8 and above
- pandas
- lightgbm
- Flask
- scikit-learn

## Usage

 Run the main script to start the activity and pose detection:

    ```bash
    python app.py
    ```

## Steps to follow:

  -open command prompt and locate to project directory
  -create a virtual environment using : python -m venv venv
  -activate the environment using : venv\Scripts\activate
  -install the common dependencies : --pip install flask pandas scikit-learn numpy
                                    --pip install joblib pickle-mixin
  - run the file : python app.py
  - ctrl + click on the link like this in the output : http://127.0.0.1:5000/.

## File Structure

```plaintext
crop-recommendation-system/
│
│
├── model/
│   ├── crop_recommendation.pkl
│
├── static/
│   ├── images/
│        ├── crop.jpg
│
├── templates/
│   ├── help.html
│   ├── home.html
│   ├── login.html
│   ├── newcrop.html
│   ├── predict.html
│   ├── service.html
│
├── app.py
├── README.md
├── crop_recommendation.pkl

```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

