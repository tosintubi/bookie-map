<p align="center">
  <a href="" rel="noopener">
  <img width=200px height=200px src="https://i.imgur.com/GaiJno0.png" alt="Project logo"></a>
</p>


<h3 align="center">BookieMap</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![GitHub issues](https://img.shields.io/github/issues/tosintubi/bookie-map)
![GitHub pull requests](https://img.shields.io/github/issues-pr/tosintubi/bookie-map?color=light%20green)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Tech](#tech)
- [Installation](#installation)
- [Built Using](#built_using)
- [Authors](#authors)
- [Collaboration](#collaboration)
- [License](#license)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Bookie-Map core is the backend of <b>Bookie</b>, a Peer to Peer Book Loan App.


## 💻 Tech <a name = "tech"></a>
BookieMap is written in [Python 3](https://www.python.org/) and [Flask 2.0.1](https://flask.palletsprojects.com/en/2.0.x/).


## ⚙️ Installation  <a name = "installation"></a>


### MacOS/Linux
Please install these packages and set up your environment in the order listed below. Run an upgrade or update if you find that the package is already installed:

- Python 3. Run the 'python3 -V' command to see the version you have installed.

- Ensure you have python version >= 3.8+ installed.

- Using VS Code as our text editor:  right click on the folder explorer and open a terminal

- create and activate your virtual environment 
```sh
python -m venv <envname>
source <envname>/bin/activate
```

- Install the requirements.
```sh
pip install -r requirements.txt
```

That is all, you have successfully created your own virtual environment. Now you can run Python (see above) and start working on your project.

<br/>

### Windows 10 Users

Please install and set up the following packages first. Upgrade if you find the package is already installed:

- Download [Python3](https://www.python.org/downloads/). It is advisable to install the python package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.

  ```sh
  python3 -V
  ```

- Download [pip](https://pip.pypa.io/en/latest/installing/) and follow the instructions in the link as an installation guide.


- Create virtual environment. You could use any virtualenv package of your choice but for Windows, install this virtual environment wrapper:

  ```sh
  python -m pip install virtualenvwrapper-win
  ```

- Create a new virtual environment:

  ```sh
  mkvirtualenv <envname>
  ```

- Activate the virtual environment with:

  ```sh
  workon <envname>
  ```

- Install requirements in the virtual environment created:
  ```sh
  pip install -r requirements.txt
  ```

## PostgreSQL
- Install [PostgreSQL](https://www.postgresql.org/).

- Create a database with PostgresQL, the installation instructions for Fedora can be found [here](https://www.postgresql.org/download/linux/redhat/). Make sure to note Database name, Database Username and Password and also ensure that the server is running

- Create a .env file in the root directory of the project and copy the content of .env.example file to it. Other values not listed below but present in the .env.example file should also be replaced with your own values in your `.env` file.
- Replace `DATABASE_URL` with your database connection string.\

- Run migrations command to create the tables in heroku after deployment.
  ```sh
  flask create_tables
  ```

- Seed data generation. This will generate some data on your local postgresql database for testing purposes. The argument `NUMBER` indicates the amount of seed data to be generated. `NUMBER = 1` will generate 2 User profiles (1 Borrower and 1 Lender),  2 Books (the first Book is borrowed, while second Book is available for loan).
This command will also generate seed data on your heroku database if you execute this command on heroku's console.\
\
Note: The database need to be have been created and the `DATABASE_URL` environment variable is set in your [.env](https://github.com/tosintubi/bookie-map/blob/main/.env.example) file.
  ```sh
  flask generate_data [NUMBER]
  ```
<br/>

## Using the API Endpoint.
* Run server to ensure everything is running properly.

  ```sh
  flask run
  ```
* Refer to the [API documentation](http://127.0.0.1:5000/#/)

<br/>

## OAth Setup Intstructions
### Google
* TBD


<br/>


### Python installation instructions for Windows, macOS and other Linux distro Users

- The following may serve as a guide:
  - (https://www.python.org/downloads/)
  - (https://realpython.com/installing-python/)
  - (https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - (https://realpython.com/learning-paths/flask-by-example/)



## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Server Environment
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Server Framework
- [PostgreSQL](https://www.postgresql.org/) - Database
- [GitHub Actions](https://github.com/features/actions) - CI/CD
- [Heroku](https://www.heroku.com/) - Deployment


## ✍️ Authors <a name = "authors"></a>
- [Tosin](https://github.com/tosintubi) 
## 🤝 Collaboration <a name = "collaboration"></a>

- You need to have PostgresQL installed and set up on your machine.

- Clone the repository from the `staging` branch and please read the [contributing guide](/CONTRIBUTING.md).

- Update your environment variables by remaning the environment variables  file from `.env.example` to `.env` and provide entries for the environment placeholders in the `.env` file.

- To run the testcases covering various functionalities, run the following command in terminal
  ```sh
  python -m unittest -v
  ```

Contact [Toßin](https://github.com/tosintubi) for more details.


## 📝 License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for more details.
