output "s3_bucket_name" {
  value = aws_s3_bucket.frontend.id
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.visitor_count.name
}

output "api_url" {
  description = "Base URL for API Gateway"
  value       = aws_apigatewayv2_stage.default.invoke_url
}
