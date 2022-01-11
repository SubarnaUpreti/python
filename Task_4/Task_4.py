import sys


class Teams:
    def __init__(self):
        self.name = ""
        self.played = 0
        self.won = 0
        self.lost = 0
        self.draw = 0
        self.score_for = 0
        self.score_against = 0

    def get_difference(self):
        return self.score_for - self.score_against

    def get_points(self):
        return self.won * 3 + self.draw


teams = {}

with open("results.txt", "r", encoding="utf-8") as results:
    for line in results:
        try:
            teams_and_scores = line.split(',')
            first_team = teams_and_scores[0]
            first_team_score = int(teams_and_scores[1])
            second_team = teams_and_scores[2]
            second_team_score = int(teams_and_scores[3])
            draw = False
            first_won = False
            if first_team not in teams:
                teams[first_team] = Teams()
                teams[first_team].name = first_team.ljust(15, " ")
            if second_team not in teams:
                teams[second_team] = Teams()
                teams[second_team].name = second_team.ljust(15, " ")

            teams[first_team].played += 1
            teams[first_team].score_for += int(first_team_score)
            teams[first_team].score_against += int(second_team_score)

            teams[second_team].played += 1
            teams[second_team].score_for += int(second_team_score)
            teams[second_team].score_against += int(first_team_score)
        except:
            print("Error in the data stored format.\nExiting the program")
            sys.exit()

        if first_team_score == second_team_score:
            teams[first_team].draw += 1
            teams[second_team].draw += 1
        elif first_team_score > second_team_score:
            teams[first_team].won += 1
            teams[second_team].lost += 1
        else:
            teams[first_team].lost += 1
            teams[second_team].won += 1


sorted_team = dict(sorted(teams.items(), key=lambda item: (item[1].get_points(), item[1].get_difference()), reverse=True))

adjust = 5

if len(sys.argv) >= 2:
    print(f"\n{sys.argv[1]}\n{'='*len(sys.argv[1])}\n")

print(" ".rjust(15, " "), "P".rjust(adjust, ' '), "W".rjust(adjust, ' '), "D".rjust(adjust, ' '), "L".rjust(adjust, ' '),
      "F".rjust(adjust, ' '), "A".rjust(adjust, ' '), "Diff".rjust(adjust, ' '), "Pts".rjust(adjust, ' '))

for i, j in sorted_team.items():
    print(f"{j.name} {str(j.played).rjust(adjust, ' ')} {str(j.won).rjust(adjust, ' ')} {str(j.draw).rjust(adjust, ' ')} "
          f"{str(j.lost).rjust(adjust, ' ')} {str(j.score_for).rjust(adjust, ' ')} "
          f"{str(j.score_against).rjust(adjust, ' ')} {str(j.get_difference()).rjust(adjust, ' ')} "
          f"{str(j.get_points()).rjust(adjust, ' ')}")
    