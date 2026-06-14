class OrderError(Exception):
    pass


class ShopService:
    def __init__(self,payment_gateway):
        self.payment_gateway = payment_gateway
        self.orders = []

    def place_order(self,email, product , amount):
        pament = self.payment_gateway.charge(email , amount)
        if pament["status"] != "success":
            raise OrderError("Payment failed")
        
        order = {"email": email, "product": product, "amount": amount}
        self.orders.append(order)
        return order
