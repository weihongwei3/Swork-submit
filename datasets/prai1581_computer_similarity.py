"""
@author:  sherlock
@contact: sherlockliao01@gmail.com

@author: Chen Shuoyi
@contact: chenshuoyi@whu.edu.cn
"""

import glob
import os
import os.path as osp
from .bases import BaseImageDataset


class PRAI1581SIMILARITY(BaseImageDataset):

    def __init__(self, root='/data0/ReIDData/',
                 verbose=False, **kwargs):
        super(PRAI1581SIMILARITY, self).__init__()
        self.dataset_dir = '../../Dataset/PRAI-1581/similarity/'

        self.train_dir = osp.join(self.dataset_dir)
        self.query_dir = osp.join(self.dataset_dir)
        self.gallery_dir = osp.join(self.dataset_dir)

        self._check_before_run()

        train = self._process_dir(self.train_dir, relabel=True, isquery=False)
        query = self._process_dir(self.query_dir, relabel=False, isquery=True)
        gallery = self._process_dir(self.gallery_dir, relabel=False, isquery=False)

        if verbose:
            print("=> PRAI1581 loaded")
            self.print_dataset_statistics(train, query, gallery)

        self.train = train
        self.query = query
        self.gallery = gallery

        self.num_train_pids, self.num_train_imgs, self.num_train_cams, self.num_train_vids = self.get_imagedata_info(
            self.train)
        self.num_query_pids, self.num_query_imgs, self.num_query_cams, self.num_train_vids = self.get_imagedata_info(
            self.query)
        self.num_gallery_pids, self.num_gallery_imgs, self.num_gallery_cams, self.num_train_vids = self.get_imagedata_info(
            self.gallery)

    def _check_before_run(self):
        """Check if all files are available before going deeper"""
        if not osp.exists(self.dataset_dir):
            raise RuntimeError("'{}' is not available".format(self.dataset_dir))
        if not osp.exists(self.train_dir):
            raise RuntimeError("'{}' is not available".format(self.train_dir))
        if not osp.exists(self.query_dir):
            raise RuntimeError("'{}' is not available".format(self.query_dir))
        if not osp.exists(self.gallery_dir):
            raise RuntimeError("'{}' is not available".format(self.gallery_dir))


    def _process_dir(self, dir_path, relabel=False, isquery=False):
        img_paths = glob.glob(osp.join(dir_path, '*.jpg'))

        pid_container = set()
        for img_path in sorted(img_paths):
            img_name = os.path.basename(img_path)
            name = img_name.split('_')
            pid = int(name[0])
            if pid == -1: continue  # junk images are just ignored
            pid_container.add(pid)
        pid2label = {pid: label for label, pid in enumerate(pid_container)}
        dataset = []
        for img_path in sorted(img_paths):
            img_name = os.path.basename(img_path)
            name = img_name.split('_')
            pid = int(name[0])
            camid = int(name[1])
            if pid == -1: continue  # junk images are just ignored
            assert 0 <= pid <= 1580  # pid == 0 means background
            assert 1 <= camid <= 2
            if isquery: camid -= 1  # index starts from 0
            if relabel: pid = pid2label[pid]

            dataset.append((img_path, pid, camid, 1))
        return dataset