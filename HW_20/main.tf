terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket = "terraform-state-danit-devops-sysadmin"
    key    = "sysadmin/terraform.tfstate"
    region = "eu-central-1"
  }
}

provider "aws" {
  region = "eu-central-1"
}

module "nginx_app" {
  source             = "./modules/ec2_nginx"
  vpc_id             = var.vpc_id
  list_of_open_ports = var.list_of_open_ports
}
