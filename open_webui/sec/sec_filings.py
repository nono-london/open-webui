import json
import asyncio
from playwright.async_api import async_playwright, Playwright
import json
from open_webui.app_config import get_project_root_path

def read_json_file(file_path):
    # Replace 'yourfile.json' with the path to your JSON file
    filename = 'yourfile.json'

    try:
        # Open the JSON file for reading
        with open(filename, 'r') as file:
            # Parse the JSON data from the file
            data = json.load(file)
        
        # Now `data` is a Python dictionary or list, depending on your JSON structure
        print(data)

    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding the JSON: {e}")
        

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())





def build_sec_url(accession_number, cik:str='0001318605', ):
    """
    Constructs a URL for accessing SEC filings.
    
    :param cik: Central Index Key (CIK) of the company
    :param accession_number: The accession number with dashes
    :return: Formatted URL string
    """
    # Remove dashes from the accession number to form directory path
    accession_without_dashes = accession_number.replace('-', '')
    
    # Construct and return the full URL
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_without_dashes}/{accession_number}-index.htm"

def process_json_file(file_path):
    """
    Reads a JSON file, extracts CIK and accession numbers, 
    and builds URLs for each filing.
    
    :param file_path: Path to the JSON file
    :return: List of constructed URLs
    """
    urls = []
    
    # Open and load the JSON data from the specified file
    with open(file_path, 'r') as file:
        filings_data = json.load(file)
        
        # Assuming the JSON structure has a list of filings under a key
        for filing in filings_data.get('filings', []):
            cik = filing.get('cik')
            accession_number = filing.get('accessionNumber')
            
            if cik and accession_number:
                url = build_sec_url(cik, accession_number)
                urls.append(url)

    return urls



if __name__ == '__main__':
    print(get_project_root_path())

    exit(0)
    # Example usage
    file_path = 'path/to/your/json_file.json'
    urls = process_json_file(file_path)

    for url in urls:
        print(url)
