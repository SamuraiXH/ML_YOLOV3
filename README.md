# ML_YOLOV3
ML_YOLOV3(目标检测)
# ML_YOLOV3
## 1.安装环境
numpy

torch >= 1.1.0

opencv-python

tqdm
## 2.总流程
### 迁移学习
python3 train.py --data data/coco_2cls.data --cfg cfg/yolov3-spp-2cls.cfg --weights weights/converted.pt --transfer
### 测试自己的模型
python3 test.py --data data/coco_1cls.data --weights weights/ultralytics49.pt
### 检测并且输出结果：
python3 detect.py --weights weights/last.pt --cfg cfg/yolov3-spp-1cls.cfg --data data/coco_1cls.data
## 3.数据集中图片的规格
maxHeight=1040    maxWeight=2008
## 4.lable的归一化处理
https://github.com/ultralytics/yolov3/issues/341
https://github.com/ultralytics/yolov3/issues/524
## 5.使用screen管理后台进程（&创建的后台进程会随着xmanager结束而退出）
(1)screen -S yourname -> 新建一个叫yourname的session

(2)screen -ls         -> 列出当前所有的session

(3)screen -r yourname -> 回到yourname这个session

(4)ctrl+a,d           ->detach当前session

(5)screen -X -S [session # you want to kill] quit

(6)screen -d yourname -> 远程detach某个session

(7)screen -d -r yourname -> 结束当前session并回到yourname这个session
## 6.当网络很差时，安装pytorch可能会超时，解决办法
pip3 --default-timeout=1000 *



