# Car Dealerships App


## 📝  Background

This application represents the penultimate milestone in the Full-Stack Software Developer certification program offered by IBM. Built on a core framework provided by the IBM team, which initially lacked functionality and predefined templates, this project was transformed into a comprehensive platform. The skills learned and practiced in 10 courses by the IBM team are presented in this project, which consists of several programming languages and a backend frameworks. The application serves as a platform for dealership users offering them to engage with dealership-related details and reviews. Its backbone relies heavily on a RestAPI for seamless communication and integration, ensuring efficient data management and retrieval. This project stands as a testament to the knowledge, expertise, and dedication fostered within the IBM certification program, exemplifying the practical application of acquired skills in real-world scenarios.


## 📖  Description 

The application functions as a platform for reviewing Best Cars dealerships, allowing logged-in users to submit reviews for specific dealership products. It utilizes a combination of backend frameworks including Flask and NodeJS to interact with the database, with Django serving as the main application. Communication and data transfer between these frameworks are facilitated through RestAPI. Flask and Node servers retrieve data from the IBM Cloudant database and transmit it to the Django server, which in turn utilizes the data for templates. On the frontend side, HTML, JavaScript, and Bootstrap are employed to create a user-friendly interface.


## 💻  Technologies

- 🚀 Node.js
- 🐍 Flask
- ⚙️ Django
- ☁️ IBM Cloudant
- 🌐 HTML
- 🚀 JavaScript
- 🅱️ Bootstrap


## 🔧  Installation and Setup

1. **Set Up Django Server:**
    - Open a terminal window.
    - Navigate to the server directory of the project:
      
        ```
        cd full-stack-car-dealerships-app/server
        ```
    - Run the following commands to set up the Django server:
      
        ```
        python3 manage.py makemigrations
        python3 manage.py migrate
        python3 manage.py runserver
        ```

2. **Set Up Node.js Server**
    - Open a new terminal window.
    - Navigate to the nodejs directory:
      
        ```
        cd full-stack-car-dealerships-app/functions/sample/nodejs
        ```
    - Install the Express.js framework:
      
        ```
        npm install express
        ```
    - Run the Node.js server to fetch dealership data:
      
        ```
        node get-dealership.js
        ```
        
3. **Set Up Flask Server**
    - Open a new terminal window.
    - Navigate to the python directory:
      
        ```
        cd full-stack-car-dealerships-app/functions/sample/python
        ```
    - Run the Flask server to simulate reviews:
      
        ```
        python reviews.py
        ```

4. **Access the Application:**
    - Open a web browser.
    - Access the application at: [http://localhost:8000](http://localhost:8000)
    - This will load the full-stack car dealerships app in your browser.


## 👤 Author
- Stipan Madzar


## 📧  Contact
- ✉️ Email: [smadzar90@student.se.edu](mailto:smadzar90@student.se.edu)
- 🐙 GitHub: [smadzar90](https://github.com/smadzar90)
- 💼 LinkedIn: [Stipan Madzar](https://www.linkedin.com/in/stipan-madzar-b6b857225/)





  




