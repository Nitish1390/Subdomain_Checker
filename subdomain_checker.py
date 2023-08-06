import requests
import time
from tabulate import tabulate

# Function for scanning subdomains
def domain_scanner(domain_name, sub_domnames):
    print('-----------Scanner Started-----------')
    print('----URL after scanning subdomains----')

    while True:
        results = []  # List to store results

        # Loop for getting URLs
        for subdomain in sub_domnames:
            # Making URL by putting subdomain one by one
            url = f"https://{subdomain}.{domain_name}"

            # Using try-except block to avoid program crash
            try:
                # Sending GET request to the URL
                response = requests.get(url)

                # If the URL is valid (status code 200), store it as "up"
                status = "up" if response.status_code == 200 else "down"
            except requests.ConnectionError:
                # If URL is invalid, store it as "down"
                status = "down"

            # Append the subdomain and its status to the results list
            results.append({"Subdomain": subdomain, "Status": status})

        # Display the results in tabular format
        table = tabulate(results, headers="keys", tablefmt="grid")
        print(table)

        # Wait for 1 minute before checking again
        time.sleep(60)
        print("\033[H\033[J")  # Clear the terminal for clean output

# Main function
if __name__ == '__main__':
    # Input the domain name
    dom_name = input("Enter the Domain Name: ")
    print('\n')

    # Opening the subdomain text file
    with open('subdomain.txt', 'r') as file:
        # Reading the file and splitting lines to get subdomains
        sub_dom = file.read().splitlines()

    # Call the function for scanning subdomains and getting the URL
    domain_scanner(dom_name, sub_dom)
