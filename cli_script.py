import click
import os

from utils import verify_email


class Interface:

    def __init__(self):
        self.display_welcome_menu()

    def display_welcome_menu(self):
        print("\t\tWe call this - The Chat Medium")
        print("\n\nChoose from the options below\n\n")

        give_access()


@click.command()
@click.option('--access', type=click.Choice(['1', '2']),
              prompt="\nChoose a number from below\
              \n1. Register as new user\n2. Login")
def give_access(access):

    if access == '1':
        register()
    elif access == '2':
        login_user()


@click.command()
@click.option('--email', type=str, prompt=True)
@click.option('--firstName', type=str, prompt=True)
@click.option('--LastName', type=str, prompt=True)
@click.password_option('--password')
def register(email, password):
    click.echo("\nYou are doing well")
    email = verify_email(email)
    click.echo('User registeration success')


@click.command()
@click.option('--email', type=str, prompt=True)
@click.option('--password', prompt="Input password", hide_input=True)
def login_user(email, password):
    email = verify_email(email)
    click.echo("Logging you in")


def display_logged_in_menu():
    os.system('clear')
    print("\nChoose from Below\n")
    print("1. Add comment")
    print("2. Display comments")

    choose_comment_action()


@click.command()
@click.option("--your_choice", prompt=True, type=click.Choice(['1', '2']))
def choose_comment_option(your_choice):
    if your_choice == 1:
        add_user_comment()
    elif your_choice == 2:
        display_all_comments()


if __name__ == '__main__':
    s = Interface()
