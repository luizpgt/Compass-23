# Define your environment variables
variable "DYNAMODB_TABLE" {}
variable "DYNAMODB_AWS_ACCESS_KEY_ID" {}
variable "DYNAMODB_AWS_SECRET_ACCESS_KEY" {}
variable "DYNAMODB_AWS_REGION" {}
variable "POLLY_AWS_ACCESS_KEY_ID" {}
variable "POLLY_AWS_SECRET_ACCESS_KEY" {}
variable "POLLY_AWS_REGION" {}
variable "S3_BUCKET_NAME" {}
variable "S3_AWS_ACCESS_KEY_ID" {}
variable "S3_AWS_SECRET_ACCESS_KEY" {}
variable "S3_AWS_REGION" {}

# Output the environment variables as a JSON file
locals {
  env_variables_json = {
    DYNAMODB_TABLE                 = var.DYNAMODB_TABLE
    DYNAMODB_AWS_ACCESS_KEY_ID     = var.DYNAMODB_AWS_ACCESS_KEY_ID
    DYNAMODB_AWS_SECRET_ACCESS_KEY = var.DYNAMODB_AWS_SECRET_ACCESS_KEY
    DYNAMODB_AWS_REGION            = var.DYNAMODB_AWS_REGION

    POLLY_AWS_ACCESS_KEY_ID        = var.POLLY_AWS_ACCESS_KEY_ID
    POLLY_AWS_SECRET_ACCESS_KEY    = var.POLLY_AWS_SECRET_ACCESS_KEY
    POLLY_AWS_REGION               = var.POLLY_AWS_REGION

    S3_BUCKET_NAME                 = var.S3_BUCKET_NAME
    S3_AWS_ACCESS_KEY_ID           = var.S3_AWS_ACCESS_KEY_ID
    S3_AWS_SECRET_ACCESS_KEY       = var.S3_AWS_SECRET_ACCESS_KEY
    S3_AWS_REGION                  = var.S3_AWS_REGION
  }
}

# Output the environment variables as a formatted JSON string
output "env_variables_json" {
  value = <<-EOF
    {
      ${join(",\n ", [for k, v in local.env_variables_json : "\"${k}\": \"${v}\""])}
    }
  EOF
}
