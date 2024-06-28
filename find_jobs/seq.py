with open('cybersecuity.report.txt', 'r', encoding='utf-8') as file:
    file_content = file.read()

# Split the file content based on the separator
    job_listings = file_content.split('----------------------------------------\n')

# Process each job listing
    for job in job_listings:
        # Perform operations on each job listing
        print(job.strip())  # Example: Print each job listing (strip removes leading/trailing whitespace)