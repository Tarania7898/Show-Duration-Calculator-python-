noSeasons = int(input("How many seasons? "))
noEpisodes = int(input("How many episodes per season? "))
noEpDur = int(input("How long is each episode? (min.) "))

noEpisodesTot = noEpisodes * noSeasons
noSeasDurTot = noEpDur * noEpisodes

noMinTot = noEpDur * noEpisodesTot
noHourTot = noMinTot // 60
noDayTot = noHourTot // 24

print(noEpisodesTot, "total episodes")
print(noSeasDurTot, "total season duration (min.)")
print(noMinTot, "total minutes")
print(noHourTot,  "total hours")
print(noDayTot,  "total days")