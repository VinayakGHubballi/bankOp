def bankOp(initialAmt, deposit, withdraw):
    totalBal = initialAmt+deposit
    updatedBal = totalBal-withdraw

    return totalBal, updatedBal

if __name__ == "__main__":

    initialAmt = int(input("Enter amount as initial balance: "))
    deposit = int(input("Enter amount to deposit: "))
    withdraw = int(input("Enter amount to withdraw"))

    totalBal, updatedBal = bankOp(initialAmt, deposit, withdraw)

    print("Total Bal: ", totalBal)
    print("Updated Bal: ", updatedBal)