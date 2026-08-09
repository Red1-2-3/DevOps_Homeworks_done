variable "vpc_id" {
  type        = string
  description = "ID для створеної VPC"
}

variable "list_of_open_ports" {
  type        = list(number)
  description = "Список портів які відкриті для входу"
  default     = [80, 22]
}
