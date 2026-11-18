from bank import bankOp

def test_amount():
    Balance, updatedBal = bankOp(100000, 40000, 0)
    assert Balance == 140000
    assert updatedBal == 140000

def test_with_withdraw():
    Balance, updatedBal = bankOp(200000, 30000, 10000)

    assert Balance == 230000
    assert updatedBal == 220000