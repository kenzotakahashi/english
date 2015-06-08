# -*- coding: utf-8 -*-
from flask import Flask, render_template
# from flask.ext.script import Manager

app = Flask(__name__)
app.debug = True

# manager = Manager(app)

@app.route('/')
def index():
	return render_template('index.html')


# @app.route('/user/<name>')
# def user(name):
# 	return render_template('user.html', name=name)

@app.route('/post/<name>')
def post(name):
	return render_template('posts/' + name + '.html')

@app.context_processor
def inject_user():
    return {
		"posts": [
			("名詞", "名詞"),
			("動詞", "動詞"), 
			("名詞２", "名詞２"),
			("形容詞", "形容詞"),
			("動詞２", "動詞２"), 
			("副詞", "副詞"),
			("前置詞", "前置詞"),
			("現在進行形(I am doing)", "現在進行形"),
			("現在形(I do)", "現在形"),
			("be動詞(I am~, I was~)", "be動詞"),
			("過去形(I did)", "過去形"),
			("過去進行形(I was doing)", "過去進行形"),
			("命令形", "命令形"),
			("接続詞", "接続詞"),
			("名詞３", "名詞３"),
			("現在完了形１(I have done)", "現在完了形１"),
			("現在完了形２(I have done)", "現在完了形２"),
			("現在完了進行形(I have been doing)", "現在完了進行形"),
			("過去完了形(I had done)", "過去完了形"),
			("過去完了進行形(I had been doing)", "過去完了進行形"),
			("used to (do)", "used_to"),
			("(I'm) going to (do)", "going_to"),
			("will", "will"),
			("現在形を使った未来形", "現在形を使った未来形"),
			("can", "can"),
			("When I do", "when_I_do"),
			("must", "must"),
			("might", "might"),
			("may", "may"),
			("should", "should"),
			("would", "would"),
			("If I do", "If_I_do"),
			("could", "could"),
			("受動態(is done)", "受動態"),
			("There (is)", "there_is"),
		]
    }

if __name__ == '__main__':
	app.run()
    # app.run(host='0.0.0.0')
