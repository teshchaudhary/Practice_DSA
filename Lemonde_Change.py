# You are an owner of lemonade island, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by given array bills[]). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# NOTE: At first, you do not have any bill to provide changes with. You can provide changes from the bills that you get from the previous customers.

# Given an integer array bills of size N where bills [ i ] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

def lemonadeChange(N, bills):
        
        if bills[0] == 10 or bills[0] == 20:
            return False
            
        c5 = c10 = 0
        
        for bill in bills:
            if bill == 5:
                c5 += 1
                
            elif bill == 10:
                if c5 < 1:
                    return False
                c5 -= 1
                c10 += 1
                
            elif bill == 20:
                if c10 >= 1 and c5 >= 1:
                    c10 -= 1
                    c5 -= 1
                    
                elif c5 >= 3:
                    c5 -= 3
                    
                else:
                    return False
        
        return True
