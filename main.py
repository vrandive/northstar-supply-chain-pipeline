import csv

def load_orders(file_path):
    csv_data = []
    with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            csv_data.append(row)
        return csv_data

def validate_orders(data):
    result_valid = []
    result_error = []

    for row in data:
        error_dict = {}
        valid_dict = {}
        error = []

        try:
            quant = int(row['quantity'])
            if quant<=0:
                error.append('Quantity must be greater than 0')

        except ValueError:
            error.append('Quantity must be an integer')


        if not row['customer'].strip():
            error.append('Customer cannot be blank')

        if error:
            error_dict['order_id'] = row['order_id']
            error_dict['customer'] = row['customer']
            error_dict['quantity'] = row['quantity']
            error_dict['status'] = "Invalid"
            error_dict['reason'] = ", ".join(error)
            result_error.append(error_dict)
        else:
            valid_dict['order_id'] = row['order_id']
            valid_dict['customer'] = row['customer']
            valid_dict['quantity'] = quant
            valid_dict['status'] = "Valid"
            valid_dict['reason'] = "-"
            result_valid.append(valid_dict)

    return result_valid, result_error


orders = load_orders('data/raw/orders.csv')
valid, invalid = validate_orders(orders)

print(f"Valid Orders: {len(valid)}")
print(f"Valid Records: {valid}")

print(f"Invalid Orders: {len(invalid)}")
print(f"Invalid Records: {invalid}")
