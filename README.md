# JobDB-HK-Auto-Apply
Job Scraper for JobsDB
This repository contains a Bash script for scraping job listings from JobsDB, specifically tailored for Hong Kong job listings. The script fetches job postings based on a specified keyword and processes each job URL to extract specific content, generating a comprehensive report.

Features
Scrapes job listings from JobsDB based on a given keyword.
Supports pagination to scrape multiple pages of job listings.
Extracts job URLs and processes each job page to gather detailed information.
Generates a report containing job details and application links.
Cleans up temporary files after execution.
Prerequisites
Unix-based operating system (Linux, macOS)
curl installed
html2text installed (can be installed via sudo apt-get install html2text on Debian-based systems)
Usage
Clone the repository:

bash
複製程式碼
git clone https://github.com/yourusername/job_scraper.git
cd job_scraper
Make the script executable:

bash
複製程式碼
chmod +x scrape_jobs.sh
Run the script with the desired keyword and number of pages to scrape:

bash
複製程式碼
./scrape_jobs.sh keyword total_pages
keyword: The job search keyword (e.g., software-developer).
total_pages: The number of pages to scrape.
Example
bash
複製程式碼
./scrape_jobs.sh software-developer 5
This command will scrape the first 5 pages of software developer job listings from JobsDB and generate a report named software-developer.report.txt.

Output
job_urls.txt: Contains the URLs of all job listings.
keyword.report.txt: The final report containing extracted job details and application links.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
