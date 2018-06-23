#!/usr/bin/env python3

"""pyrename 1.0.9
Copyright (c) 2016-2018, Jordan Dunn.

Usage:
    photorename [--md5 | --sha256 | --sha512] -i <input_file> -o <output_dir>
    photorename [-h | --help]

Options:
    -a --all            Rename all files in the current directory
    -i --input_file     Set the file to be renamed
    -o --ouput_path     The path to output the file to
    -h --help           Display this message
    --md5               Use md5 to generate the file name
    --sha256            Use sha256 to generate the file name
    --sha512            Use sha512 to generate the file name
"""

import os
import os.path
import sys
from hashlib import md5, sha256, sha512
from docopt import docopt

args = docopt(__doc__, version='photorename v1.0.9')


def get_md5_string(input_file):
    m = md5()
    m.update(input_file)
    md5string = str(m.hexdigest())
    return md5string


def get_sha256_string(input_file):
    s = sha256()
    s.update(input_file)
    sha256string = str(s.hexdigest())
    return sha256string


def get_sha512_string(input_file):
    s = sha512()
    s.update(input_file)
    sha512string = str(s.hexdigest())
    return sha512string


def rename():
    try:
        print("Input File: " + os.path.realpath(args.input_file))
        input_file = os.path.realpath(args.input_file)
    except TypeError:
        print("You must specify an input file.")
        sys.exit(1)

    _, file_extention = os.path.splitext(input_file)

    if args.output_path:
        output_path = os.path.realpath(args.output_path) + "/"
    else:
        output_path = os.getcwd() + "/"

    if args.md5:
        file_name = get_md5_string(args.input_file.encode('utf-8')) + file_extention
        output_file = f"{output_path}/{file_name}"
    elif args.sha256:
        file_name = get_sha256_string(args.input_file.encode('utf-8')) + file_extention
        output_file = f"{output_path}/{file_name}"
    elif args.sha512:
        file_name = get_sha512_string(args.input_file.encode('utf-8')) + file_extention
        output_file = f"{output_path}/{file_name}"

    try:
        print(f"Output File: {output_file}")
        os.rename(input_file, output_file)
    except IOError as error:
        print(error)
        sys.exit(1)


if __name__ == '__main__':
    print(__doc__)
