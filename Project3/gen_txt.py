#!/usr/bin/env python3

import os
import numpy
import random
import string
import cv2
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', help='Length of captchas in characters', type=int)
    parser.add_argument('--count', help='How many captchas to generate', type=int)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    args = parser.parse_args()

    if args.length is None:
        print("Please specify the captcha length")
        exit(1)

    if args.count is None:
        print("Please specify the captcha count to generate")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    #captcha_generator = captcha.image.ImageCaptcha(width=args.width, height=args.height)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()

    print("Generating captchas with symbol set {" + captcha_symbols + "}")

    with open("audio_captcha.csv", 'w') as output_file:
        for i in range(args.count):
            captcha_text = ' '.join([random.choice(captcha_symbols) for j in range(args.length)])
            output_file.write(captcha_text + "\n")

if __name__ == '__main__':
    main()
