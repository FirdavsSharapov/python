customer_29876 = {'First Name': 'Fred', 'Last Name': 'Sharapov', 'Address': '505 Elmwood Ave'}
jobs_to_do_list = ['email', 'texting', 'calls']

print(customer_29876["First Name"])

# del customer_29876["Last Name"]
# print(customer_29876["First Name"])

for each_value in customer_29876.keys():
    print(each_value)

for e, each_value in customer_29876.items():
    print("The customer's " + e + " is " + each_value)

customers = [
    {"Customer ID": 0,
     "First Name": "Fred",
     "Last Name": "Sharapov"},
    {"Customer ID": 1,
     "First Name": "David",
     "Last Name": "de Heer"},
    {"Customer ID": 2,
     "First Name": "Faha",
     "Last Name": "Sharapov"},
]

customer_first_name = customers[0]
customer_name = customer_first_name["Last Name"]
len_customer = len(customers)
print(len_customer)
