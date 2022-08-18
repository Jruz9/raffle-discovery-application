from flask_sqlalchemy import SQLAlchemy

raffle_database = SQLAlchemy()


class Raffle(raffle_database.Model):
    __tablename__ = 'raffle'

    raffle_id = raffle_database.Column(raffle_database.Integer, primary_key=True)
    raffle_name = raffle_database.Column(raffle_database.String, nullable=False)
    raffle_prizes = raffle_database.Column(raffle_database.Integer, nullable=False)
    project_rating = raffle_database.Column(raffle_database.Enum("trash", "decent", "good", "great"))

    def __init__(self, raffle_name: str, raffle_prize: int, project_rating: str) -> None:
        super().__init__()
        self.raffle_name = raffle_name
        self.raffle_prizes = raffle_prize
        self.project_rating = project_rating

    def __repr__(self) -> str:
        return f'Raffle({self.raffle_name},{self.raffle_prizes},{self.project_rating})'
