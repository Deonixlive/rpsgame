import kivy
import game
kivy.require("2.0.0")

from kivy.core.window import Window
Window.fullscreen = False

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

paperimg = "assets/Paper.png"
rockimg = "assets/Rock.png"
scissorimg = "assets/Scissor.png"
tieimg = "assets/Tie.png"
playerwin = "assets/playerwin.png"
aiwin = "assets/aiwin.png"
reset = "assets/kiwi.png"
blankimg = "assets/blank.png"
class AIMod(game.Selector):

    #Adding a dictionary with scores for the player, ai and ties.
    def __init__(self):
        self.scores = {"1": 0, "2": 0, "3": 0} #ties, aiwins and playerwins
        super().__init__(5,5)

    def update_scores(self, playerpick, aipick):
        self.outcome = game.winner(playerpick, aipick)
        self.scores[self.outcome] += 1


class mainLayout(FloatLayout):
    ai = AIMod()
    translation_dict = {"R": rockimg, "P": paperimg, "S": scissorimg,
                        "1": aiwin, "2": playerwin, "3": tieimg,
                        "reset": reset, "blank": blankimg}

    def update_display(self):
        self.ids.top1.text = "Player wins: " + str(self.ai.scores["2"])
        self.ids.top2.text = "Ties: " + str(self.ai.scores["3"])
        self.ids.top3.text = "AI wins: " + str(self.ai.scores["1"])
        self.ids.dis_1.source = self.translation_dict[self.playerpick]
        self.ids.dis_2.source = self.translation_dict[self.ai.outcome]
        self.ids.dis_3.source = self.translation_dict[self.aipick]

    def nextround(self, pick):
        self.playerpick = pick
        self.aipick = self.ai.turn()
        self.ai.update_scores(pick[0], self.aipick)
        self.ai.update(pick[0])
        self.update_display()
        print(self.ai.scores)

    def reset(self):
        self.ai = AIMod()
        self.ai.outcome = "reset"
        self.aipick = "blank"
        self.playerpick = "blank"
        self.update_display()
        self.ids.dis_1.text = ""
        self.ids.dis_3.text = ""

class MyApp(App):
    def build(self):
        return mainLayout()


if __name__ == "__main__":
    MyApp().run()
