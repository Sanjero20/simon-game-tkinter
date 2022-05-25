class ScoringSystem:
    def get_highscore(self):
        """
        Retrieve previous highscore from txt file, 
        if not found, create a file and set highscore to zero
        """
        try:
            file = open("highscore.txt")
        except FileNotFoundError:
            file = open("highscore.txt", "w")
            file.write("0")
        else:
            highscore = file.read()
            if highscore:
                self.highscore.set(int(highscore))
            file.close()

        self.highscore_txt.set(f"Highscore: {self.highscore.get()}")

    def set_highscore(self):
        """Check if the score is higher than the highscore"""
        if self.score.get() > self.highscore.get():
            self.highscore.set(self.score.get())
            self.highscore_txt.set(f"Highscore: {self.highscore.get()}")
            self.window.update()

        with open("highscore.txt", "w") as file:
            file.write(str(self.highscore.get()))

    def add_score(self):
        """Add score"""
        score = self.score.get()
        self.score.set(score+1)
        self.score_txt.set(f"Score: {self.score.get()}")
   
    def reset_score(self):
        self.score.set(0)
        self.score_txt.set(f"Score: {self.score.get()}")