from utils.utils import DB,RequestJson


class ImageJudge:
    _host = "192.168.10.32"
    _port = 3306
    _user_db = "root"
    _pswd_db = "deepwise"
    _database = "dw_aiserver_config"
    _method = "POST"
    _json_login = {"name": "deepwise123", "pass": "Deepwise!@#123"}
    _json_restart = {"serverName": "allJava"}
    _header = {"Content-Type":"application/json"}
    _url_login = "http://{}:81/aiconsole/user/login".format(_host)
    _url_restart = "http://{}:81/aiconsole/server/restart".format(_host)

    def set_im_judge(self, sql):
        db = DB(self._host, self._port, self._user_db, self._pswd_db, self._database)
        db.handle_db(sql, method="Check")
        db.close_db()

    def restart_server(self):
        request = RequestJson()
        token = request.json_parse(request.request(self._method, self._url_login, json=self._json_login,
                                                   headers=self._header), "$..data.token")
        request.request(self._method, self._url_restart, headers={"token": token, "Content-Type": "application/json"},
                        json=self._json_restart)

    def push_data(self):
        pass

