import click, pytest, sys
import os, csv
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.database import db, get_migrate
from App.models import *
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)
from App.controllers import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''



# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)


@app.cli.command("comps", help="view competitions")
def upload():
    bob = get_all_competitions_json()
    for competitions in bob:
        print(f"Competition Name: {competitions['competition_name']} ")
        print("-" * 40) 

@app.cli.command("results", help="to view all results")
def upload():
  jim = get_all_competitions_results()
  for competitions_results in jim:
        competition_id = competitions_results['competition_id']

        competition = Competitions.query.filter_by(competition_id=competition_id).first()
        print(f"Competition Name: {competition.competition_name} ")
        print(f"Team ID: {competitions_results['team']}")
        print(f"Rank: {competitions_results['rank']}")
        print(f"Score: {competitions_results['score']}")
        print("-" * 40) 


@app.cli.command("upload", help= "to upload data file")
def upload():
    # Load the CSV file
    students_added = {}
    teams_added = {}
    competitions_added = {}


    with open('/workspace/flaskmvc/App/models/soft eng2 a1 sample data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['student_id'] not in students_added:
                    student = Student(student_id=row['student_id'], first_name=row['first_name'], last_name=row['last_name'])
                    db.session.add(student)
                    students_added[row['student_id']] = student  # Track inserted students
                    print('These are ALL competition results')

        #Team table
                if row['team_name'] not in teams_added:
                    team = Team(team_name=row['team_name'])
                    db.session.add(team)
                    teams_added[row['team_name']] = team  # Track inserted teams

        # Competitions table
                if row['competition_name'] not in competitions_added:
                    competitions = Competitions(competition_name=row['competition_name'], date=row['date'], description=row['description'], category=row['category'] )
                    db.session.add(competitions)
                    competitions_added[row['competition_name']] = competitions  # Track inserted competitions
                
        # Competitions Results table
                competitions_results = Competitions_Results(team_id = get_team_id_by_name(row['team_name']) ,competition_id = get_competition_id_by_name(row['competition_name']) , rank = row['rank'], score = row['score'] )
                db.session.add(competitions_results)

            team_membership = Team_Membership(team_id = get_team_id_by_name(row['team_name']), competition_id = get_competition_id_by_name(row['competition_name']), student_id = row['student_id'])
            db.session.add(team_membership)

    db.session.commit()
    print('GREAT SUCCESS')
