class Solution:
    def process_game(self, line):
        game_number = int(line.split(": ")[0].split(" ")[1])
        game = line.split(": ")[1]
        rounds = game.split("; ")
        result = []
        for round in rounds:
            r = {
                "blue": 0,
                "red": 0,
                "green": 0,
            }
            balls = round.split(", ")
            for ball in balls:
                ball = ball.split(" ")
                count = int(ball[0])
                color = ball[1]
                r[color] += count
            result.append(r)
        return game_number, result

    def question_1(self, data):
        result = 0
        for line in data:
            game_number, game = self.process_game(line)
            possible = True
            for round in game:
                if round["red"] > 12 or round["green"] > 13 or round["blue"] > 14:
                    possible = False
                    break
            if possible:
                result += game_number
        return result

    def question_2(self, data):
        result = 0
        for line in data:
            _, game = self.process_game(line)
            max_red = 0
            max_green = 0
            max_blue = 0
            for round in game:
                max_red = max(max_red, round["red"])
                max_green = max(max_green, round["green"])
                max_blue = max(max_blue, round["blue"])
            result += max_red * max_green * max_blue
        return result
