def bankOp(initialAmt, deposit, withdraw):
    totalBal = initialAmt+deposit
    updatedBal = totalBal-withdraw

    return totalBal, updatedBal

if __name__ == "__main__":

    initialAmt = int(input("Enter amount as initial balance: "))
    deposit = int(input("Enter amount to deposit: "))
    print("Total Balance: ", bankOp(initialAmt, deposit, 0))
    withdraw = int(input("Enter amount to withdraw"))
    print("Updated Balance: ", bankOp(initialAmt, deposit, withdraw))