import socket
import sys

import hlt


class Game(hlt.Game):
    def __init__(self, *args, **kwargs):
        self._buf = []
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 1337
        self._connection.connect(("localhost", port))
        print("Connected to intermediary on port #", port)
        super().__init__(*args, **kwargs)

    def _send_string(self, s):
        """
        Send data to the game. Call :function:`done_sending` once finished.
        :param str s: String to send
        :return: nothing
        """
        self._buf.append(s)

    def _done_sending(self):
        """
        Finish sending commands to the game.
        :return: nothing
        """
        self._connection.sendall((''.join(self._buf) + "\n").encode("ascii"))
        self._buf.clear()

    def _get_string(self):
        """
        Read input from the game.
        :return: The input read from the Halite engine
        :rtype: str
        """
        buf = []
        while True:
            c = self._connection.recv(1).decode("ascii")
            if c == "\n" or not c:
                break
            else:
                buf.append(c)
        if not c:
            sys.exit()
        return "".join(buf)

    def send_command_queue(self, command_queue):
        """
        Issue the given list of commands.
        :param list[str] command_queue: List of commands to send the Halite engine
        :return: nothing
        """
        for command in command_queue:
            self._send_string(command)

        self._done_sending()