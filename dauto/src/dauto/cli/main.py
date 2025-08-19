import click


@click.group()
def cli():
    pass

from dauto.cli.debug.scoop import scoop
cli.add_command(scoop)


if __name__ == "__main__":
    cli()