from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class CustomMediaStorage(S3BotoStorage):
	bucket_name = settings.AWS_STORAGE_BUCKET_NAME_MEDIA


class CustomStaticStorage(S3BotoStorage):
	bucket_name = settings.AWS_STORAGE_BUCKET_NAME