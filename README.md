# Preparation
1. download everything from the current project to path_1<br>
Note that all the prerequisites are from tensorflow official [models](https://github.com/tensorflow/models)<br>
object_detection<-official_model/research/object_detection<br>
utils&models<-official_model/research/object_detection/utils&models<br>
datasets&deployment&nets<-official_model/research/slim/datasets&deployment&nets<br>
model<-official_model/research/cvt_text/model<br>
download link for [ssd_model](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz)<br>
2. install necessary py packages<br>
# Fix data (from current project)
1. object_Dataset/images contains source images<br>
2. object_Dataset/annotations contains annotations information for source images<br>
3. if you would like to annotate images by yourself, use the [label_tool](https://github.com/tzutalin/labelImg)<br>
4. object_Dataset/train.txt contains image names for training<br>
5. object_Dataset/test.txt contains image names for testing<br>
6. object_Dataset/object_label_map.pbtxt contains label information<br>
7. set correct paths in the config_modification.py and generate the config.xml<br>
7. set correct paths of "fine_tune_checkpoint","train_input_reader","eval_input_reader"  in /ssd_mobilenet_v1_small_object.config<br>
# Train
1. run /totfrecord.py twice (path configuration needs to be motified) to generate tfrecords for training and testing respectively, check config.xml if error occurs<br>
2. run /train.py to train you model, press "control_c" to stop when receiving a stable loss<br>
# Freeze model
1. run /export_inference_graph.py to freeze the *.pb model, output is supposed to be saved at the train folder (latest step by default)<br>
# test
1. set path configuration in /object_detection_my.py and run<br>

