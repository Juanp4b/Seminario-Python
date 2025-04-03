# Simule varias partidas de un juego de disparos y genere un ranking basado en el puntaje
# total de cada jugador. Se utilizará el siguiente sistema de puntuación:
#     Acción Puntos
#     Kill 3
#     Asistencia 1
#     Muerte -1
# Imprima las tablas de temp luego de la inserción de cada una de las rondas pudiendo
# ver el progreso en el equipo.
# Además cada ronda debe tener un MVP (Mejor Jugador del Partido/ronda) basado en su
# puntuación. La cantidad de veces que el jugador ha sido MVP también se debe contabilizar
# Se debe imprimir el total de kills, asistencias, muertes, cantidad de MVP y puntos totales. La
# tabla tienen que estar en orden decreciente por los puntos totales.

def tableRow(array,form,divider='no'):
    if divider != 'only':
        print(form.format(*array))
    if divider != 'no':
        leng = len(form.format(*array))
        print('-'*leng)
        
    
def getPoints(stats,skeys,guide):
    return sum(guide[x]*stats[x] for x in skeys)

def getMVP(compare,section):
    return max(compare, key=lambda player: compare[player][section])


def simulateRound(round,guide,resultados):
    temp = {}
    header = ['Jugador','Kills','Asistencias','Muertes','Puntos']
    tab = '{:<8} {:<6} {:<12} {:<7} {:<7}'
    tableRow(header, tab, divider='yes')
    
    for player,stats in round.items():
        line = [player]
        line += (list(stats.values())) # [player, kills, assists, deaths]

        statsKeys = list(stats.keys()) # ['kills', 'assists', 'deaths']
        points = getPoints(stats,statsKeys,guide)
        line += [points] # [player, kills, assists, deaths, points]
        
        # tengo que guardar y sumar todas las estadisticas y puntos de los jugadores
        temp[player] = {**stats, 'points': points} # {player: {'kills': #, 'assists': #, 'deaths': #, 'points': #}, ...}
        for x in statsKeys:
            resultados[player][x] = resultados[player].get(x,0) + stats[x]
        resultados[player]['points'] = resultados[player].get('points',0) + points
        
        tableRow(line, tab)

    tableRow(header, tab, divider='only')

    mvp = getMVP(temp,'points') # obtiene el jugador con la mayor cantidad de puntos
    resultados[mvp]['mvps'] = resultados[mvp].get('mvps',0) + 1
    print(f'MVP de la ronda: {mvp} con {temp[mvp]['points']} puntos.')


def finalRank(resultados):
    header = ['Jugador','Kills','Asistencias','Muertes','MVPs','Puntos']
    tab = '{:<8} {:<6} {:<12} {:<7} {:<5} {:<7}'
    tableRow(header, tab, divider='yes')
    
    for player,stats in resultados.items():
        line = [player]
        line += list(stats.values()) # [player, kills, assists, deaths, mvps, points]
        tableRow(line, tab)
        
    tableRow(header, tab, divider='only')
    


# faster testing stuff, ignore

# rounds = [
#     {
#         'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
#         'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
#         'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
#         'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
#         'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
#     },
#     {
#         'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
#         'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
#         'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
#         'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
#         'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
#     },
#     {
#         'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
#         'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
#         'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
#         'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
#         'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
#     },
#     {
#         'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
#         'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
#         'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
#         'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
#         'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
#     },
#     {
#         'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
#         'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
#         'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
#         'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
#         'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
#     }
# ]

# guide = {
#     'kills': 3,
#     'assists': 1,
#     'deaths': -1
# }

# ranks = {
#     'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
#     'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
#     'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
#     'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
#     'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0}
# }

# for i,r in enumerate(rounds):
#     print(f'Ranking ronda {i}:')
#     simulateRound(r,guide,ranks)
#     print()

# print('Ranking final:')
# finalRank(ranks)