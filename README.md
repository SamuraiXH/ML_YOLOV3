# ML_YOLOV3
ML_YOLOV3(目标检测)
# ML_YOLOV3
## 1.安装环境
numpy
torch >= 1.1.0
opencv-python
tqdm
## 2.
###迁移学习
train --data data/coco_2cls.data --cfg cfg/yolov3-spp-2cls.cfg --weights weights/converted.pt --transfer
###测试自己的模型
test --data data/coco_1cls.data --weights weights/ultralytics49.pt
###检测并且输出结果：
detect --weights weights/last.pt --cfg cfg/yolov3-spp-1cls.cfg --data data/coco_1cls.data
##3.数据集中图片的规格
maxHeight=1040    maxWeight=2008
##4.lable的归一化处理
https://github.com/ultralytics/yolov3/issues/341
https://github.com/ultralytics/yolov3/issues/524

