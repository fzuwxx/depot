from get_bvid import get_bvid
from get_cid import get_cid
from get_data import get_data
from print_danmu import print_danmu
from save_to_file import save_to_file
import time
import warnings
from word_cloud import citu

'''忽略匹配的警告'''
warnings.filterwarnings("ignore")


def main():

    for i in range(15):
        for j in range(20):
            save_to_file(get_data(get_cid(get_bvid(i, j))))
    time.sleep(1)
    citu()


if __name__ == '__main__':
    main()
    print_danmu()
