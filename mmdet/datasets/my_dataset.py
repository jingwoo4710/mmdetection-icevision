from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class MyDataset(CocoDataset):

    CLASSES = ('car', 'pedestrian', 'trafficLight-Red', 'trafficLight-Green', 'truck',
                'trafficLight', 'biker', 'trafficLight-RedLeft', 'trafficLight-GreenLeft'
                , 'trafficLight-Yellow', 'trafficLight-YellowLeft')
