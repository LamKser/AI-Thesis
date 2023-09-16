import os
from os.path import join, splitext
from random import randint

import cv2


def get_pair_images(lr_directory, hr_directory, scale=4, step=96):
    # lr_files = sorted(os.listdir(lr_directory))
    # hr_files = sorted(os.listdir(hr_directory))

    # for lr, hr in zip(lr_files, hr_files):
    #     # Read image BGR
    #     lr_img = cv2.imread(join(lr_directory, lr))
    #     hr_img = cv2.imread(join(hr_directory, hr))

    #     # Get image height, width
    #     h_lr, w_lr = lr_img.shape[:2]
    #     h_hr, w_hr = hr_img.shape[:2]
    pass


def ger_hr_lr_patches(directory, scale=4, step=96, size=96,
                      hr_save='hr', lr_save='lr'):
    files = os.listdir(directory)
    os.makedirs(hr_save, exist_ok=True)
    os.makedirs(lr_save, exist_ok=True)

    for f in files:
        name, ext = splitext(f)
        try:
            img = cv2.imread(join(directory, f))
        except:
            print(f'Can not read image: {f}')
            continue

        h, w = img.shape[:2]
        for i, x in enumerate(range(0, h - size, step)):
            for j, y in enumerate(range(0, w - size, step)):
                hr_img = img[y : y + size, x : x + size]
                lr_img = cv2.resize(hr_img, (size//scale, size//scale))
                cv2.imwrite(join(hr_save, f'{name}_{i}{j}_{ext}'), hr_img)
                cv2.imwrite(join(lr_save, f'{name}_{i}{j}_{ext}'), lr_img)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--directory', '--dir', type=str,
                        help='Images folder', required=True)
    parser.add_argument('--size', '--si', type=int, default=96,
                        help='Size of HR image')
    parser.add_argument('--step', '--st', type=int, default=96,
                        help='Step crop image')
    parser.add_argument('--scale', '--sa', type=int, default=4,
                        help='Scale factor')
    parser.add_argument('--hr_directory', '--hr', type=str, default='hr',
                        help='hr_dir')
    parser.add_argument('-lr_directory', '--lr', type=str, default='lr',
                        help='lr_dir')
    args = parser.parse_args()

    ger_hr_lr_patches(args.directory, args.scale, args.step, args.size, args.hr_directory, args.lr_directory)