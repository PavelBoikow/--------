import cherrypy
from cherrypy.lib.static import serve_file
import random
import string
import os.path
import sqlite3

class Root:
    @cherrypy.expose
    def index(self, name):
        return serve_file(os.path.join(static_dir, name))

@cherrypy.expose
@cherrypy.tools.json_out()
class StringGeneratorWebService(object):
    @cherrypy.tools.json_in()
    def POST(self, length=8):
        print(cherrypy.request.json)
        json = {}
        json = cherrypy.request.json
        if json['id'] == "reg":
            print (json['mail'])
            flag = 0
            con = sqlite3.connect("metanit.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM people")
            full = cursor.fetchall()
            for t in range(len(full)):
                if full[t][1] == json['mail']:
                    flag=1
                    return {"message": "Пользователь сущестует"}
            if flag == 0:
                con = sqlite3.connect("metanit.db")
                cursor = con.cursor()
                people = (json['mail'], json['password'])
                cursor.execute("INSERT INTO people (mail, pass) VALUES (?, ?)", people)
                con.commit()       
                return {"message": "Пользователь добавлен"}
        if json['id'] == "log":
            if json['mail'] == '':
                return {"message": "Введите данные"}
            print (json['mail'])
            flag = 0
            con = sqlite3.connect("metanit.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM people")
            full = cursor.fetchall()
            for t in range(len(full)):
                if full[t][1] == json['mail']:
                    print(full[t][2])
                    if full[t][2] == json['password']:
                        print(full[t][2])
                        flag=1
                        return {"message": "Вы вошли"}
                    return {"message": "Пароль указан не верно"}
            if flag == 0:     
                return {"message": "Пользователь не существует"}    
        return {"message": "Ошибка"}


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

if __name__=='__main__':
    static_dir = os.path.dirname(os.path.abspath(__file__))  # Root static dir is this file's directory.
    print ("\nstatic_dir: %s\n" % static_dir)
    
    cherrypy.config.update( {  # I prefer configuring the server here, instead of in an external file.
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 3000,
        } )
    conf = {
         '/': {  # Root folder.
            'tools.staticdir.on':   True,  # Enable or disable this rule.
            'tools.staticdir.root': static_dir,
            'tools.staticdir.dir':  '',
        },
        '/api':{
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }

    webapp = StringGenerator()
    webapp.api = StringGeneratorWebService()
    cherrypy.quickstart(webapp, '/', conf)  # ..and LAUNCH ! :)
    