import csv

result_error = []
result_valid = []
with open('data/raw/orders.csv', newline= '', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        error_dict = {}
        valid_dict = {}

        try:
            quant = int(row['quantity'])

        except ValueError:
            error_dict['order_id'] = row['order_id']
            error_dict['customer'] = row['customer']
            error_dict['quantity'] = row['quantity']
            error_dict['status'] = "Invalid"
            error_dict['reason'] = "The quantity must be an integer"
            result_error.append(error_dict)

        else:
            if quant <= 0:
                error_dict['order_id'] = row['order_id']
                error_dict['customer'] = row['customer']
                error_dict['quantity'] = row['quantity']
                error_dict['status'] = "Invalid"
                error_dict['reason'] = "Quantity must be greater than 0"
                result_error.append(error_dict)

            else:
               valid_dict['order_id'] = row['order_id']
               valid_dict['customer'] = row['customer']
               valid_dict['quantity'] = quant
               valid_dict['status'] = "Valid"
               valid_dict['reason'] = "-"
               result_valid.append(valid_dict)

    print(result_valid)

    print(result_error)