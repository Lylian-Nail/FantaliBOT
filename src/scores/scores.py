
class Scores():

    def __init__(self, db_cursor, db_name):
        self.db_cursor = db_cursor

        sql = (
            'CREATE TABLE IF NOT EXISTS players ('
            'playerID BIGINT PRIMARY KEY, '
            'score MEDIUMINT);'
        )
        db_cursor.execute(sql, (db_name))

    def add_score(self, player_id, score):
        sql = (
            'SELECT score FROM players WHERE playerID=?;'
        )
        self.db_cursor.execute(sql, (player_id,))

        if self.db_cursor.fetchone() == None:
            sql = (
                'INSERT INTO players (playerID,score) VALUES (?, ?);'
            )
            self.db_cursor.execute(sql, (player_id, score))
        else:
            sql = (
                'UPDATE players SET score=score+? WHERE playerID=?;'
            )
            self.db_cursor.execute(sql, (score, player_id))
    
    def get_score(self, player_id):
        sql = (
            'SELECT score FROM players WHERE playerID=?;'
        )
        self.db_cursor.execute(sql, (player_id,))
        score = self.db_cursor.fetchone()
        return score[0] if score != None else 0

    def get_scores(self):
        sql= (
            'SELECT score FROM players;'
        )
        self.db_cursor.execute(sql)

        scores = self.db_cursor.fetchall()
        return [int(score) for score in scores]
