import os
from django.core.exceptions import ValidationError

MAX_FILE_SIZE = 6000000
IMAGE_ALLOWED_EXTENSIONS = ['.jpg', '.png', '.gif']
FILE_ALLOWED_EXTENSIONS = ['.pptx', '.rtf', '.pdf', '.docx']


def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f'max file size is: {MAX_FILE_SIZE}')


def validate_image_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in IMAGE_ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {IMAGE_ALLOWED_EXTENSIONS}')


def validate_file_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in FILE_ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {FILE_ALLOWED_EXTENSIONS}')
