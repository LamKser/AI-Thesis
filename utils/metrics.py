import pyiqa

# Reference:
#   https://github.com/chaofengc/IQA-PyTorch?fbclid=IwAR1qqeNCmABtuZsutNPJo5NDRzRz8Nvr5QXkwCU98ju4xOH_Q-r47mnkBuo
def psnr(gt_path, sr_path, test_y_channel=False, color_space='rgb'):
    metric = pyiqa.create_metric('psnr', test_y_channel=test_y_channel, color_space=color_space)
    return metric(gt_path, sr_path)

def ssim(gt_path, sr_path, test_y_channel=False, color_space='rgb'):
    metric = pyiqa.create_metric('ssim', test_y_channel=test_y_channel, color_space=color_space)
    return metric(gt_path, sr_path)

def brisque(sr_path):
    metric = pyiqa.create_metric('brisque')
    return metric(sr_path)

def niqe(sr_path, test_y_channel=False, color_space='rgb'):
    metric = pyiqa.create_metric('niqe', test_y_channel=test_y_channel, color_space=color_space)
    return metric(sr_path)