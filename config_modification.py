import os
import io
import codecs
from bs4 import BeautifulSoup as bs
path_home=os.path.split(os.path.realpath(__file__))[0]
xmlstr='<config><config/>'
soup=bs(xmlstr,'xml')

soup.config['ssd_mobilenet_config_path']=os.path.join(path_home,'ssd_mobilenet_v1_small_object.config')
soup.config['train_folder']=os.path.join(path_home,'train')
soup.config['image_path']=os.path.join(path_home,'object_dataset\\images')
soup.config['image_annotation_path']=os.path.join(path_home,'object_dataset\\annotations')
soup.config['container_train']=os.path.join(path_home,'object_dataset\\train.txt')
soup.config['container_test']=os.path.join(path_home,'object_dataset\\test.txt')
soup.config['tfrecord_train']=os.path.join(path_home,'object_dataset\\train.record')
soup.config['tfrecord_test']=os.path.join(path_home,'object_dataset\\test.record')
soup.config['objects_label_map_path']=os.path.join(path_home,'object_dataset\\object_label_map.pbtxt')
soup.config['ssd_model_path']=os.path.join(path_home,'ssd_mobilenet_v1_coco_2017_11_17')

with codecs.open(os.path.join(path_home,'config.xml'),'w',encoding='utf8') as f:
    f.write(str(soup))



