resource "aws_s3_bucket" "amazon-polly-bucket" {
  bucket = var.S3_BUCKET_NAME
}

resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.amazon-polly-bucket.id
  key = "./audio_files"
  source = "/dev/null"
}