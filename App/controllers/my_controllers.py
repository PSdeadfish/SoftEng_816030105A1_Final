from App.models import *
from App.database import db

def create_student(student_id, first_name, last_name):
    newstudent = Student(student_id=student_id, first_name=first_name, last_name=last_name)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent

def get_student_by_first_name(first_name):
    return User.query.filter_by(first_name=first_name).first()

def get_student(id):
    return User.query.get(id)

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students = [student.get_json() for student in students]
    return students

def update_student(id, first_name,last_name):
    student = get_student(id)
    if student:
        student.first_name = first_name
        student.last_name = last_name
        db.session.add(student)
        return db.session.commit()
    return None


def create_competition(competition_name, date, description, category):
    newcompetition = Competitions(competition_name,date,description,category)
    db.session.add(newcompetition)
    db.session.commit()
    return newcompetition

def get_competition_by_name(competition_name):
    return Competitions.query.filter_by(competition_name=competition_name).first()

def get_competition_id_by_name(competition_name):
    myComp = Competitions.query.filter_by(competition_name=competition_name).first()
    return myComp.competition_id

def get_competition(competition_id):
    return Competitions.query.get(competition_id)

def get_all_competitions():
    return Competitions.query.all()

def get_all_competitions_json():
    competitions = Competitions.query.all()
    if not competitions:
        return []
    competitions = [competitions.get_json() for competitions in competitions]
    return competitions

def update_competition(competition_id, competition_name):
    competition = get_competition(competition_id)
    if competition:
        competition.competition_name = competition_name
        db.session.add(competition)
        return db.session.commit()
    return None


def create_team(team_name):
    newteam = Team(team_name)
    db.session.add(newteam)
    db.session.commit()
    return newteam

def get_team_by_name(team_name):
    return Team.query.filter_by(team_name=team_name).first()

def get_team_id_by_name(team_name):
    myTeam = Team.query.filter_by(team_name=team_name).first()
    return myTeam.team_id

def get_team(team_id):
    return Team.query.get(team_id)

def get_all_teams():
    return Team.query.all()

def get_all_teams_json():
    teams = Team.query.all()
    if not teams:
        return []
    teams = [team.get_json() for team in teams]
    return team

def update_team(team_id,team_name):
    team = get_team(team_id)
    if team:
        team.team_name = team_name
        db.session.add(team)
        return db.session.commit()
    return None


def create_team_membership(team_id, competition_id, student_id):
    newteam_membership = Team_Membership(team_id, competition_id, student_id)
    db.session.add(newteam_membership)
    db.session.commit()
    return newteam_membership

def create_competitions_results(team_id, competition_id, rank, score):
    newresults = Competitions_Results(team_id, competition_id, rank,score)
    db.session.add(newresults)
    db.session.commit()
    return newresults

def get_all_competitions_results():
    return Competitions_Results.query.all()

def get_all_competitions_results():
    competitions_results = Competitions_Results.query.all()
    if not competitions_results:
        return []
    competitions_results = [competitions_results.get_json() for competitions_results in competitions_results]
    return competitions_results





