class Account:

    def __init__(self, ident, owner, amount, password):
        self.ident = ident
        self.owner = owner
        self.amount = amount
        self.password = password

    def abheben(self):
        benutzereingabe = input('Bitte Passwort eingeben!')
        if benutzereingabe == self.password:
            withdrawn = float(input('Wie viel möchtest du abheben?'))
            if withdrawn <= self.amount:
                self.amount = self.amount - withdrawn
                print(f'{withdrawn} € wurde von deinem Konto abgehoben!')
            else:
                print('Der Betrag ist höher als dein aktuelles Guthaben!')

        else:
            print('Passwort falsch!')


Alex = Account('1', 'alex', 1000, '1234')

Alex.abheben()
print(Alex.amount)
