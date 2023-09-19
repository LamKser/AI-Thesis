import os
from os.path import join, splitext
import random

import cv2




def ger_hr_lr_patches(directory, 
                      border_scale=0.08, scale=4, step=96, size=96,
                      hr_save='hr', lr_save='lr'):
    files = os.listdir(directory)
    # os.makedirs(hr_save, exist_ok=True)
    # os.makedirs(lr_save, exist_ok=True)

    for f in files:
        name, ext = splitext(f)
        try:
            img = cv2.imread(join(directory, f))
        except:
            print(f'Can not read image: {f}')
            continue

        h, w = img.shape[:2]
        xmin, ymin = int(w * border_scale), int(h * border_scale)
        xmax, ymax = w -1 - int(w * border_scale), h - 1 - int(h * border_scale)

        # cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 255), thickness=2)
        # import matplotlib.pyplot as plt
        # plt.imshow(img)
        # plt.show()
        # break
        for i, x in enumerate(range(xmin, xmax - size, step)):
            for j, y in enumerate(range(ymin, ymax - size, step)):
                hr_img = img[y : y + size, x : x + size]
                lr_img = cv2.resize(hr_img, (size//scale, size//scale))
                cv2.imwrite(join(hr_save, f'{name}_{i}{j}_{ext}'), hr_img)
                cv2.imwrite(join(lr_save, f'{name}_{i}{j}_{ext}'), lr_img)
        


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--dir', type=str,
                        help='Images folder', required=True)
    parser.add_argument('--border-scale', '--bs', type=float, default=0,
                        help='Border scale')
    parser.add_argument('--size', '--si', type=int, default=96,
                        help='Size of HR image')
    parser.add_argument('--step', '--st', type=int, default=96,
                        help='Step crop image')
    parser.add_argument('--scale', '--sa', type=int, default=2,
                        help='Scale factor')
    parser.add_argument('--hr_dir', '--hr', type=str, default='hr',
                        help='hr_dir')
    parser.add_argument('--lr_dir', '--lr', type=str, default='lr',
                        help='lr_dir')
    args = parser.parse_args()

    ger_hr_lr_patches(args.dir, args.border_scale, args.scale, args.step, args.size, args.hr_dir, args.lr_dir)
