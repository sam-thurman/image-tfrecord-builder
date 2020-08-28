app = dict(
    IMAGES_INPUT_FOLDER = '/Users/sam/flatiron/projects/capstone/asl_alphabet_image_classification/data/asl_alphabet_train',
    OUTPUT_FILENAME = '/Users/sam/flatiron/projects/capstone/asl_alphabet_image_classification/data/tfrecord_train',
    NUMBER_OF_SHARDS = 87, # (29 classes * 3000 imgs each)/1000 records recommended per shard (I think?)
    TRAINING_EXAMPLES_SPLIT = 0.8,
    SEED = 123
)