# Job Scraping Web Application

This project implements multi-threaded web scraping to extract job listings from multiple websites (e.g., Jobstreet, Loker.id, Kalibrr) based on user-specified keywords. Built using Python for the backend and Flask for the web interface, it leverages Selenium to automate the scraping process. Users can select which job sites to scrape and view the results dynamically on the web interface.

## Preview Application

- Main page:
  
![home](https://github.com/user-attachments/assets/5e9a8c65-17f2-4cb3-8d21-94bc6c6f372b)

- Scraping result page:
  
![result](https://github.com/user-attachments/assets/cd6d8529-c14a-402d-9cca-6e135ca4fb4e)

## Folder Structure
```bash
WEB_SCRAPING/
│
├── app/
│   ├── __pycache__/           # Contains Python bytecode files generated during runtime. These files do not need to be edited or viewed directly.
│   ├── __init__.py            # Initialization file for the Python package, allowing the 'app' folder to be recognized as a package.
│   ├── scraping.py            # Python module containing the logic for scraping data from selected job sites.
│
├── templates/
│   ├── index.html             # HTML page for the input form where users can enter a keyword and select sites for scraping.
│   └── result.html            # HTML page that displays the scraping results after the user submits a keyword and selects sites.
│
├── app.py                     # Main application file that handles routing logic and user interaction using Flask.
├── README.md                  # Instructions on how to use the application.
└── requirements.txt           # File listing the required libraries to run this application.
```

## Configuration for Scraping

To run the scraping functionality, follow these steps:

### Use Chrome:
1. Install Chromium by visiting this [link](https://googlechromelabs.github.io/chrome-for-testing/#stable).
2. Select the appropriate version of ChromeDriver based on your device. Copy the URL and open it in a new tab to start the download.
3. Once downloaded, extract the file and copy the path to `chromedriver.exe` (e.g., `C:/Users/YourUsername/Downloads/chromedriver-win32/chromedriver.exe`).
4. Insert that path in the `app.py` file at the `CHROME_DRIVER_PATH` variable.

## Installation

1. Clone this repository to your local machine.
2. Open a terminal in the project directory.
3. Install the required Python libraries by running the following command:
   ```bash
   pip install -r requirements.txt

## Running the Application

1. Open a terminal in the project directory.
2. Start the Flask application by running the following command:
   ```bash
   python app.py
3. Open your web browser and navigate to the following URL:
   ```bash
   http://127.0.0.1:5000/
