resource "aws_dynamodb_table" "visitor_count" {
  name           = "${var.project_name}-visitor-table"
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "PK"

  attribute {
    name = "PK"
    type = "S"
  }

  tags = {
    Environment = var.environment
  }
}
