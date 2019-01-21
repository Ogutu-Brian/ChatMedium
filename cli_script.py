import click


class Interface:

    def __init__(self):
        self.display_welcome_menu()

    def display_welcome_menu(self):
        print("\t\tWe call this - The Chat Medium")
        print("\n\nChoose from the options below\n\n")

        self.give_access()

    @click.command()
    @click.option('--access', type=int,
                  prompt="You are doing well. Choose a number from below\
                  \n1. Register as new user\n2. Login")
    def give_access(self, access):
        print('You are doing well. Choose a number from below')

        while access != 1 and access != 2:
            click.echo("Illegal choice. Try 1 or 2")
            access = input("\n1. Register as new user\n2. Login")
