def getcmd():
    cmd = input("Commande > ")
    join = cmd.replace(' ', ';')
    listcmd = join.split(';')
    return listcmd