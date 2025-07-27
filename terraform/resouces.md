https://www.youtube.com/watch?v=YcJ9IeukJL8

IAC-Infrastructure as code

In traditional IT and challenges

Buiseness-Buiseness analyste-solution arch-teams like n/w-

this process will take 

Challenges or issue-

1.slow deployment 
2.Expensive
3.Limited Automation
4.Human error
5.wasted Resource
6.Inconsistance

Infrastructure As code-IAC

IAC write and execture code to create provision or destroy the resoucres.
database,network,storage
Types of IAC-

1.Configuration Management-Ansible,puppet,saltstack,shef
- They are idempotent-you can run code multiple times but only make changes that are required to make env in desied state
- Designed to install and manage software
- version control
- maintain standard structure


2.Server Templating-docker,hashicorp packer,hashicorp vagrant
- vm image,docker image(ami in aws)
- immutable 
- we need to update image and update
- immutable infrastructure-once its deployed it is designed to remain unchanged.we need to update image and redeploy instance.

3.Provisioning Tools-terraform,clodformation
- provision Infrastructure,vm,db,vpc,subnets,sg,
- cloudformation used only on aws where as terraform is vendor agnostic
- Deploy immutable infrastructure resources

Terraform-
- terraform uses HCL(hashicorp Configuration Language)
- free and open source
- Infrastructure provision Tools-
- free and opensource developed by hashicorp
- used to provision infrastructure across multiple platform aws,gcp,azure,vmware

Provider-

Providers helps tf to manage platform through api.enaled tf aws,gcp

Terraform uses HCL-Hashicorp Configuration Language-
main.tf -.tf configuration files-

code is declaratativate-meaning the code is defined is the state we want our infrastructure to be in.current state.

tf takes care of current and desired state-

There are three 
1.init-initialise project and identifies providers
2.plan-draft plans to reach target
3.apply-makes changes to reach desired state.fixing mixing


Resouce-db,compute instance execture
lifecycle of resoucres

terraform.tfstate
is blueprint


Installing terraform-

www.terraform.id



HCL Basics-
blocks-infrastructure and set if resources
1.<block> <parameter>{
    key1= value1
    key2 = value2
}

resource "local_file" "pet" {
    filename = "/root/pets.txt"
    content = "happy learning"
}

resource -is block-name
local_file-resoucres Type,local provider file resource,local is provider
pet-resource name can be anything logical name
{}-define argument,specific to type of resource we are creating


Simple terrafrom execution flow consist of four steps-
1.init-
2.plan-
3.apply-


Example
1.terraform init-
downloads plugin
Initializes Backend – Configures where Terraform stores its state (e.g., local or remote like S3).

Installs Providers – Downloads the necessary provider plugins (like AWS, Azure, Google Cloud, etc.).

Prepares the Working Directory – Validates configuration files and sets up dependencies.

2.terraform plan-it will not create anything it will create 
shows actions which is performed-



3.terraform apply -applies files


1️⃣ terraform plan -out=tfplan

Creates an execution plan and saves it to a file (tfplan).
This ensures that the exact plan is applied later, preventing unintended changes.

terraform plan -out=tfplan
This generates a binary file (tfplan), which stores the Terraform execution plan.

2️⃣ terraform apply tfplan

Applies the saved plan (tfplan) instead of generating a new one.
Ensures that the changes being applied match what was previously reviewed.


 
📌 Why Use This Approach?
✅ Prevents unexpected changes (since the plan does not change between plan and apply).
✅ Ensures approval before execution, making it useful for review processes in teams.
✅ Essential for CI/CD pipelines, where you generate a plan, get approval, and then apply it later.


n Terraform, you can assign values to variables in several ways. Here's a breakdown of the most common methods:

✅ 1. In a terraform.tfvars file
Create a file named terraform.tfvars:

hcl
Copy
Edit
region = "us-west-2"
instance_type = "t3.micro"
Terraform will automatically load this file when you run terraform plan or terraform apply.

✅ 2. Directly in the CLI using -var
bash
Copy
Edit
terraform apply -var="region=us-west-2" -var="instance_type=t3.micro"
✅ 3. In environment variables
Use TF_VAR_ prefix:

bash
Copy
Edit
export TF_VAR_region="us-west-2"
export TF_VAR_instance_type="t3.micro"
✅ 4. In a variable definition file (.tf or .tfvars)
You can create your own file like prod.tfvars:

h
Copy
Edit
# prod.tfvars
region = "us-east-1"
Then use it with:

bash
Copy
Edit
terraform apply -var-file="prod.tfvars"
✅ 5. Default value in the variable block
Inside your .tf file:

h
Copy
Edit
variable "region" {
  type    = string
  default = "us-east-1"
}
If no other value is provided, Terraform uses the default.


variable defination precedence

order option
1  env variable
2 terraform.tfvars
3.auto.tfvars
4. -var or -var-file command line flag


important command-
1.terraform init
2.terraform plan
3.terraform apply
4.terraform validate-check validate format and if it correct
5.terraform fmt-format
6.terraform show  -json
7.terraform output
8.terraform refresh
9.terraform graph


Mutable vs Imutable

updating 


lifecycle rules
if we donot want decide the lifecycle of events create before destory etc


lifecycle={
  ignore_changes=[
    tags
  ]
  create_before_destroy = true
}

data sources use data from files not provide by terraform 
 


meta argument
depends on 
lifecycle

