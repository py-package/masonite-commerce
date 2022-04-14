from masonite.commands import Command

class MasoniteCommerce(Command):
    """
    Description of Command

    commerce:demo
        {user : A positional argument for the command}
        {--f|flag : An optional argument for the command}
        {--o|option=default: An optional argument for the command with default value}
    """

    def handle(self):
        self.info("Info Message")
