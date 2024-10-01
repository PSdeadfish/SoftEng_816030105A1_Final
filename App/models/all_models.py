from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    first_name =  db.Column(db.String(120), nullable=False, unique=False)
    last_name = db.Column(db.String(120), nullable=False, unique=False)

    def __init__(self, student_id, first_name, last_name ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    def get_json(self):
        return{
            'id': self.student_id,
            'first name': self.first_name,
            'last name': self.last_name
        }

class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name =  db.Column(db.String(120), nullable=False, unique=False)

    def __init__(self,team_name):
        self.team_name = team_name

    def get_json(self):
        return{
            'id': self.team_id,
            'team name': self.team_name,
        }

class Competitions(db.Model):
    competition_id = db.Column(db.Integer, primary_key=True)
    competition_name =  db.Column(db.String(120), nullable=False, unique=False)
    date = db.Column(db.String(120), nullable=False, unique=False)
    description = db.Column(db.String(120), nullable=False, unique=False)
    category = db.Column(db.String(240), nullable=False)

    def __init__(self, competition_name,date, description, category):
        self.competition_name = competition_name
        self.date = date
        self.description = description
        self.category = category

    def get_json(self):
        return{
            'id': self.competition_id,
            'competition_name': self.competition_name,
        }


class Competitions_Results(db.Model):
    results_id = db.Column(db.Integer, primary_key=True)
    team_id =  db.Column(db.Integer,db.ForeignKey('team.team_id'), nullable=False, unique=False)
    competition_id = db.Column(db.Integer,db.ForeignKey('competitions.competition_id'), nullable=False, unique=False)
    rank = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, team_id, competition_id, rank, score):
        self.team_id = team_id
        self.competition_id = competition_id
        self.rank = rank
        self.score = score

    def get_json(self):
        return{
            'competition_id': self.competition_id,
            'team': Team.query.filter_by(team_id=self.team_id).first(),
            'rank': self.rank,
            'score': self.score,
        }
        
class Team_Membership(db.Model):
    membership_id = db.Column(db.Integer, primary_key=True)
    team_id =  db.Column(db.String(120),db.ForeignKey('team.team_id'), nullable=False, unique=False)
    competition_id = db.Column(db.String(120),db.ForeignKey('competitions.competition_id'), nullable=False, unique=False)
    student_id = db.Column(db.String(120),db.ForeignKey('student.student_id'), nullable=False, unique=False)

    def __init__(self, team_id, competition_id, student_id):
        self.team_id = team_id
        self.competition_id = competition_id
        self.student_id = student_id

    def get_json(self):
        return{
            'id': self.membership_id,
            'team id': self.team_id,
            'competition id': self.competition_id,
            'student id': self.student_id,
        }


