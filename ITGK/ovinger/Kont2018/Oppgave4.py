def importResults(file):
        while True:
            if file == 'q':
                break
            try:
                with open(file, 'r') as f:
                    lines = []
                    for line in f.readlines():
                        line = line.strip()
                        lines.append(line)
                    return lines

            except:
                file = input(str(file) + " Could not be fount. File name ('q' exits): ")


def analyseResults(results):
    for i in range(len(results)):
        results[i] = results[i].split(',')
        results[i][-1] = results[i][-1].split('-')
        results[i][2:] = [int(results[i][-1][0]), int(results[i][-1][1])]
    return results

def calculateScores(homeGoals, awayGoals):
    if homeGoals > awayGoals:
        return 3,0
    if homeGoals < awayGoals:
        return 0,3
    return 1,1



def sumTeamValues(analyzed):
    db = {}
    for i in range(len(analyzed)):
        if analyzed[i][0] not in db:
            db[analyzed[i][0]] = [0, 0]
        if analyzed[i][1] not in db:
            db[analyzed[i][1]] = [0, 0]

        score = calculateScores(analyzed[i][-2], analyzed[i][-1])

        db[analyzed[i][0]][0] += score[0]
        db[analyzed[i][0]][1] += 1

        db[analyzed[i][1]][0] += score[1]
        db[analyzed[i][1]][1] += 1

    return db


