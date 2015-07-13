from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class CustomMediaStorage(S3BotoStorage):
	bucket_name = settings.MEDIA_AWS_STORAGE_BUCKET_NAME


class CustomStaticStorage(S3BotoStorage):
	bucket_name = settings.STATIC_AWS_STORAGE_BUCKET_NAME