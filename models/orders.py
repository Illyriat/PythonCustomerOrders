class Order:
    def __init__(self, customer_name, order_date, quantity, order_number,description, shipping_status, delivered, chargeAmount):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.order_number = order_number
        self.description = description
        self.shipping_status = shipping_status
        self.delivered = delivered
        self.chargeAmount = chargeAmount