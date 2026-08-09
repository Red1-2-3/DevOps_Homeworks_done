variable "vpc_id" {
  type        = string
  description = "VPC ID"
  default     = "vpc-0e01eaa754d3307b6"
}

variable "list_of_open_ports" {
  type        = list(number)
  description = "Ports to open"
  default     = [80, 22]
}
