output "ec2_public_ips" {
  value       = aws_instance.web_servers[*].public_ip
  description = "Public IP addresses of created EC2 instances"
}
