# -*- coding: utf-8 -*-

import json

from flask_script import Manager, Server

from apps.main import app_factory


manager = Manager(app_factory)


def pretty_print(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    server = Server(host="localhost", port=12345)
    manager.add_command("runserver", server)
    manager.run()
