class Account:

    def __init__(self, ident, owner, amount, password):
        self.ident = ident
        self.owner = owner
        self.amount = amount
        self.password = password

    def buchen(self):
        print('Herzlich Willkommen!')
        benutzereingabe = input('Bitte gib dein Passwort ein:  ')
        if benutzereingabe == self.password:
            print('Was wollen Sie machen?')
            eingabe = int(input('Drücken Sie [1] fürs Abheben und [2] fürs Einzahlen oder [3] für das Beenden:  '))
            if eingabe == 1:
                self.abheben()
            elif eingabe == 2:
                self.einzahlen()
            elif eingabe == 0:
                print('Vielen dank für deinen Besuch!')
            else:
                print('Ungültige Eingabe!')
        else:
            print('Passwort falsch!')

    def abheben(self):
        withdrawn = float(input('Wie viel möchtest du abheben?  '))
        if withdrawn <= self.amount:
            self.amount = self.amount - withdrawn
            print(f'{withdrawn} € wurde von deinem Konto abgehoben!')
            print('Aktueller Restbetrag = ' + str(self.amount))
            self.buchen()
        else:
            print('Der Betrag ist höher als dein aktuelles Guthaben!')
            self.abheben()

    def einzahlen(self):
        withdrawn = float(input('Wie viel möchtest du einzahlen?  '))
        self.amount = self.amount + withdrawn
        print(f'{withdrawn} € wurde auf dein Konto eingezahlt!')
        print('Aktuelles Guthaben = ' + str(self.amount))

        self.buchen()


Alex = Account('1', 'alex', 1000, '1234')

Alex.buchen()
