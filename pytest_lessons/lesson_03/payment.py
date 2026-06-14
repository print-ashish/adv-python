class Payment:
    def charge(self,email,amount):

        return {
            "status" : "success",
            "transaction_id" : f"txn_{email}_{amount}"
        }