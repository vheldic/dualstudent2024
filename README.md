# dualstudent2024
This repo is a solution to a task from the company Drei Österreich, for an application as a dual student at the FH Technikum Wien

## Installation 
1. Clone the repository:
```
https://github.com/vheldic/dualstudent2024.git
```
2. Install the required dependencies:
```
pip install Flask
pip install flask-cors
```
3. If SQLite is not already installed, you can download it from the SQLite website:
```
https://www.sqlite.org/download.html
```

## Files & Usage
### backend/importCSVtoDatabase.py
When runing this Python program, the SQLite database named `database.db`, which is also located in the backend directory, will be populated with all elements of the `customers_sales_2021_2022.csv` file:
```
python importCSVtoDatabase.py
```

### app.py
This Python file uses Flask to work as an REST API between the frontend and backend of this project. Run the script to allow fetching from the frontend:
```
python app.py
```

### frontend/index.html
This HTML file uses a bootstrap link for easier css implementation and a vue cdn link for effective functionality. Opening the file, you will be able to search for items from the database. By clicking on the Search-Button, the data will be fetched using our API and presented as a table on the website. Sorting and filtering is possible too, by selecting a filter and the Sort-Button.

## Configuration
This project uses database.db in the database directory as default. By changing the name or path in `importCSVtoDatabase.py` and `app.py`, it is possible to target any other database.
