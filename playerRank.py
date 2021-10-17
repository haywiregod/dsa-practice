from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict(
            [(player, Counter()) for player in players])
        print(self.standings)

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
        print(player, self.standings[player])

    def createRanks(self):
        maxScore = -1
        maxScoreOcurrence = 0
        totalRanks = len(self.standings)
        for key, value in self.standings.items():
            if value['score'] >= maxScore:
                maxScore = value['score']
                maxScoreOcurrence += 1
        if maxScoreOcurrence > 1:
            leastGamePlayed = 1000
            leastGamePlayedOcurrence = 0
            for key, value in self.standings.items():
                if value['games_played'] <= leastGamePlayed:
                    leastGamePlayed = value['games_played']
                    leastGamePlayedOcurrence += 1
            if leastGamePlayedOcurrence > 1:
                pass

    def player_rank(self, rank):
        maxScore = -1
        leastGamesPlayed = 1000
        for key, value in self.standings.items():
            if self.standings[key]['score'] > maxScore:
                maxScore = self.standings[key]['score']
        # print(maxScore)
        listOfSameGames = []
        winner = ''
        for key, value in self.standings.items():
            if self.standings[key]['score'] == maxScore:
                # comapre games
                gamesPlayed = self.standings[key]['games_played']
                if gamesPlayed == leastGamesPlayed:
                    return key
                elif gamesPlayed < leastGamesPlayed:
                    leastGamesPlayed = gamesPlayed
                    winner = key

        return winner
        # print("sameScorers", listOfSameScorers)
        leastgame = 10000
        for sameScorer in listOfSameScorers:
            numOfGames = self.standings[sameScorer]['games_played']
            if numOfGames < leastgame:
                leastgame = numOfGames

        # print("sameGames", listOfSameGames)
        # return listOfSameGames[0]
        return None


if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
