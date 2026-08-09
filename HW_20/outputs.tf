output "ec2_public_ip" {
  value       = module.nginx_app.public_ip
  description = "Public IP of the created Nginx EC2"
}

output "nginx_url" {
  value       = "http://${module.nginx_app.public_ip}"
  description = "URL to check Nginx status"
}
