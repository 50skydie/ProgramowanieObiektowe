class Score_system:
    def __init__(self):
        self._score = 0
        self._hiscore = 200

    def load_hiscore(self):
        score_file = open("highscore.txt", "r")
        self._hiscore = int(score_file.readline())
        score_file.close()

    def save_hiscore(self):
        score_file = open("highscore.txt", "w")
        score_file.write(str(self._hiscore))
        score_file.close()

    def set_hiscore(self):
        if self._score > self._hiscore:
            self._hiscore = self._score
    
    def score_update(self, points):
        self._score += points
    
    def score_reset(self):
        self._score = 0

    def return_score(self):
        return self._score

    def return_hiscore(self):
        return self._hiscore