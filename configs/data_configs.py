from configs import transforms_config
from configs.paths_config import dataset_paths


DATASETS = {
	'seg_to_chip': {
		'transforms': transforms_config.SegToImageTransforms,
		'train_source_root': dataset_paths['seg_chip'],
		'train_target_root': dataset_paths['seg_chip'],
		'test_source_root': dataset_paths['seg_chip_t'],
		'test_target_root': dataset_paths['seg_chip_t'],
	}
}
