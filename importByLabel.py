import pandas as pd

labels = [
    "SHIP CODE",
    "CONTACT NAME",
    "ORDER TYPE",
    "Sum of Total  tons ",
]
reader = pd.read_excel(
    "D:\HCMUT\FinalProject231_232\Import_Excel_to_python\input.xlsx",
    sheet_name=0,
    header=2,
)
print(reader.shape[0])
# print(reader.loc[0])
customers = []


for i in range(0, reader.shape[0]):
    customer = {
        "ship_code": "",
        "contact_name": "",
        "order_type": "",
        "total_tons": "",
    }
    for label in labels:
        if label == "SHIP CODE":
            customer["ship_code"] = reader.at[i, label]
        elif label == "CONTACT NAME":
            customer["contact_name"] = reader.at[i, label]
        elif label == "ORDER TYPE":
            customer["order_type"] = reader.at[i, label]
        elif label == "Sum of Total  tons ":
            customer["total_tons"] = reader.at[i, label]
        # print(reader.at[i, label])
    customers.append(customer)

print(customers)
