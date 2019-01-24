# A Basic Flask App with asnychronous task queuing

The goal of this project is to build an extremely basic site crawler which does nothing but sends a request to an URL and
records the number of words in that page (roughly) and saves it to the database. This task is done asnychronously using a redis queue.

## Step 1:
Ensure you have a PostgreSQL database created. 

---
## Step 2:
Navigate to `app/configs/db_uri.py` and set the variable to detect your database.
`SQLALCHEMY_DATABASE_URI = postgresql://username:password@hostname/database`
`username`: The username used to create the database.
`password`: The password for that user.
`hostname`: The name of the host (locally it should be `localhost`)
`database`: The name of the database.

Also ensure you have `redis` set up on your computer. If not please download it from here: https://redis.io/download

---
## Step 3:
Make sure you are connected to the internet. Then, navigate to the project root and *activate your virtual environment*. Also install all the dependencies using `pip install -r requirements.txt`.

---
## Step 4:

1. On your terminal, type `flask rebuild` and hit enter to load up the models in your database.
WARNING: This function drops all tables and creates them again, so you WILL lose data. Use with caution.
2. Activate the redis worker by typing `flask worker` on the terminal and hitting enter.
3. Finally, run the application by running the application in `development` mode using `python run.py`
4. Go to `localhost:5000/index` and paste a link in the text box.
5. Hit submit and see the results appearing in a while!

## Running Tests

Ensure your virtual environment is activated. Then:
1. Rebuild the database using `flask rebuild`.
2. Type `pytest` in the terminal and hit enter. All the tests should pass.
3. Remember to rebuild your database again to clear all the data the test has generated.