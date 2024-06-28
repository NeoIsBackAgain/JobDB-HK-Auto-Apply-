import pandas as pd

# Read the content of the text file
with open('art-teacher.report.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content into individual job postings
job_posts = content.split('Be careful')

# Extract relevant details for each job posting
job_details = []

for job in job_posts:
    lines = job.split('\n')
    title = ''
    company = ''
    location = ''
    category = ''
    job_type = ''
    salary = ''
    posted = ''
    apply_link = ''
    
    for line in lines:
        if 'The apply link is' in line:
            apply_link = line.split(' ')[-1]
        if 'School of Continuing Education' in line:
            company = 'School of Continuing Education, HKBU'
        if 'View all jobs' in line:
            location = 'Hong Kong'
        if 'Tutoring' in line:
            category = 'Tutoring (Education & Training)'
        if 'Part time' in line:
            job_type = 'Part time'
        if 'Posted' in line:
            posted = line.split(' ')[1]
        if 'Food Revolution and Lifestyle' in line:
            title = 'Food Revolution and Lifestyle'
    
    job_details.append([title, company, location, category, job_type, salary, posted, apply_link])

# Create a DataFrame
df = pd.DataFrame(job_details, columns=['Title', 'Company', 'Location', 'Category', 'Job Type', 'Salary', 'Posted', 'Apply Link'])

# Save the DataFrame to an Excel file
df.to_excel('art_teacher_jobs.xlsx', index=True)

