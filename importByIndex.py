import pandas as pd

reader = pd.read_excel(
    "D:\HCMUT\FinalProject231_232\Import_Excel_to_python\input.xlsx",
    sheet_name=0,
    header=2,
)
print(reader.shape[0])
# print(reader.loc[0])
customers = []
label_index = [0, 1, 4, 16]
for i in range(0, reader.shape[0]):
    customer = {
        "ship_code": "",
        "contact_name": "",
        "order_type": "",
        "total_tons": "",
    }
    count = 0
    for i1 in label_index:
        if count == 0:
            customer["ship_code"] = reader.iloc[i, i1]
        elif count == 1:
            customer["contact_name"] = reader.iloc[i, i1]
        elif count == 2:
            customer["order_type"] = reader.iloc[i, i1]
        elif count == 3:
            customer["total_tons"] = reader.iloc[i, i1]
        count += 1
    customers.append(customer)
print(customers)
