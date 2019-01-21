import click


class Interface:

    def __init__(self):
        self.display_welcome_menu()

    def display_welcome_menu(self):
        print("\t\tWe call this - The Chat Medium")
        print("\n\nChoose from the options below\n\n")

        self.give_access()

    @click.command()
    @click.option('--access', type=click.choice([1, 2]),
                  prompt="You are doing well. Choose a number from below\
                  \n1. Register as new user\n2. Login")
    def give_access(self, access):
        print('You are doing well. Choose a number from below')

        while access != 1 and access != 2:
            click.echo("Illegal choice. Try 1 or 2")
            access = input("\n1. Register as new user\n2. Login")
        if access == 1:
            self.register()
        elif access == 2:
            self.login_user()

    @click.command()
    @click.option('--email', type=str, prompt=True)
    @click.password_option('--password')
    def register(self, value):
        click.echo('User registeration success')
