# JobDB-HK-Auto-Apply
# Job Scraper for JobsDB

This repository contains a Bash script for scraping job listings from JobsDB, specifically tailored for Hong Kong job listings. The script fetches job postings based on a specified keyword and processes each job URL to extract specific content, generating a comprehensive report.

## Features

- Scrapes job listings from JobsDB based on a given keyword.
- Supports pagination to scrape multiple pages of job listings.
- Extracts job URLs and processes each job page to gather detailed information.
- Generates a report containing job details and application links.
- Cleans up temporary files after execution.

## Prerequisites

- Unix-based operating system (Linux, macOS)
- `curl` installed
- `html2text` installed (can be installed via `sudo apt-get install html2text` on Debian-based systems)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/NeoIsBackAgain/JobDB-HK-Auto-Apply-.git
    cd find_jobs
    ```

2. Make the script executable:

    ```bash
    chmod +x jobfind.sh
    ```

3. Run the script with the desired keyword and number of pages to scrape:

    ```bash
    ./jobfind.sh keyword total_pages
    ```

    - `keyword`: The job search keyword (e.g., `software-developer`).
    - `total_pages`: The number of pages to scrape.

## Example

```bash
./scrape_jobs.sh software-developer 5

