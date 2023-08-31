import pandas as pd

def extract_emails_from_file(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        print("Unsupported file format")
        return
    
    # adjust column name as needed
    emails = df['email']
    
    # extract username and domain
    email_parts = [email.split('@') for email in emails]
    usernames = [parts[0] for parts in email_parts]
    domains = [parts[1] for parts in email_parts]
    
    
    new_df = pd.DataFrame({'Username': usernames, 'Domain': domains})
    
    # new CSV file
    new_file_path = 'extracted_emails.csv'
    new_df.to_csv(new_file_path, index=False)
    
    print(f"Extracted emails saved to {new_file_path}")

# path file containing emails
file_path = 'EmailChecker.csv'  # Change this to your file's path
extract_emails_from_file(file_path)
