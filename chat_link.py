from filetail import FileTail  # import the script to tail files like in linux
from server_data import console_in
from server_data import console_out
from server_data import death_messages
from server_data import server_mappings


def server_link(line, server):
    # format the chat message, message starts with [server] in yellow
    msg = 'tellraw @a [{{\"text\":\"[{}] \", \"color\":\"yellow\"}}, ' \
          '{{\"text\":\"{}\", \"color\":\"white\"}}]\n'.format(server, line[33:-1])
    for s in server_mappings.keys():  # write to all servers that are not the server where the messages comes from
        if s != server:
            with open(console_in.format(server_mappings[s]), 'w') as f:
                f.writelines(msg)
                f.close()


# survival
# chat link blocking code
def chat_link(server):
    tail = FileTail(console_out.format(server_mappings[server]))  # tail the console.out file
    for line in tail:
        if '[Server thread/INFO]' in line:  # check if the new line was of the correct type
            if line[33] == '<' and '>' in line:  # check if the the message was sent by a player i.e. <player>
                server_link(line, server)
                return line
            elif line[33] == '*':  # to also send messages generated by \me
                server_link(line, server)
                return line
            elif 'joined the game' in line:  # sent player join messages
                server_link(line, server)
                return line
            elif 'left the game' in line:  # sent player leave messages
                server_link(line, server)
                return line

            # if the message wasn't yet recognised as a valid message it could still be a death message
            # to check for death messages we check if a death message is in the line by looping over
            # the list with death messages and checking if they are in the line
            # ignore some annoying console messages when villagers die
            for i in death_messages:
                if i in line and 'Villager class' not in line:
                    server_link(line, server)
                    return line
    return
