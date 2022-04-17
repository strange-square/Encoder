#!/bin/python3
import argparse
import sys
from ast import literal_eval

from caesar import caesar_encode, caesar_decode
from vigenere import vigenere_encode, vigenere_decode
from vernam import vernam_encode, vernam_decode
from hack_and_train import caesar_hack, analyse


def text_input(args):
    return args.input_f.read() if args.input_f else sys.stdin.read()


def res_output(args, res):
    args.output_f.write(res) if args.output_f else sys.stdout.write(res)


def encode(args):
    text = text_input(args)

    if args.cipher == 'caesar':
        if not args.key.isdigit():
            print('Key is not a number')
            return

        args.key = int(args.key)
        res = caesar_encode(args.key, text)

    elif args.cipher == 'vigenere':
        if not args.key.isalpha():
            print('Key is not a word')
            return

        res = vigenere_encode(args.key, text)
    
    elif args.cipher == 'vernam':
        if not 0 <= int(args.key) <= 25:
            print('The key is not a number from the [0, 25]')
            return

        args.key = int(args.key)
        res = vernam_encode(args.key, text)

    res_output(args, res)


def decode(args):
    text = text_input(args)

    if args.cipher == 'caesar':
        if not args.key.isdigit():
            print('key is not digit')
            return

        args.key = int(args.key)
        res = caesar_decode(args.key, text)

    elif args.cipher == 'vigenere':
        if not args.key.isalpha():
            print('key is not word')
            return

        res = vigenere_decode(args.key, text)

    elif args.cipher == 'vernam':
        if not 0 <= int(args.key) <= 25:
            print('The key is not a number from the [0, 25]')
            return

        args.key = int(args.key)
        res = vernam_decode(args.key, text)

    res_output(args, res)


def train(args):
    text = text_input(args)
    args.model_f.write(str(analyse(text)))


def hack(args):
    text = text_input(args)
    model = literal_eval(args.model_f.read())
    res = caesar_hack(text, model)
    res_output(args, res)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Work with caesar, vigenere, vernam ciphers')
    subparsers = parser.add_subparsers(dest='cmd')

    funcs = []

    encoder = subparsers.add_parser('encode')
    encoder.set_defaults(func=encode)
    funcs.append(encoder)

    decoder = subparsers.add_parser('decode')
    decoder.set_defaults(func=decode)
    funcs.append(decoder)

    for func in funcs:
        func.add_argument(
        '--cipher', choices=['caesar', 'vigenere', 'vernam'], dest='cipher', required=True)
        func.add_argument('--key', dest='key', required=True)


    hacker = subparsers.add_parser('hack')
    hacker.set_defaults(func=hack)
    funcs.append(hacker)
    hacker.add_argument('--model-file', dest='model_f',
                        type=argparse.FileType('r'), required=True)

    for func in funcs:
        func.add_argument('--input-file', dest='input_f',
                        type=argparse.FileType('r'))
        func.add_argument('--output-file', dest='output_f',
                        type=argparse.FileType('w'))

    trainer = subparsers.add_parser('train')
    trainer.set_defaults(func=train)
    trainer.add_argument('--text-file', dest='input_f',
                         type=argparse.FileType('r'))
    trainer.add_argument('--model-file', dest='model_f',
                         type=argparse.FileType('w'), required=True)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
    else:
        args.func(args)
