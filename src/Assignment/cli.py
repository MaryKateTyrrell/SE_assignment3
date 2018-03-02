'''
Created on 2 Mar 2018

@author: mary-katetyrrell
'''
import sys
import click
click.disable_unicode_literals_warning= True

@click.command()
@click.option("--input", default=None, help="input URI (file or URI)")

def main(input=None):
    
    '''console script for lightTest'''
    
    print('input', input)
    return 0

if __name__ == "__main__":
    sys.exit(main())
