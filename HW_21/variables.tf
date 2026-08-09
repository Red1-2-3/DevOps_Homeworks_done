variable "region" {
  type        = string
  default     = "us-east-1"
  description = "AWS Region"
}

variable "vpc_id" {
  type        = string
  default     = "my default vpc"
  description = "Target VPC ID in us-east-1"
}

variable "key_name" {
  type        = string
  default     = "My ip"
  description = "SSH key pair name in AWS"
}
