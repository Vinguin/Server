import valve.source.a2s
import valve.source.master_server

msq = valve.source.master_server.MasterServerQuerier()
try:
    for address in msq.find(region=[u"eu", u"as"], gamedir=u"tf", map=u"ctf_2fort"):
        server = valve.source.a2s.ServerQuerier(address)
        info = server.info()
        players = server.players()

        print "{player_count}/{max_players} {server_name}".format(**info)
        for player in sorted(players["players"], key=lambda p: p["score"], reverse=True):
            print "{score} {name}".format(**player)
except valve.source.a2s.NoResponseError:
     print "Master server request timed out!"
