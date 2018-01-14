#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    IgnoriPy is a script to quicky generate a `.gitignore`
    when starting new projects. This makes use of https://gitignore.io
    under the hood to make it happen.

    Be sure to check the generated `.gitignore` and modify them
    at your own discretion.

    This module is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    General Public V3 License for more details.
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
import os
import sys
import argparse
from builtins import input
from . import GitIgnore
from . import GitIgnoreError

__author__ = 'Meenakshi Sundaram V'
__maintainer__ = 'Meenakshi Sundaram <vms20591@gmail.com>'
__version__ = '1.0.0'
__license__ = 'GPL V3'


def format_error(error, language):
    """
    Pretty print errors

        :param error: Exception to pretty print
        :param language: Language that GitIgnore was processing
        
        :return: Returns formatted error message
        :rtype: unicode
    """
    message = "# Language: {0}\n# Error: {1}"
    language = language or "N/A"
    error = unicode(error) if error else "N/A"

    message = message.format(language, error)

    return message


def banner():
    """
    Displays the welcome message
    """
    welcome = """
▄█     ▄██████▄  ███▄▄▄▄    ▄██████▄     ▄████████  ▄█     ▄███████▄ ▄██   ▄   
███    ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███ ███   ██▄ 
███▌   ███    █▀  ███   ███ ███    ███   ███    ███ ███▌   ███    ███ ███▄▄▄███ 
███▌  ▄███        ███   ███ ███    ███  ▄███▄▄▄▄██▀ ███▌   ███    ███ ▀▀▀▀▀▀███ 
███▌ ▀▀███ ████▄  ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ███▌ ▀█████████▀  ▄██   ███ 
███    ███    ███ ███   ███ ███    ███ ▀███████████ ███    ███        ███   ███ 
███    ███    ███ ███   ███ ███    ███   ███    ███ ███    ███        ███   ███ 
█▀     ████████▀   ▀█   █▀   ▀██████▀    ███    ███ █▀    ▄████▀       ▀█████▀  
                                         ███    ███                             
    """

    print(welcome)


def build_parser():
    """
    Builds argument parser and adds the following arguments,

    1) language - Type: str, Required: True

    :return: Returns parsed command line arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("language", help="Lanugauge to generate .gitignore for.")

    return parser.parse_args()


def main():
    """
    Main method that orchestrates and handles errors
    """
    language = "N/A"
    overwrite = 1

    try:
        banner()
        
        api_endpoint = os.environ.get("GITIGNORE.IO.ENDPOINT", "https://gitignore.io/api")
        arguments = build_parser()

        language = arguments.language.lower()

        gitignore = GitIgnore(api_endpoint, language)

        ignore = gitignore.get()

        if os.path.exists(".gitignore") and os.path.isfile(".gitignore"):
            overwrite_message = "A .gitignore already exists, overwrite? (y/n - default: y)- "
            overwrite = unicode(input(overwrite_message)) or "y"

            if overwrite not in ["y", "Y"]:
                overwrite = 0

        if overwrite and ignore != "":
            with open(".gitignore", "wb") as file_handle:
                file_handle.write(ignore)

            print(".gitnore generated")

        print("Exiting.")
        return 0
    except KeyboardInterrupt:
        print("Exiting.")
        return 0
    except GitIgnoreError as gitignore_error:
        print(format_error(gitignore_error, language))
        return 1
    except ValueError as value_error:
        print(format_error(value_error, language))
        return 1
    except argparse.ArgumentError as argument_error:
        print(format_error(argument_error, language))
        return 1
    except argparse.ArgumentTypeError as argument_type_error:
        print (format_error(argument_type_error, language))
        return 1

if __name__ == "__main__":
    sys.exit(main())
