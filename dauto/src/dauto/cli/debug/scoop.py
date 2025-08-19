
import click
from zuu.scoop import scoop_list_filter, ScoopEntry

from dauto.utils.scoop import get_gauto_index

@click.group()
def scoop():
    pass

@scoop.command("list")
def _list():
    """List all gauto packages"""
    for pkg in scoop_list_filter(bucket_match="gauto"):
        pkg : ScoopEntry
        print(pkg["name"],"\t\t  ", pkg["version"], "\t\t  ", pkg["updated"])

@scoop.command("index")
def index():
    """List all packages in the gauto bucket."""
    installed = {x["name"][3:] : x for x in scoop_list_filter(bucket_match="gauto")}

    for name in get_gauto_index():
        if name in installed:
            print(f"{name} (installed)")
        else:
            print(name)