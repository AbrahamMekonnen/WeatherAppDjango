# Django Weather App
This Django app pulls weather data from an API and displays it on a webpage based on user input. Users can search for weather information by providing the name of a city or country. The app uses the OpenWeatherMap API to retrieve the weather data.

### Installation
To use this app, follow these steps:

1. Clone the repository to your local machine using git clone https://github.com/your_username/django-weather-app.git.
2. Change into the project directory using cd django-weather-app.
3. Create a virtual environment using python -m venv env.
4. Activate the virtual environment using source env/bin/activate (Linux/Mac) or env\Scripts\activate (Windows).
5. Install the required packages using pip install -r requirements.txt.
6. Create a .env file in the root directory of the project and add your OpenWeatherMap API key to it using the following format:
makefile
6. Copy code
API_KEY=<your_api_key>
### Usage
To use the app, follow these steps:

1. Start the development server using python manage.py runserver.
2. Open a web browser and navigate to http://localhost:8000/.
3. Enter the name of a city or country into the search field and click the "Search" button.
4. The app will retrieve weather data from the OpenWeatherMap API and display it on the page.
### Troubleshooting
If you encounter any issues while using the app, please try the following troubleshooting steps:

1. Make sure you have created a .env file with your OpenWeatherMap API key.
2. Check the console for any error messages.
3. Make sure you have installed all the required packages using pip install -r requirements.txt.
4. f you are still experiencing issues, please create a new issue on the project's GitHub page.
### Credits
This app was created by [Your Name]. The weather data is provided by the OpenWeatherMap API.
