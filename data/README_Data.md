# AI Capstone Project: Enhance the Quality and Color of Underwater Images
# Members
* Advisor: Nguyen Quoc Trung
* Dinh Hoang Lam
* Tran Duy Ngoc Bao

# How to run
* `data`
    
    **Create LR HR pair data from HR images**
    ```
    python data/create_dataset.py --dir <image folder>
    ```
    
    * Optional arguments
        * `--border-scale` : crop border of image base on scale of image shape (default: 0)
        * `--size` :  size of HR image (default: 96)
        * `--step` : step of window crop (default: 96)
        * `--scale` : scale factor for resizing image (default: 2)
        * `--hr-dir` , `--lr-dir` : HR and LR folder for saving crop images (default: 'hr', 'lr')

