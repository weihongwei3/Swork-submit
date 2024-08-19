# train
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distributed.launch --nproc_per_node=4 --master_port 66666 train.py --config_file configs/PRAI-1581/vit_transreid_stride_384.yml MODEL.DIST_TRAIN True
CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch --nproc_per_node=4 --master_port 66666 train.py --config_file configs/UAV-Human/vit_transreid_stride_384_4090.yml MODEL.DIST_TRAIN True
python -m torch.distributed.launch --nproc_per_node=1 --nnodes 2 --node_rank 0 --master_addr=192.168.100.147 --master_port 36635 train.py --config_file configs/UAV-Human/vit_transreid_stride_384_4090.yml MODEL.DIST_TRAIN True
python -m torch.distributed.launch --nproc_per_node=1 --nnodes 2 --node_rank 1 --master_addr=192.168.100.147 --master_port 36635 train.py --config_file configs/UAV-Human/vit_transreid_stride_384_4090.yml MODEL.DIST_TRAIN True

# test
python test.py --config_file configs/VehicleID/vit_base.yml MODEL.DIST_TRAIN False MODEL.DEVICE_ID "('0')"


# 单卡训练
# UAVHuman
python train.py --config_file configs/UAV-Human/vit_transreid_stride_384_A10.yml
# PRAI-1581
python train.py --config_file configs/PRAI-1581/vit_transreid_stride_384_A10.yml
# AG-ReID.v2
python train.py --config_file configs/AG-ReID.v2/vit_transreid_stride_384_A10.yml
# P-DESTRE
python train.py --config_file configs/P-DESTRE/vit_transreid_stride_384_A10.yml