import json
import asyncio
from playwright.async_api import async_playwright, Playwright
import json
from open_webui.app_config import get_project_download_path
from pathlib import Path
import pandas as pd


def read_json_file(file_path) -> pd.DataFrame | None:

    try:
        # Open the JSON file for reading
        with open(file_path, "r") as file:
            # Parse the JSON data from the file
            data = json.load(file)

        data = pd.DataFrame(data.get("filings").get("recent"))
        print(data.head())
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding the JSON: {e}")

    return data


def build_sec_url(accession_number, cik, doc_name):
    """
    Constructs a URL for accessing SEC filings.

    :param cik: Central Index Key (CIK) of the company
    :param accession_number: The accession number with dashes
    :return: Formatted URL string
    """
    # Remove dashes from the accession number to form directory path
    accession_without_dashes = accession_number.replace("-", "")

    # Construct and return the full URL
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_without_dashes}/{doc_name}"


def process_json_file(file_path, cik) -> pd.DataFrame:
    """
    Reads a JSON file, extracts CIK and accession numbers,
    and builds URLs for each filing.

    :param file_path: Path to the JSON file
    :return: List of constructed URLs
    """
    json_df: pd.DataFrame = read_json_file(file_path)
    json_df["url"] = json_df.apply(
        lambda x: build_sec_url(x["accessionNumber"], cik, x["primaryDocument"]), axis=1
    )

    return json_df


async def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)



if __name__ == "__main__":
    file_path: Path = Path(get_project_download_path(), "CIK0001318605.json")
    print(file_path)
    print(file_path.exists())

    result_df = process_json_file(file_path, "0001318605")
    print(result_df.head())
    print(str(result_df.head(1).values[0][-1]))

    asyncio.run(main())
