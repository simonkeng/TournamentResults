#!/usr/bin/env python
# tournament.py is an implementation of a Swiss-system tournament
# part of Project 4, FSND track with Udacity, Jan 18 2017


import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database. Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print "ERROR"



def deleteMatches():
    """Remove all the match records from the database."""

    connection, c = connect()

    c.execute("TRUNCATE matches;")

    connection.commit()
    connection.close()


def deletePlayers():
    """Remove all the player records from the database."""

    connection, c = connect()

    c.execute("TRUNCATE players CASCADE;")

    connection.commit()
    connection.close()


def countPlayers():
    """Returns the number of players currently registered."""

    connection, c = connect()

    c.execute("SELECT COUNT(*) FROM players;")

    count = c.fetchone()[0]

    connection.commit()
    connection.close()

    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    connection, c = connect()

    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))

    connection.commit()
    connection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    connection, c = connect()

    c.execute("""SELECT players.id, players.name,
                (SELECT COUNT(*) FROM matches WHERE players.id = matches.winner_id)
                as number_of_wins,
                (SELECT COUNT(*) FROM matches WHERE players.id = matches.winner_id
                OR players.id = matches.loser_id)
                as number_of_matches
                FROM players ORDER BY number_of_wins DESC;""")

    fetch = c.fetchall()

    connection.commit()
    connection.close()

    return fetch


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    connection, c = connect()

    c.execute("""INSERT INTO matches (winner_id, loser_id)
                VALUES (%s, %s);""", (winner, loser,))

    connection.commit()
    connection.close()


# this is a genius idea for making the pairing in the swissPairings() function
# much more simple. credit to Chris Ullyott, Udacity FSND student.
def makePairs(list, size=2):
    size = max(1, size)
    return [list[i:i + size] for i in range(0, len(list), size)]


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings. Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    groups_paired = makePairs(standings, 2)

    final_pairs = list()

    for pairs in groups_paired:
        starting_pairs = list()

        for pair in pairs:
            starting_pairs.append(pair[0])
            starting_pairs.append(pair[1])
        final_pairs.append(starting_pairs)

    return final_pairs


# Note: swissPairings() could also be done like this:

# standings = playerStandings()
# pairs = zip(standings[1::2], standings[0::2])
# pairs = [(x[0:2], y[0:2]) for (x,y) in pairs]
# return [(pair[0][0], pair[0][1], pair[1][0], pair[1][1]) for pair in pairs]

# for this approach, credit to Michael Noronha, FSND student,
# for this ultra concise and clean method for
# the pairing. Its literally just four lines of code
# and this doesn't even involve the makePairs() function.


# debugging/dev
# swissPairings()
