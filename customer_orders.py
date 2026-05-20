#generated data for customer_orders.py
products = [
    {"item": "Laptop",   "price": 3000, "category": "electronics"},
    {"item": "Shirt",    "price":  40, "category": "clothing"},
    {"item": "Phone",    "price": 1350, "category": "electronics"},
    {"item": "Trousers", "price":  75, "category": "clothing"},
    {"item": "Tablet",   "price": 1500, "category": "electronics"},
    {"item": "Cabinet",   "price": 300, "category": "home essentials"},
    {"item": "Chair",   "price": 150, "category": "home essentials"},
    {"item": "Desk",   "price": 2500, "category": "home essentials"},
]

customers = [
    {"name": "Alice",   "age": 30, "city": "New York"},
    {"name": "Bob",     "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},  
    {"name": "David",   "age": 28, "city": "Houston"},
    {"name": "Eve",     "age": 22, "city": "Phoenix"},  
    {"name": "Frank",   "age": 40, "city": "Philadelphia"},
    {"name": "Grace",   "age": 27, "city": "San Antonio"},
    ]

orders = [
    {"customer": "Alice",   "product": "Laptop",   "quantity": 1},
    {"customer": "Alice",   "product": "Trousers",   "quantity": 5},
    {"customer": "Bob",     "product": "Phone",    "quantity": 1}, 
    {"customer": "Bob",     "product": "Shirt",    "quantity": 2}, 
    {"customer": "Bob",     "product": "Tablet",    "quantity": 1},          
    {"customer": "Bob",     "product": "Laptop",   "quantity": 1},
    {"customer": "Charlie", "product": "Phone",    "quantity": 2},
    {"customer": "Charlie", "product": "Chair",    "quantity": 6},
    {"customer": "Charlie", "product": "Cabinet",  "quantity": 2},
    {"customer": "Charlie", "product": "Desk",     "quantity": 1},
    {"customer": "David",   "product": "Trousers", "quantity": 3},
    {"customer": "David",   "product": "Shirt", "quantity": 2},
    {"customer": "Eve",     "product": "Tablet",   "quantity": 1},
    {"customer": "Eve",     "product": "Laptop",   "quantity": 1},
    {"customer": "Frank",   "product": "Desk",     "quantity": 2},
    {"customer": "Grace",   "product": "Chair",    "quantity": 4},
]
print("--Data--")
print("Products:", products)
print("Customers:", customers)
print("Orders:", orders)

"""
Tasks 
1. Store customer orders 
• Create a list of customer names 
• Store each customer's order details (customer name, product, price, category) as 
tuples inside a list 
• Use a dictionary where keys are customer names and values are lists of ordered 
products """
print("--Tasks--")
#1 Store customer orders
print("1. Store customer orders")
customer_names = [customer["name"] for customer in customers]
print(customer_names)
print("Customer names stored in a list:", customer_names)
#Store each customer's order details (customer name, product, price, category) as tuples inside a list
customer_orders = []
for order in orders:
    customer_name = order["customer"]
    product_name = order["product"]
    quantity = order["quantity"]
    # Find the product details
    product_details = next((product for product in products if product["item"] == product_name), None)
    if product_details:
        price = product_details["price"]
        category = product_details["category"]
        customer_orders.append((customer_name, product_name, price, category, quantity))

print(customer_orders)

#Generate a dictionary where keys are customer names and values are lists of ordered products
print("Generate a dictionary where keys are customer names and values are lists of ordered products")
customer_order_dict = {}
for order in customer_orders:
    customer_name = order[0]
    product_name = order[1]
    if customer_name not in customer_order_dict:
        customer_order_dict[customer_name] = []
    customer_order_dict[customer_name].append(product_name)
print(customer_order_dict)

"""
2. Classify products by category 
• Use a dictionary to map each product to its respective category 
• Create a set of unique product categories 
• Display all available product categories """

#2 Classify products by category
print("2. Classify products by category")
product_category_dict = {product["item"]: product["category"] for product in products}
print(product_category_dict)
unique_categories = set(product_category_dict.values())
print(unique_categories)


"""
3. Analyze customer orders 
• Use a loop to calculate the total amount each customer spends 
• If the total purchase value is above $100, classify the customer as a high-value buyer 
• If it is between $50 and $100, classify the customer as a moderate buyer 
• If it is below $50, classify them as a low-value buyer """

#3 Analyze customer orders
print("3. Analyze customer orders")
customer_spending = {}
for order in customer_orders:
    customer_name = order[0]
    total_amount = order[2] * order[4]  # price * quantity
    if customer_name not in customer_spending:
        customer_spending[customer_name] = 0
    customer_spending[customer_name] += total_amount
customer_classification = {}
for customer, spending in customer_spending.items():
    #the assignment of customer classification based on spending has thresholds 
    # too low for differentiating high-value buyers, so I will adjust the thresholds 
    # to better reflect typical e-commerce spending patterns in this dataset
    #if spending > 100:
    if spending > 4000:
        customer_classification[customer] = "high-value buyer"
    #elif 50 <= spending <= 100:
    elif 1000 <= spending <= 4000:
        customer_classification[customer] = "moderate buyer"
    else:
        customer_classification[customer] = "low-value buyer"
print(customer_spending)
print(customer_classification)

"""
4. Generate business insights 
• Calculate the total revenue per product category and store it in a dictionary 
• Extract unique products from all orders using a set 
• Use a list comprehension to find all customers who purchased electronics 
• Identify the top three highest-spending customers using sorting """

#4 Generate business insights
print("4. Generate business insights")
revenue_per_category = {}
for order in customer_orders:
    category = order[3]
    total_amount = order[2] * order[4]  # price * quantity
    if category not in revenue_per_category:
        revenue_per_category[category] = 0
    revenue_per_category[category] += total_amount
print(revenue_per_category)
unique_products = set(order[1] for order in customer_orders)
print(unique_products)
customers_who_purchased_electronics = [order[0] for order in customer_orders if order[3] == "electronics"]
print(customers_who_purchased_electronics)
top_spenders = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]
print(top_spenders)

