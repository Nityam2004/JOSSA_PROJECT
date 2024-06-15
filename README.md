JoSAA Registration System
The JoSAA Registration System is a web application built using Django, designed to provide various functionalities related to college admissions and counseling processes.

Features
User Authentication: Allows users to register, log in, and log out securely.
Home Page: Provides access to different features such as Marks vs Rank, College Predictor, FAQs, About, Contact, and more.
Marks vs Rank: Predicts ranks based on input marks and category.
College Predictor: Predicts colleges based on user preferences.
News and Notices: Displays important notices and news items.
Help: Important links and helpline
Faqs: Some frequently asked questions
Responsive Design: Ensures compatibility across various devices.
Installation
Follow these steps to set up the project locally:

Clone the Repository:

bash
Copy code
git clone <git@github.com:Nityam2004/JOSSA_PROJECT.git>
cd JoSAA-Registration-System
Install Dependencies:

Copy code
pip install -r requirements.txt
Database Setup:

Ensure your database settings are correctly configured in settings.py.
Apply migrations:
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

Copy code
Go in this folder and then run -- JOSSA_PROJECT\FRONTEND\login_page\registeration_system\registeration
python manage.py runserver
Access the Application:
Open your web browser and go to http://127.0.0.1:8000/ to view the application.

Usage
User Registration: Navigate to the registration page (/signup) to create a new user account.
User Login: Access the login page (/login) to authenticate and log into the system.
Navigation: Use the navigation links in the header to explore different features such as Marks vs Rank, College Predictor, and more.
News and Notices: Important notices are displayed on the homepage. Click on each notice button to view more details.
Contributing
Contributions are welcome! Here's how you can contribute to the project:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.
Credits
Created by [NITYAM , YASH PAWAR , ROHIT NIGAM , RAMJAS SAHU]
License
This project is licensed under the MIT License.

Notes:
