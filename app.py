#!/usr/bin/env python3
from flask import Flask, request,session, redirect,render_template,send_from_directory,jsonify
import os,json,random
from oauth import Oauth



app = Flask(__name__)
app.config["SECRET_KEY"] = "OctoCat"
 

@app.route("/")
def home():
    return render_template("index.html",discord_url=Oauth.discord_login_url)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route("/oauth/authorize")
def oauth():
    return redirect(Oauth.discord_login_url) 

@app.route("/500")
def err500():
    return render_template("500.html")

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsof.icon')

@app.route("/login")
def login():
    code = request.args.get("code")

    at = Oauth.get_access_token(code)
    session["token"] = at
    
    return "Success."

@app.route("/error/sessionnotfound")
def sessionError():
    return render_template("sessionError.html")

@app.route("/invite")
def invite():
    return redirect("https://discord.com/oauth2/authorize?client_id=820308868705812491&scope=bot&permissions=1350036599")

@app.route("/support")
def support():
    return redirect("https://tinyurl.com/octosupport")



if __name__ == "__main__":
    app.run(debug=True)
