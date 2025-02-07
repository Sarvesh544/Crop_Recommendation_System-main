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
├── train_model.py
├── config.json
├── requirements.txt
├── README.md


```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

