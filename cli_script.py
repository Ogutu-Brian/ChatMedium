import click


class Interface:

    def __init__(self):
        self.display_welcome_menu()

    def display_welcome_menu(self):
        print("\t\tWe call this - The Chat Medium")
        print("\n\nChoose from the options below\n\n")

        give_access()


@click.command()
@click.option('--access', type=click.Choice(['1', '2']),
              prompt="You are doing well. Choose a number from below\
              \n1. Register as new user\n2. Login")
def give_access(access):

    if access == '1':
        register()
    elif access == '2':
        login_user()


@click.command()
@click.option('--email', type=str, prompt=True)
@click.password_option('--password')
def register(email, password):
    click.echo('User registeration success')


@click.command()
@click.option('--email', type=str, prompt=True)
@click.option('--password', prompt="Input password", hide_input=True)
def login_user(email, password):
    click.echo("Logging you in")


if __name__ == '__main__':
    s = Interface()
