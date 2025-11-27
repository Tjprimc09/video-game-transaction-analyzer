import csv

def get_valid_filename():
    # Prompt user for a valid CSV filename
    
    while True:
        filename = input("Enter the CSV filename you wish to read:\n")
        if filename == "":
            print("\nFilename cannot be empty. Please try again.\n")
            continue
        if not filename.endswith('.csv'):
            filename += '.csv'
        try:
            with open(filename, 'r') as file:
                return filename
        except FileNotFoundError:
            print(f"\nFile '{filename}' not found. Please check your input and try again.\n")


def read_transactions(filename):
    # Read and process transactions from the CSV file
    
    transactions = []
    not_included = []
    
    with open(filename, 'r') as f:
        rows = csv.DictReader(f)
        for row in rows:
            if not row['TransactionID'].startswith('VG'):
                print(f'Transaction not included: {row}\n')
                print(f'Transaction ID appears unrelated to video game sales.\n')
                not_included.append(row)
                print('Continuing processing...\n')
                continue
            try:
                amount = f"{float(row['Price']) * int(row['Quantity']):.2f}" #fixed to make sure processed data has only 2 decimal places
                row['Amount'] = float(amount)
                transactions.append(row)

                '''
                if int(row['Quantity']) == 1:
                    row['Popularity'] = 'Low'
                elif int(row['Quantity']) == 2:
                    row['Popularity'] = 'Moderate'
                elif int(row['Quantity']) >= 3:
                    row['Popularity'] = 'Hot Seller'
                '''
            
            except ValueError:
                print(f"Transaction not included: {row}\n")
                print('Could not convert data types properly.\n')
                not_included.append(row)
                print('Continuing processing...\n')
            
            except KeyError:
                print(f'Transaction not included: {row}\n')
                print('Could not find expected fields.\n')
                not_included.append(row)
                print('Continuing processing...\n')
        
        print('Processing completed.\n')
        print(f'Valid transactions processed: {len(transactions)}\n')
        print(f'Transactions not included: {len(not_included)}\n')   
    
    return transactions


def calculate_average_spent(transactions):
    # Calculate average amount spent per transaction
    
    if not transactions:
        return 0.00
    
    amts = [t['Amount'] for t in transactions]
    average = sum(amts) / len(amts)
    return average


def find_top_selling_games(transactions):
    # Identify top 3 selling games by total sales amount
    game_totals = {}

    for t in transactions:
        game_totals[t['GameTitle']] = game_totals.get(t['GameTitle'], 0) + t['Amount']

    ordered_sales = sorted(game_totals.items(), key = lambda x:x[1], reverse = True)
    top3 = ordered_sales[:3]
    
    print("\n--- Top 3 Best-Selling Games ---\n")
    for i, sale in enumerate(top3):
        print(f'{i+1} - Title: {sale[0]}, Total Sales: ${sale[1]:.2f}')

    return 

def mark_popularity(transactions):
    # Mark games' popularity based on quanity sold
    '''
    low = []
    moderate = []
    hot = []
    '''
    for t in transactions:
        if int(t['Quantity']) == 1:
            t['Popularity'] = 'Low'
            #low.append(t)
        elif int(t['Quantity']) == 2:
            t['Popularity'] = 'Moderate'
            #moderate.append(t)
        elif int(t['Quantity']) >= 3:
            t['Popularity'] = 'Hot Seller'
            #hot.append(t)
    '''
    print("\nGame popularity marked based on quantity sold.\n")

    print("Unpopular games:\n")
    for i in low:
        print(f'{i['GameTitle']}')
    print()

    print("Moderately popular games:\n")
    for i in moderate:
        print(f'{i['GameTitle']}')
    print()

    print("Hot sellers:\n")
    for i in hot:
        print(f'{i['GameTitle']}')
    print()
    ''' 
    
        
    
    return transactions

def display_summary(transactions):
        print(f"Total Transactions: {len(transactions)}")
        print(f"Total Revenue: ${sum([t['Amount'] for t in transactions]):.2f}")
        print(f"Average transaction value: ${calculate_average_spent(transactions):.2f}")

def find_top_customer(transactions):
    # Identify top customer by total spending

    customer_spending = {}

    for t in transactions:
        customer_spending[t['Customer']] = customer_spending.get(t['Customer'], 0) + t['Amount']

    top_customer = max(customer_spending.items(), key=lambda x: x[1])
    
    print(f'\n--- Top Spending Customer ---\n')
    print(f'{top_customer[0]}, Total Spending: ${top_customer[1]:.2f}\n')

def save_to_csv(transactions, filename):
    # Save processed transactions to a new CSV file

    ofile = "processed_" + filename
    
    with open(ofile, 'w') as f:
        writer = csv.DictWriter(f, fieldnames = transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)
    
    print(f'Processed data saved to {ofile}\n')  

def menu():
    return {
        '1': 'Display Summary of Statistics',
        '2': 'Find Top Selling Games',
        '3': 'Find Top Customer',
        '4': 'Save Processed Data to CSV',
        '5': 'Exit'
    }  

def menu_selection(menu):
    #Display menu and get a selection
    print("\nMENU")
    for key, value in menu.items():
        print(f'{key}. {value}')
    
    while True:
        choice = input("\nEnter your choice (1-5):\n")
        if not menu.get(choice):
            print("\nInvalid selection. Please try again.\n")
            continue
        return choice
    
def route_selection(transactions, filename):
    #Call menu_selection to continously show menu and get a choice until the user decides to exit.
    while True:
        choice = menu_selection(menu())
        if choice == '1':
            display_summary(transactions)
            continue
        elif choice == '2':
            find_top_selling_games(transactions)
            continue
        elif choice == '3':
            find_top_customer(transactions)
            continue
        elif choice == '4':
            save_to_csv(transactions, filename)
            continue
        elif choice == '5':
            print("Exiting program. Goodbye!")
            return False
        return True

def main():
    filename = get_valid_filename()
    transactions = read_transactions(filename)
    mark_popularity(transactions)#From an architectural POV: Why not just do this work in read_transactions(), cleaning all the data before returning transactions?
    if not route_selection(transactions, filename):
        return
    

if __name__ == "__main__":
    main()
        
        
