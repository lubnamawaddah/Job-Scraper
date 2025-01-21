from flask import Flask, render_template, request
from app.scraping import scrape_with_threading

app = Flask(__name__)

# Path to Chrome driver
CHROME_DRIVER_PATH = "C:/Users/LENOVO/Downloads/chromedriver-win32/chromedriver.exe"

# Number of items per page
ITEMS_PER_PAGE = 5

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    # Get data from form (for POST) or from URL (for GET)
    keyword = request.form.get('keyword') or request.args.get('keyword')
    selected_sites = request.form.getlist('sites') or request.args.getlist('sites')

    if not keyword or not selected_sites:
        return "Please enter a keyword and select at least one site."

    try:
        # Perform scraping and get scraping duration
        result, scraping_duration = scrape_with_threading(selected_sites, keyword, CHROME_DRIVER_PATH)

        # Check if the result is empty
        if result is None:
            return render_template('index.html', message=f'Keyword "{keyword}" is not found')
        
        # Calculate total pages
        total_pages = (len(result) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

        # Get the requested page (default to page 1 if not provided)
        page = int(request.args.get('page', 1))

        # Calculate start and end indices for the requested page
        start_idx = (page - 1) * ITEMS_PER_PAGE
        end_idx = start_idx + ITEMS_PER_PAGE
        page_data = result.iloc[start_idx:end_idx].copy()

        # Add a column for numbering
        page_data.insert(0, 'No', range(start_idx + 1, end_idx + 1))

        return render_template(
            'result.html',
            data=page_data,
            keyword=keyword,
            selected_sites=selected_sites,
            page=page,
            total_pages=total_pages,
            scraping_duration=scraping_duration
        )
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)