from os.path import join, basename, splitext, exists
import os

import cv2


def cut_frame(video_path, fps_step, save_dir):
    name = splitext(basename(video_path).split('/')[0])[0]
    extention = '.jpg'
    cap = cv2.VideoCapture(video_path)
    fps = 0
    
    # Create folder
    if not exists(save_dir):
        print(f'Directory "{save_dir}" not exist')
        print(f'Creating "{save_dir}"..........')
        os.makedirs(save_dir)
    else:
        print(f'Directory "{save_dir}" already exist')
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:     
            if fps % fps_step == 0:
                cv2.imwrite(join(save_dir, f'{name}_{fps}.{extention}'), frame)
            fps = fps + 1
        else: 
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--path', '-p', type=str, required=True,
                        help='Video path')
    parser.add_argument('--step', '-st', type=int, default=30,
                        help='Step cut frame')
    parser.add_argument('--save', '-sa', type=str,
                        help='Save directory')
    args = parser.parse_args()


    cut_frame(args.path, args.step, args.save)