<img width="1230" height="151" alt="Screenshot 2026-11-02 150020" src="https://github.com/user-attachments/assets/0c1d4898-fe58-4e98-82e8-144810612df5" />


# *VisitPulse Pro - Dockerised Web Application*
## *Project Overview*

*What is VisitPulse Pro?*

Visitpulse pro is a web application I created which trakcs the number of times the webpage has been visited and shows the location in which people are visiting from and stores the value of how many people have visited from each country. 

*What was the aim?*

The aim of this project was to create a simple web application, and containerise it using docker, and scale it to deal with large requests. The project gave an understanding of how different servers communicate with eachother using docker containers, and how YAML files can be used to run multiple containers at once within a custom network. 

*How does it work?*

I started of with creating a flask web application, where I then progressed into creating a redis database to store the visit counts of the webpage, which required a nginx server to act as a reverse proxy to handle large workflows with the use of one port, before adding a GeopIP database from dockerhub to retrieve the IP address of visitors to find the location, and send the information to flask. I then created a .compose YAML file to enable the containers to run together and communicate on a local network. 

## Creating the Project:

*Flask Web Application*

- I began creating a basic python web application
- The code already imported flask and was configured to return a basic welcome message
- We then configured the code to create VisitPlulse Pro and to add a HTML and CSS to customise the webpage
- We began to add more routes to integrate additional servers:
   - */* - The original Welcome page
   - */count* - The count page which displayed the number of times a visitor visited the page
   - */about* - An about page to provide further detail about me and the website
   - */GeoIP* - This displayes the country of the visitors

*Redis Database:*

- This was integrated to store the data for the flask website
- Redis uses port 6379 which was configured in the app.py code
- We gave redis an environment variable (Redis_host, Redis_port)
- Redis was the database which stored the totoal visit count and number of visits from each country
<img width="482" height="97" alt="Screenshot 2026-11-02 144344" src="https://github.com/user-attachments/assets/b976ad12-6c53-4602-a815-b4330147ffba" />


*Nginx Reverse Proxy:*

- The application was configured to port 5000 on our host machine and container port
- To scale the application we created 3 containers using the command;
   - *docker-compose up --scale web=3*
-  This provided 3 containers, which have a internal docker port of 5000 however they could not listen to port 5000 on our local host
-  We required a reverse proxy to direct traffic flow to the 3 containers and to ease the load on one container. This is known as load balancing
-  Thus, we used nginx
-  This is useful for when the website is deadling with large requests, and it allows the applications to run smoothly.

<img width="620" height="332" alt="Screenshot 2026-11-02 144504" src="https://github.com/user-attachments/assets/c72cb7b9-4753-4359-b242-1a4065dbc5e8" />



*GeopIP for location data:*

- GeopIP is a server which finds the location of IP addresses
- I pulled the GeopIP image from docker hub using :
     - *docker pull gsmlg/geoip2:embed*
- This is an image already configured
- I then run the image on my local host using:
     - *docker run -d --name geopip -p 8000:8000 gsmlg/geopip2 -addr :8000*
- This give us a name for the container, maps the container to our laptop port and tells geopIP to listen to port 8000
- This runs our image to test it
- I then integrate GeopIP into our flask application by changing app.py
- GeopIP now sends the location of users IP addresses to flask, which displays it on the website

<img width="278" height="111" alt="image" src="https://github.com/user-attachments/assets/e1eba917-d960-4bfe-9a62-ee7a1a9de116" />


## *Creating the Dockerfiles:*

- The dockerfile is the blueprint for the image
- It stores the information required to build the image we want
- I created a dockerfile for the flask application
  
  <img width="306" height="120" alt="Screenshot 2026-11-01 154638" src="https://github.com/user-attachments/assets/0ce3662a-580c-4909-99c5-844d3a188e7b" />

*What does each command do?*
   - *FROM*: Forms the Base of the image
   - *WORKDIR*: Defines the working directory inside of our docker container
   - *COPY*: The first argument tells us which folder to copy files from and the second tells us which folder to paste them to inside docker (defined in WORKDIR)
   - *RUN*: The instruction we want our dockerfile to execute
   - *EXPOSE*: The port our application uses inside the container
   - *CMD*: The command for running our application

Building the image:

- Once we have confiured our dockerfile, we can build it
- This creates the actual image with all the information we have passed into it:
     - *Docker build -t flask-application .*
       
*What does this do?*
- *docker build* tells docker to create the image
- *-t flask-application* tags our flask applcation with a name (flask-application)
- *.* tells docker to build our image in this directory


 *Creating our dockerfile for redis:*

