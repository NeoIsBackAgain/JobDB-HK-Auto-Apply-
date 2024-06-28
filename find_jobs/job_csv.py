import csv

# Function to parse job listings from the text data
def parse_job_listings(file_content):
    # Split the file content based on the separator
    job_listings = file_content.split('Be careful--------------------------------------------------------------------------------------------')
    
    parsed_jobs = []
    
    for job in job_listings:
        if job.strip():  # Ignore empty splits
            job_details = {}
            lines = job.strip().split('\n')
            
            # Extract apply link
            apply_link_line = next((line for line in lines if 'The apply link is' in line), None)
            if apply_link_line:
                job_details['Apply Link'] = apply_link_line.split(' ')[-1]
            
            # Extract job title
            job_title_line = next((line for line in lines if '******' in line), None)
            if job_title_line:
                job_details['Job Title'] = job_title_line.strip('* ')
            
            # Extract company
            company_line = next((line for line in lines if 'View all jobs' in line), None)
            if company_line:
                company_index = lines.index(company_line) - 1
                job_details['Company'] = lines[company_index]
            
            # Extract location
            location_line = next((line for line in lines if 'Security (' in line), None)
            if location_line:
                location_index = lines.index(location_line) - 1
                job_details['Location'] = lines[location_index]
            
            # Extract job type and salary
            job_type_salary_index = next((i for i, line in enumerate(lines) if 'Posted' in line), None)
            if job_type_salary_index:
                job_type_salary_lines = lines[job_type_salary_index-2:job_type_salary_index]
                job_details['Job Type'] = job_type_salary_lines[0] if len(job_type_salary_lines) > 0 else ''
                job_details['Salary'] = job_type_salary_lines[1] if len(job_type_salary_lines) > 1 else ''
            
            # Extract posted date
            posted_date_line = next((line for line in lines if 'Posted' in line), None)
            if posted_date_line:
                job_details['Posted Date'] = posted_date_line.split(' ')[1]
            
            # Extract description and profile
            try:
                description_index = lines.index('Description')
                profile_index = lines.index('Profile')
                
                job_details['Description'] = ' '.join(lines[description_index+1:profile_index]).strip()
                job_details['Profile'] = ' '.join(lines[profile_index+1:lines.index('Job Offer')]).strip()
            except ValueError:
                job_details['Description'] = ''
                job_details['Profile'] = ''
            
            # Extract job offer
            job_offer_line = next((line for line in lines if 'Job Offer' in line), None)
            if job_offer_line:
                try:
                    job_details['Job Offer'] = ' '.join(lines[lines.index(job_offer_line)+1:lines.index('To apply online please click the \'Apply\' button below.')]).strip()
                except ValueError:
                    job_details['Job Offer'] = ''
            
            parsed_jobs.append(job_details)
    
    return parsed_jobs

# Read job listings from file
with open('cybersecuity.report.txt', 'r', encoding='utf-8') as file:
    file_content = file.read()

# Parse job listings
parsed_jobs = parse_job_listings(file_content)

# Define CSV file headers
headers = ['Apply Link', 'Job Title', 'Company', 'Location', 'Job Type', 'Salary', 'Posted Date', 'Description', 'Profile', 'Job Offer']

# Write parsed job listings to CSV file
with open('job_listings.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
    csvwriter.writeheader()
    csvwriter.writerows(parsed_jobs)

print("CSV file 'job_listings.csv' created successfully.")
