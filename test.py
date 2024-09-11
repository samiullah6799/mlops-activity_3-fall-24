from main import Account

account = Account(500)

def test_getAmountMethod():
    assert account.getAmount() == 500

def test_depositMethod():
    account.deposit(500)
    assert account.getAmount() == 1000

def test_withDrawMethod():
    account.withDraw(500)
    assert account.getAmount() == 500