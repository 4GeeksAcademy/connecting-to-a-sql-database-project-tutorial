# Connecting to an SQL database using Python

## Part 1: Create a database using PostgreSQL

Make sure you have installed the Postgres client for the terminal called `PSQL`. You can check if you have it by running the following command:

```bash
$ psql --version
```

> NOTE: If you get an error, try [following these instructions](https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows/) to install `psql` on your computer.

Now, review the contents of the `./.env` file and follow the steps described below:

1. Create a new database within the Postgres engine by customizing and executing the following command: `$ createdb -h localhost -U <username> <db_name>`
2. Connect to the Postgres engine to use your database, manipulate tables and data: `$ psql -h localhost -U <username> <db_name>`

> NOTE: Remember to check the `./.env` file information to get the `username` and `db_name`.

Once you are inside `PSQL` you will be able to create tables, make queries, insert, update, or delete data and much more!

## Part 2: Understand the structure of your project's template

Once you have completed the above steps, you will have created your SQL database, but there are no tables yet. Next, you need to connect to your empty database, and you will create some tables using Python via SQL scripts that you will find in the `./src/sql/` folder:

- `./src/sql/create.sql` with all the tables you need to create. Hands on the creation of those tables.
- `./src/sql/insert.sql` with all the table values that will be inserted into each table.
- `./src/sql/drop.sql` contains the SQL code to drop the tables, very useful to clean up your database.

Other important things to mention about the structure:

- Professional projects usually have a `./src` folder that contains all the **coding files** (the files that the developer will implement).
- `./assets` is irrelevant to you; it contains all the images we needed for this tutorial.
- The root of any professional project usually contains all the configuration files such as `.gitignore`, `requirements.txt`, etc. You will learn more about these files during the rest of the project.

## Part 3: Install dependencies

There is a file in this project called `./requirements.txt` that contains the list of Python libraries that we will use in this project, such as Pandas, psycopg2, SQLAlchemy, etc. Run the `pip install -r requirements.txt` command to install all the libraries at once using the PIP (*Package Installer of Python*) wizard.

> NOTE: Make sure that the command does not generate any errors in the terminal.

## Part 4: Include your database credentials

Create your `./.env` file. It is good practice for every Python application to have a `.env` file. The file name starts with a `.` dot because it is a configuration file that will be ignored by your Git repository. It should be ignored because we will add our database password inside that file.

Write your database credentials inside the `.env` file. It should look something like this (the values included serve as examples):

```text
DB_USER = 'hkietatgd83b4x0l'
DB_PASSWORD = 'p0s2wasdado1cr02d12'
DB_PORT = 3306
DB_HOST = 'f565gmi022AD.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
DB_NAME = 'y9uflxvx2hsf11g3f'
```

> NOTE: Be sure to replace these values with your actual database credentials.

## Part 5: Start programming

All your Python code should always be inside the `src` folder; this is also another good practice.

1. The `connect` function contains the code needed to connect to your Python database. If you look closely, you will see how it loads all the environment variables into a variable called `connection_string` and then calls the `create_engine` and `connect` functions.

```py
def connect():
    global engine # This allows us to use a global variable called "engine"
    # A "connection string" is basically a string containing all database credentials together.
    connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine
```

## 📝 Instructions

1. Let's create a file inside the `src` folder named `./src/app.py`.

> NOTE: This file will contain most of your application code, as well as the database connection and database queries.

2. Create a PostgreSQL database as described in part 1.

3. In your `app.py`, program the connection to your database.

> NOTE: You can try to reuse the `connect` Python function provided above.

4. Create the tables indicated in `./src/sql/create.sql`.

5. Insert the data specified in `./src/sql/insert.sql` into the tables created in the previous point.

6. Use Pandas to print one of the tables as a DataFrame using the `read_sql` function of this library.

## Additional tips

- Log into your database using `psql -h localhost -u postgres`
- Connect to a remote database using: `psql -h <REMOTE_HOST> -p <REMOTE_PORT> -U <DB_USER> <DB_NAME>`
- Deletes a database: `$ dropdb -h localhost -U <username> <db_name>`
- Create a DB in the render.com cloud and connect [following these commands](https://render.com/docs/databases#connecting-from-outside-render).

