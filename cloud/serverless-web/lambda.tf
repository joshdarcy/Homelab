data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "hello.py"
  output_path = "lambda_function_payload.zip"
}

resource "aws_lambda_function" "hello_world" {
  filename      = "lambda_function_payload.zip"
  function_name = "${var.project_name}-function"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "hello.lambda_handler"
  runtime       = "python3.11"

  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.visitor_count.name
    }
  }
}
