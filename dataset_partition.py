# ## PRAI####################################################################################
# import pickle
# import shutil
# import os
#
# f = open('../../Dataset/PRAI-1581/partitions.pkl','rb')
# partition = pickle.load(f)
# # print(partition)
# trainval_im_names = partition['trainval_im_names']
# val_im_names = partition['val_im_names']
# train_im_names = partition['train_im_names']
# test_im_names = partition['test_im_names']
# trainval_ids2labels = partition['trainval_ids2labels']
# train_ids2labels = partition['train_ids2labels']
# val_marks = partition['val_marks']
# test_marks = partition['test_marks']  # 划分query和gallery的标记
#
# f.close()
# print('start process')
#
# # for train_im_i in train_im_names:
# #     source_file = '../../Dataset/PRAI-1581/images/' + train_im_i
# #     destination_path = '../../Dataset/PRAI-1581/partition/bounding_box_train/'
# #     if not os.path.exists(destination_path):
# #         os.makedirs(destination_path)
# #     shutil.copy(source_file, destination_path)
# #
# for trainval_im_i in trainval_im_names:
#     source_file = '../../Dataset/PRAI-1581/images/' + trainval_im_i
#     destination_path = '../../Dataset/PRAI-1581/partition/bounding_box_train/'
#     if not os.path.exists(destination_path):
#         os.makedirs(destination_path)
#     shutil.copy(source_file, destination_path)
#
# print('process train completed and successful, from trainval')
# #
# # for val_im_i in val_im_names:
# #     source_file = '../../Dataset/PRAI-1581/images/' + val_im_i
# #     destination_path = '../../Dataset/PRAI-1581/partition/val/'
# #     if not os.path.exists(destination_path):
# #         os.makedirs(destination_path)
# #     shutil.copy(source_file, destination_path)
# #
# for i in range(len(test_im_names)):
#     test_im_i = test_im_names[i]
#     source_file = '../../Dataset/PRAI-1581/images/' + test_im_i
#     if test_marks[i] == 0:
#         destination_path = '../../Dataset/PRAI-1581/partition/query/'
#     else:
#         destination_path = '../../Dataset/PRAI-1581/partition/gallery/'
#     if not os.path.exists(destination_path):
#         os.makedirs(destination_path)
#     shutil.copy(source_file, destination_path)
#
# print('process query and gallery completed and successful, from test and test_marks')
#
# print('ALL process completed and successful')




# # ## AGReID.v2 ####################################################################################

# ####全部混在一起
# import shutil
# import os
#
# print('start process')
# for (train_dir_path, train_dir_names, train_file_names) in os.walk('../../Dataset/AG-ReID.v2/AG-ReID.v2/train_all'):
#     for train_file_name in train_file_names:
#         source_file = os.path.join(train_dir_path, train_file_name)
#         source_file = source_file.replace('\\', '/')
#         destination_path = '../../Dataset/AG-ReID.v2/partition/train/'
#         if not os.path.exists(destination_path):
#             os.makedirs(destination_path)
#         shutil.copy(source_file, destination_path)
# print('process train completed and successful')
#
# for (query_dir_path, query_dir_names, query_file_names) in os.walk('../../Dataset/AG-ReID.v2/AG-ReID.v2/query'):
#     for query_file_name in query_file_names:
#         source_file = os.path.join(query_dir_path, query_file_name)
#         source_file = source_file.replace('\\', '/')
#         destination_path = '../../Dataset/AG-ReID.v2/partition/query/'
#         if not os.path.exists(destination_path):
#             os.makedirs(destination_path)
#         shutil.copy(source_file, destination_path)
# print('process query completed and successful')
#
# for (gallery_dir_path, gallery_dir_names, gallery_file_names) in os.walk('../../Dataset/AG-ReID.v2/AG-ReID.v2/gallery'):
#     for gallery_file_name in gallery_file_names:
#         source_file = os.path.join(gallery_dir_path, gallery_file_name)
#         source_file = source_file.replace('\\', '/')
#         destination_path = '../../Dataset/AG-ReID.v2/partition/gallery/'
#         if not os.path.exists(destination_path):
#             os.makedirs(destination_path)
#         shutil.copy(source_file, destination_path)
# print('process gallery completed and successful')
#
# print('ALL process completed and successful')


#### 取A-C做验证
import pickle
import shutil
import os

f = open('../../Dataset/AG-ReID.v2/exp1_aerial_to_cctv.txt')
# partition = f.readlines()

print('start process')

for line in f.readlines():
    # print(line)
    source_file = '../../Dataset/AG-ReID.v2/AG-ReID.v2/' + line
    source_file = source_file.replace('\n', '')
    if line.find('query'):
        destination_path = '../../Dataset/AG-ReID.v2/a_c_test/query'
    else:
        destination_path = '../../Dataset/AG-ReID.v2/a_c_test/gallery'
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    shutil.copy(source_file, destination_path)
    # print('move' + source_file + 'to' + destination_path)

f.close()
print('process query and gallery completed and successful, from aerial to cctv test')

# # ## P-DESTRE ####################################################################################

# import os
# import shutil
#
#
# count = 0
# # 遍历文件夹
# def walkFile(file):
#     for root, dirs, files in os.walk(file):
#         # root 表示当前正在访问的文件夹路径
#         # dirs 表示该文件夹下的子目录名list
#         # files 表示该文件夹下的文件list
#
#         # 遍历文件
#         for f in files:
#             global count
#             count += 1
#             # print(os.path.join(root, f))
#         # 遍历所有的文件夹
#         for d in dirs:
#             continue
#             # print(os.path.join(root, d))
#     # print("{} 文件数量一共为:{}".format(file, count))
#
# # walkFile(r'D:\Workspace\uav_reid\Dataset\PRAI-1581\partition')
#
# root_path = '../../Dataset/P-DESTRE/'
# split_file_path = os.path.join(root_path, 'pedestrian_reid_splits/Splits')
# source_fold_path = os.path.join(root_path, 'jpg_Extracted_PIDS')
# file_names = os.listdir(split_file_path)
# print('start process')
# count_dict = dict()
# for file in file_names:
#     file_open = open(os.path.join(split_file_path, file))
#     for img_fold in file_open.readlines():
#         source_subfold_path = os.path.join(source_fold_path, img_fold.replace('\n', ''))
#         walkFile(source_subfold_path)
#         for (img_dir_path, img_dir_names, img_file_names) in os.walk(source_subfold_path):
#             for img_file_name in img_file_names:
#                 source_file = os.path.join(img_dir_path, img_file_name)
#                 source_file = source_file.replace('\\', '/')
#                 destination_path = root_path + 'partition/' + file[:-4]
#                 if not os.path.exists(destination_path):
#                     os.makedirs(destination_path)
#                 shutil.copy(source_file, destination_path)
#     file_open.close()
#     print('process {} completed and successful, img counts is {}'.format(file, count))
#     count_dict[file] = count
#     count = 0
#
# # print(count_dict['Gallery_0.txt'] + count_dict['Query_0.txt'] + count_dict['Train_0.txt'])
# # print(count_dict['Gallery_1.txt'] + count_dict['Query_1.txt'] + count_dict['Train_1.txt'])
# # print(count_dict['Gallery_2.txt'] + count_dict['Query_2.txt'] + count_dict['Train_2.txt'])
# # print(count_dict['Gallery_3.txt'] + count_dict['Query_3.txt'] + count_dict['Train_3.txt'])
# # print(count_dict['Gallery_4.txt'] + count_dict['Query_4.txt'] + count_dict['Train_4.txt'])