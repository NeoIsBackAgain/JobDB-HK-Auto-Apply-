#!/bin/bash
keyword="$1"   # Use keyword from the first argument
total_pages=$2  # Adjust this to the total number of pages you want to scrape

# Function to fetch and process job listings from a given page
fetch_job_listings() {
    local page=$1
    if [ "$page" -eq 1 ]; then
        curl -s "https://hk.jobsdb.com/${keyword}-jobs" -o result
    else
        curl -s "https://hk.jobsdb.com/${keyword}-jobs?page=${page}" -o result
    fi

    # Save job URLs to a file
    grep -Eo '<a href="/job/[^"]+"' result | sed 's/<a href="//' | sed 's|^|https://hk.jobsdb.com|' | sed 's/"$//' >> job_urls.txt
}

# Function to process each job URL
process_job_url() {
    local job_url=$1
    echo "Fetching job page: $job_url"
    curl -s "$job_url" | html2text > job_page.html

    # Extract specific content from the job page and append to report
    echo "The apply link is $job_url" >> "$keyword.report.txt"
    grep -Pzo '(?s)Report.*?Be careful' job_page.html >> "$keyword.report.txt"
    echo "------------------------------------------------------------------------------------------------------------------------------------" >> "$keyword.report.txt"
    echo "------------------------------------------------------------------------------------------------------------------------------------" >> "$keyword.report.txt"
    echo "------------------------------------------------------------------------------------------------------------------------------------" >> "$keyword.report.txt"
    echo "------------------------------------------------------------------------------------------------------------------------------------" >> "$keyword.report.txt"
}

# Main script execution
> job_urls.txt  # Clear previous job URLs file

# Fetch and process job listings from the first page
fetch_job_listings 1

# Fetch and process job listings from subsequent pages
for (( page=2; page<=$total_pages; page++ )); do
    fetch_job_listings $page
done

# Loop through each job URL and process the content
while read -r job_url; do
    process_job_url "$job_url"
done < job_urls.txt

rm result job_urls.txt job_page.html  # Clean up temporary files

echo "Job scraping and reporting completed."






