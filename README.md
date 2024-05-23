# Taxi Fare Predictor

This Django project predicts taxi fares based on user input, including departure and arrival points within New York City (using Mapbox), the year, and the bearing. The project uses a pre-trained machine learning model to make fare predictions.

## Features

- Select departure and arrival points on a Mapbox map to calculate the distance.
- Input the year and bearing.
- Predict taxi fares using a machine learning model.
- Display the predicted fare to the user.

## Technologies Used

- Django
- Mapbox
- Scikit-learn (or any other ML library used for training the model)
- HTML/CSS for front-end

## Project Structure
```plaintext
TaxiFarePredictor/
├── manage.py
├── TaxiFarePredictor/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── fare_prediction/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── templates/
│   │   ├── fare_prediction/
│   │   │   ├── predict.html
│   │   │   ├── result.html
│   ├── static/
│       ├── fare_prediction/
│           ├── styles.css
├── model/
│   ├── model.pkl
```

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 3.0+
- Virtualenv (recommended)

### Steps to Run the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/TaxiFarePredictor.git
   cd TaxiFarePredictor

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt

4. **python manage.py migrate:**

    ```bash
    python manage.py migrate

5. **python manage.py runserver:**

    ```bash
    python manage.py runserver

   # Taxi Fare Predictor

This project is a web application for predicting taxi fares based on user inputs such as departure and arrival points, year, and bearing. The application leverages Django for the web framework, Mapbox for map integration, and a machine learning model for fare prediction.

## Configuration

### Mapbox Configuration

To integrate Mapbox, you need an access token. You can obtain one by signing up on the [Mapbox website](https://www.mapbox.com/).

1. Open `django_model_app/templates/predict.html`.
2. Replace `YOUR_MAPBOX_ACCESS_TOKEN` with your actual Mapbox access token.

### Machine Learning Model

Ensure that your machine learning model file (`model.pkl`) is saved in the `model` directory.

## Usage

1. **Select the departure point:** Click on the map to set the departure location.
2. **Select the arrival point:** Click on the map again to set the arrival location.
3. **Fill in the form:** Select the year and bearing.
4. **Predict the fare:** Click the "Predict Fare" button to get the predicted fare.

## Directory Breakdown

### Django Project Files

- `manage.py`: Django's command-line utility for administrative tasks.
- `django_model/`: Contains settings and configuration files for the Django project.
  - `settings.py`: Configuration file for your Django project.
  - `urls.py`: URL declarations for the project.
  - `wsgi.py` and `asgi.py`: Entry points for WSGI/ASGI-compatible web servers.

### Django model App

- `views.py`: Contains view functions to handle requests and render responses.
- `forms.py`: Contains the form for user input (year, distance, bearing).
- `utils.py`: Utility functions, including loading the machine learning model and predicting fare.
- `templates/`: Directory containing HTML templates for the app.
  - `predict.html`: Template for the prediction form and Mapbox integration.
  - `result.html`: Template for displaying the prediction result.
- `static/`: Directory for static files (CSS, JavaScript) related to the app.
- `model/`: Directory containing the saved machine learning model file (`model.pkl`).

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Mapbox](https://www.mapbox.com/)
- [Scikit-learn](https://scikit-learn.org/)