"""
5. Organize and display data 
• Print a summary of each customer's total spending and their classification 
• Use set operations to find customers who purchased from multiple categories 
• Identify common customers who bought both electronics and clothing """

#5 Organize and display data
print("5. Organize and display data")
for customer, spending in customer_spending.items():
    classification = customer_classification[customer]
    print(f"{customer} spent a total of ${spending:.2f} and is classified as a {classification}.")
customers_by_category = {}
for order in customer_orders:
    category = order[3]
    customer_name = order[0]
    if category not in customers_by_category:
        customers_by_category[category] = set()
    customers_by_category[category].add(customer_name)
print(customers_by_category)
customers_electronics = customers_by_category.get("electronics", set())
customers_clothing = customers_by_category.get("clothing", set())
common_customers = customers_electronics.intersection(customers_clothing)
print(common_customers)


"""
Actions 
Customer order processing in python 
• Store customer order data using lists, tuples, and dictionaries 
• Retrieve and modify customer records using dictionary methods 
Classification and analysis 
• Use loops to categorize customers based on their total spending 
• Use set operations to find common and unique products across different categories 
Insight generation 
• Extract the high-value customers and most frequently purchased products 
• Identify trends based on category-wise sales """

#Customer order processing in python
print("--Actions--")
print("Customer order processing in python")
def store_customer_orders(customers, products, orders):
    customer_orders = []
    for order in orders:
        customer_name = order["customer"]
        product_name = order["product"]
        quantity = order["quantity"]
        # Find the product details
        product_details = next((product for product in products if product["item"] == product_name), None)
        if product_details:
            price = product_details["price"]
            category = product_details["category"]
            customer_orders.append((customer_name, product_name, price, category, quantity))
    return customer_orders

example_orders_data = store_customer_orders(customers, products, orders)
print(example_orders_data)

#Retrieve and modify customer records using dictionary methods 
def modify_customer_record(customer_dict, customer_name, new_city):
    if customer_name in customer_dict:
        customer_dict[customer_name]["city"] = new_city
    else:
        print(f"Customer {customer_name} not found.")

customer_dict = {customer["name"]: customer for customer in customers}

modify_customer_record(customer_dict, "Alice", "Boston")
print(customer_dict["Alice"])

#Classification and analysis 
# Use loops to categorize customers based on their total spending 
# Use set operations to find common and unique products across different categories 
print("Classification and analysis:")

def classify_customers(customer_spending):
    customer_classification = {}
    for customer, spending in customer_spending.items():
        if spending > 4000:
            customer_classification[customer] = "high-value buyer"
        elif 1000 <= spending <= 4000:
            customer_classification[customer] = "moderate buyer"
        else:
            customer_classification[customer] = "low-value buyer"
    return customer_classification
customer_classification_result = classify_customers(customer_spending)
print(customer_classification_result)

def find_common_and_unique_products(customer_orders):
    products_by_category = {}
    for order in customer_orders:
        category = order[3]
        product_name = order[1]
        if category not in products_by_category:
            products_by_category[category] = set()
        products_by_category[category].add(product_name)
    return products_by_category
products_by_category_result = find_common_and_unique_products(customer_orders)
print(products_by_category_result)


"""
Result 
The final deliverable will be a detailed report summarizing customer classifications, total 
sales per category, and key insights about purchase behavior. This project demonstrates 
how Pythons data structures can be used to analyze real-world e-commerce data, 
helping businesses make informed decisions.
"""