- We created a dockerfile for our redis file
- This allowed us to build a image for our redis file
- We then used these two images (redis and flask) in our *YAML* file

  <img width="357" height="102" alt="Screenshot 2026-11-01 171010" src="https://github.com/user-attachments/assets/a58917ec-f9ff-47dd-abae-892aba1ae1d0" />
  
  *Note for next time:*

- I created a new dockerfile for the redis image however, this was not necessary. There already exists a redis image on docker hub hence I only used two commands on the dockerfile to configure the image. I could have included the pre-built image on the *YAML* file instead of creating a new one.  
- I did this for the GeopIP. I learnt to use pre-existing images and I found it on dockerhub before adding it directly to my *YAML* file, isntead of creating a new dockerfile. 
<img width="1901" height="447" alt="Screenshot 2026-11-02 143436" src="https://github.com/user-attachments/assets/b15d4888-4a8d-4562-bebd-3e6a68117e60" />

## *Docker Compose YAML file:*

- I created a *YAML* file to run the 4 containers all together
- I configured the file for all 4 services
<img width="445" height="683" alt="Screenshot 2026-11-01 144502" src="https://github.com/user-attachments/assets/c32c3999-1c1c-45d5-9c1b-ebea29ac0d60" />

*Why use the YAML file?*

- Using a *yml* files means all 4 services run simultaneously
- This means with one command we get:
     - A flask web container 
     - An Nginx container (The reverse proxy for load balancing
     - A redis container (This stores the data to count the number of visits)
     - A GeopIP container (finds the location of the visitors using their IP address)
     - A custom network is created for all the containers to communicate with each other
- The command I run to start the defined *yml* file is:
     - *Docker-compose up*
   <img width="1397" height="770" alt="Screenshot 2026-11-01 214621" src="https://github.com/user-attachments/assets/4dac5628-ae57-4c5d-87d1-83a73700170c" />
   
- This starts the application with the 4 containers communicating with each other
- We can view the containers with the command :
     *docker ps*

  <img width="1410" height="177" alt="Screenshot 2026-11-01 225414" src="https://github.com/user-attachments/assets/85aa2e4a-4eac-4853-915f-9f00db44ef58" />
 

  
  ## *How do we scale the application to deal with large traffic?*
  
- We now run the command to scale our application to have 3 flask containers, managed by the reverse proxy:
     - *Docker-compose up --scale web=3*

  <img width="1399" height="902" alt="Screenshot 2026-11-02 133423" src="https://github.com/user-attachments/assets/f34093d9-f85c-4aec-89dc-3cb363b7389f" />

      
- This now creates a total of 6 containers across 4 services, with nginx now managing the load between 3 flask containers by distributing the load effectively
- We can see the amount of the containers being updated to 6 currently running
- The command to close the containers is:
     - *docker-compose down*
  <img width="1401" height="198" alt="Screenshot 2026-11-02 135825" src="https://github.com/user-attachments/assets/1214bb18-2b89-49a5-9f26-97774a5710be" />

## *Persistent Storage*

- Each time we start the containers, we want our visit count to remain the same and remembered by redis.
- To do this, we must create a volume in our *YAML* file
 <img width="388" height="447" alt="Screenshot 2026-11-02 174733" src="https://github.com/user-attachments/assets/e1532976-d42d-4601-a4ed-861d1e18e6fe" />
- redis-data is the container where the redis data is stored
- /data is the folder within the redis container which stores the visits
- Volume is then used to as a seperate storage box which stores all the redis data
- This means even if the redis container is stopped or removed, volume keeps the data, ready to reconnect to the redis container
- The volume at the bottom tells docker compose to create a volume for redis-data 





  ## *Customising our Application*
  - We can add some features to our web application
  - We used *CSS* and *HTML* to improve the quality of our website
  - We improved the layout
  - Added color schemes
  - Incuded links to my linkedIn page
  
<img width="1917" height="901" alt="image" src="https://github.com/user-attachments/assets/35485f0a-7ea1-49c0-8760-4d2913c64b3d" />

*Welcome page (/)*




<img width="1900" height="903" alt="image" src="https://github.com/user-attachments/assets/336a811c-b6ab-47f1-a56e-9848f63acfa8" />

*About me page (/about)*




<img width="1897" height="907" alt="image" src="https://github.com/user-attachments/assets/36b2b6df-eddb-4979-a1ae-73ba0da1aad3" />

*Count page displaying number of visits and location (/count)*




