from vending_app.models import Products

products = [
    {"name": 'Classic Club', "price": 850, 'category': 'sandwich'},
    {"name": 'Spicy Chicken', "price": 550, 'category': 'sandwich'},
    {"name": 'Veggie Delight', "price": 750, 'category': 'sandwich'},
    {"name": 'BBQ Pulled Pork', "price": 700, 'category': 'sandwich'},
    {"name": 'Roast Beef and Swiss', "price": 600, 'category': 'sandwich'},
    {"name": 'Tuna Melt', "price": 800, 'category': 'sandwich'},
    {"name": 'Italian Panini', "price": 650, 'category': 'sandwich'},
    {"name": 'Caprese Sandwich', "price": 750, 'category': 'sandwich'},
    {"name": 'Breakfast BLT', "price": 600, 'category': 'sandwich'},

    {"name": 'Greek Salad', "price": 750, 'category': 'salad'},
    {"name": 'Caesar Salad', "price": 550, 'category': 'salad'},
    {"name": 'Cobb Salad', "price": 700, 'category': 'salad'},
    {"name": 'Spinach Salad', "price": 600, 'category': 'salad'},
    {"name": 'Chicken Avocado Salad', "price": 800, 'category': 'salad'},
    {"name": 'Mediterranean Salad', "price": 650, 'category': 'salad'},
    {"name": 'Caprese Salad', "price": 750, 'category': 'salad'},
    {"name": 'Fruit Salad', "price": 600, 'category': 'salad'},
    {"name": 'Fruit Salad', "price": 600, 'category': 'salad'},

    {"name": 'Cheese and Crackers', "price": 250, 'category': 'snack'},
    {"name": 'Hummus and Veggie Sticks', "price": 350, 'category': 'snack'},
    {"name": 'Yogurt Parfait', "price": 450, 'category': 'snack'},
    {"name": 'Trail Mix', "price": 300, 'category': 'snack'},
    {"name": 'Fruit and Nut Bar', "price": 400, 'category': 'snack'},
    {"name": 'Vegetable Chips', "price": 350, 'category': 'snack'},
    {"name": 'Mini Sandwiches', "price": 500, 'category': 'snack'},
    {"name": 'Cheese Sticks', "price": 350, 'category': 'snack'},
    {"name": 'Cheese Sticks', "price": 350, 'category': 'snack'},

    {"name": 'Orange Juice', "price": 200, 'category': 'drink'},
    {"name": 'Iced Coffee', "price": 300, 'category': 'drink'},
    {"name": 'Lemonade', "price": 250, 'category': 'drink'},
    {"name": 'Green Smoothie', "price": 350, 'category': 'drink'},
    {"name": 'Mango Lassi', "price": 300, 'category': 'drink'},
    {"name": 'Sparkling Water', "price": 200, 'category': 'drink'},
    {"name": 'Iced Tea', "price": 250, 'category': 'drink'},
    {"name": 'Hot Chocolate', "price": 300, 'category': 'drink'},
    {"name": 'Hot Chocolate', "price": 300, 'category': 'drink'},

    {"name": 'Chocolate Brownie', "price": 150, 'category': 'sweet'},
    {"name": 'Apple Pie', "price": 200, 'category': 'sweet'},
    {"name": 'Strawberry Cheesecake', "price": 250, 'category': 'sweet'},
    {"name": 'Cinnamon Roll', "price": 200, 'category': 'sweet'},
    {"name": 'Vanilla Cupcake', "price": 150, 'category': 'sweet'},
    {"name": 'Peanut Butter Cookie', "price": 150, 'category': 'sweet'},
    {"name": 'Fruit Tart', "price": 250, 'category': 'sweet'},
    {"name": 'Ice Cream Sundae', "price": 300, 'category': 'sweet'},
    {"name": 'Ice Cream Sundae', "price": 300, 'category': 'sweet'},
]


for product_data in products:
    product = Products(**product_data)
    product.save()