resource "aws_dynamodb_table" "dynamodb_table" {
  name         = var.DYNAMODB_TABLE
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "unique_id"

  attribute {
    name = "unique_id"
    type = "S"
  }
  attribute {
    name = "created_audio"
    type = "S"
  }
  attribute {
    name = "received_phrase"
    type = "S"
  }
  attribute {
    name = "url_to_audio"
    type = "S"
  }

  # Define a global secondary index (GSI) for created_audio
  global_secondary_index {
    name            = "CreatedAudioIndex"
    hash_key        = "created_audio"
    projection_type = "ALL" # or "KEYS_ONLY" or "INCLUDE" as needed
  }

  # Define a global secondary index (GSI) for url_to_audio
  global_secondary_index {
    name            = "UrlToAudioIndex"
    hash_key        = "url_to_audio"
    projection_type = "ALL" # or "KEYS_ONLY" or "INCLUDE" as needed
  }

  global_secondary_index {
    name            = "ReceivedPhraseIndex"
    hash_key        = "received_phrase"
    projection_type = "ALL" # or "KEYS_ONLY" or "INCLUDE" as needed
  }
  tags = local.common_tags
}
