# Tournament Results

This is project 4 on the full stack nanodegree path with Udacity, and is the last project in the [intro to relational databases course](https://www.udacity.com/course/intro-to-relational-databases--ud197).

#### Project Overview

In this project I built a python module that uses PostgreSQL database to keep track of players and matches in a swiss-system tournament.

### Run it locally

1. Install [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/)
2. Clone this repository https://github.com/simonkeng/TournamentResults.git
3. Launch the Vagrant VM by going into the directory where these files reside, and run the command `vagrant up`, which may take one minute or two. Once its finished run `vagrant ssh` to launch the VM.
4. Once here, you may access the PostgreSQL database with the command `psql` from inside the VM.
5. And you can link to the tournament.sql with `\c tournament`. After this you'll be able to run queries on the database.
6. To run 10 tests on the tournament system and my code, exit the database with `\q` and then run `python tournament_test.py`.



Thanks!