import  os
from pathlib import  Path
import  subprocess
import  click
from wsp import  add,get_list, get_path
from emoji import  random_emoji

@click.group()
def cli():
    pass


@cli.command()
def list():
    for i in get_list():
        click.echo(f"{random_emoji(6)} ~ {i}")

@cli.command()
@click.argument('name')
def go(name): 
    if os.path.exists(get_path(name)):
        os.chdir(get_path(name))
        os.system('$SHELL')

@cli.command()
@click.argument('name')
@click.argument('path')
def new(name,path):
    add(name,**{'name':name,'path':path})
    
if __name__ == '__main__':
    cli()
