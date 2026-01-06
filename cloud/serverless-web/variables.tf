variable "aws_region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "ap-southeast-2"
}

variable "project_name" {
  description = "Name of the project for naming resources"
  type        = string
  default     = "homelab-cloud"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}
