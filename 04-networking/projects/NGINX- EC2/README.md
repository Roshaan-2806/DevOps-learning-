# Networking Assignment - Creating a **NGINX EC2** Instance
## Project overview

In this project, I created a **NGINX** web server on a hosted **AWS** **EC2** Instance, running on **Ubuntu**. The aim is to make a custom domain, which I connect to the **EC2** instance using **Cloudfare DNS** which enables access to the **NGINX** page thorugh our domain. 

## Step 1 - Purchasing our Domain

- Go to Cloudfare 
- Create a Domain using a name your happy with 
- Purchase it
<img width="1912" height="899" alt="Screenshot 2026-10-16 153010" src="https://github.com/user-attachments/assets/3f2265bc-ca31-49fd-ac72-216f0cf43b92" />


## Step 2 - Creating an AWS EC2 Instance

- Create an AWS account 
- Navigate to EC2 and launch a new Instance 
- Give it a name 
- Select a Ubuntu Server as the **AMI**

<img width="1221" height="748" alt="Screenshot 2026-10-19 170038" src="https://github.com/user-attachments/assets/6156b93b-cd5d-4b69-921c-ef7ad8332a31" />


- Select **t3.micro** as the Instance type

<img width="1228" height="282" alt="Screenshot 2026-10-19 170110" src="https://github.com/user-attachments/assets/fb6905a0-bebc-48a9-a02c-7b11402050dd" />


- Create a new key pair ( make sure its RSA type and .pem private key )
<img width="726" height="703" alt="Screenshot 2026-10-19 170717" src="https://github.com/user-attachments/assets/720614d3-8448-417f-ad35-11ce13912be0" />

- Launch the Instance

## Step 3 - Connecting to the EC2 Instance 

- Select the Instance and ensure its running
- Select **Connect** 
- On your terminal, run chmod 400 on your .pem file to secure its permissions
- Then copy in your SSH command from AWS 
- ssh -i "your-key-name.pem" ubuntu@your-ec2-public-dns

  <img width="1411" height="692" alt="Screenshot 2026-10-19 171146" src="https://github.com/user-attachments/assets/c422f33b-cfc0-48da-8ef5-bc2e386fcf3e" />


## Step 4 - Installing NGINX

- You need to install nginx on your EC2 
- sudo apt update (to refresh updates and packages) 
- sudo apt install nginx (to install NGINX on your ubuntu server)

  <img width="1486" height="600" alt="Screenshot 2026-10-19 165107" src="https://github.com/user-attachments/assets/fdfc70dc-20d5-4c6f-b8ea-b5c970dff385" />


   Why sudo?
- Gives you administrative powers

## Step 5 - Configuring the security group 

- Go to the AWS EC2 instance 
- Navigate to security and select **Launch-Wizward-1**
- Edit the inbound rules of the existing security group
- Add HTTP (port 80) to it 
- Select Anywhere IPv4 (0.0.0.0/0) as the source
<img width="1917" height="727" alt="Screenshot 2026-10-16 172301" src="https://github.com/user-attachments/assets/90ef3866-6b49-4d12-ae24-87c56c835e9d" />

  Why?
- This allows anyone on the internet to acess the NGINX website 
- Save rules
<img width="1538" height="285" alt="Screenshot 2026-10-19 165417" src="https://github.com/user-attachments/assets/181ef56b-7e30-4e32-ba0d-250efea3e380" />

  

## Step 6 - Configuring Cloudfare DNS 

- Nasvigate to Cloudfare where your DNS was created
- Add a record
- Select A as the type (points our Domain name to Public IPV4 adress)
- Enter your domain name and your public IPV4 adress from your EC2 instance 
- Turn proxy status off
- Save

<img width="950" height="547" alt="Screenshot 2026-10-16 161539" src="https://github.com/user-attachments/assets/2ce82473-40f8-4476-bfe1-24a33d9b69e2" />


## Step 7 - Testing the website 
- Enter your domain into your web browser
- You will be greeted with the default Welcome to nginx! page

<img width="1917" height="906" alt="Screenshot 2026-10-19 163834" src="https://github.com/user-attachments/assets/331e64a5-0e8b-4711-97d9-c10cd4f36b33" />
