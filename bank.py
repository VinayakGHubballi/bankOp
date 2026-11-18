import sys

def bankOp(initialAmt, deposit, withdraw):
    totalBal = initialAmt+deposit
    updatedBal = totalBal-withdraw

    return totalBal, updatedBal

if __name__ == "__main__":

    initialAmt = int(sys.argv[1])
    deposit = int(sys.argv[2])
    withdraw = int(sys.argv[3])

    totalBal, updatedBal = bankOp(initialAmt, deposit, withdraw)

    print("Total Bal: ", totalBal)
    print("Updated Bal: ", updatedBal)