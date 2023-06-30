DATASET_TO_IMAGE_SIZES = {
    'yuntian-deng/im2latex-100k': (64, 320),
    'yuntian-deng/im2html-100k': (64, 64),
    'yuntian-deng/im2ly-35k-syn': (192, 448),
    'yuntian-deng/im2smiles-20k': (128, 128),
}

DATASET_TO_INPUT_FIELDS = {
    'yuntian-deng/im2latex-100k': 'formula',
    'yuntian-deng/im2html-100k': 'html',
    'yuntian-deng/im2ly-35k-syn': 'source',
    'yuntian-deng/im2smiles-20k': 'smiles',
}

DATASET_TO_ENCODER_MODEL_TYPES = {
    'yuntian-deng/im2latex-100k': 'EleutherAI/gpt-neo-125M',
    'yuntian-deng/im2html-100k': 'EleutherAI/gpt-neo-125M',
    'yuntian-deng/im2ly-35k-syn': 'EleutherAI/gpt-neo-125M',
    'yuntian-deng/im2smiles-20k': 'DeepChem/ChemBERTa-77M-MLM',
}

DATASET_TO_COLOR_MODES = {
    'yuntian-deng/im2latex-100k': 'grayscale',
    'yuntian-deng/im2html-100k': 'grayscale',
    'yuntian-deng/im2ly-35k-syn': 'grayscale',
    'yuntian-deng/im2smiles-20k': 'rgb',
}

def get_image_size(dataset_name):
    if dataset_name not in DATASET_TO_IMAGE_SIZES:
        print(
            'Please specify image size for customized datasets through image_height and image_width!'
        )
        raise NotImplementedError
    return DATASET_TO_IMAGE_SIZES[dataset_name]

def get_input_field(dataset_name):
    if dataset_name not in DATASET_TO_INPUT_FIELDS:
        print('Please specify image size for customized datasets through input_field!')
        raise NotImplementedError
    return DATASET_TO_INPUT_FIELDS[dataset_name]

def get_encoder_model_type(dataset_name):
    if dataset_name not in DATASET_TO_ENCODER_MODEL_TYPES:
        print(
            'Please specify encoder model type for customized datasets through encoder_model_type!'
        )
        raise NotImplementedError
    return DATASET_TO_ENCODER_MODEL_TYPES[dataset_name]

def get_color_mode(dataset_name):
    if dataset_name not in DATASET_TO_COLOR_MODES:
        print('Please specify color mode for customized datasets through color_mode!')
        raise NotImplementedError
    return DATASET_TO_COLOR_MODES[dataset_name]

