# -*- coding: utf-8 -*-
from flask import Flask, render_template
# from flask.ext.script import Manager

app = Flask(__name__)
app.debug = True

# manager = Manager(app)

# ================= English Corner =====================

@app.route('/ec')
def ec():
	return render_template('englishCorner/ec.html')

@app.route('/ec/<name>')
def ecSession(name):
	return render_template('englishCorner/ec' + name + '.html')

#=====================================================

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/grammar')
def grammar():
	posts = [
		("名詞", "名詞"),
		("動詞", "動詞"), 
		("名詞２ - 冠詞", "名詞２"),
		("形容詞", "形容詞"),
		("動詞２ - 状態を表す動詞", "動詞２"), 
		("副詞", "副詞"),
		("前置詞", "前置詞"),
		("現在形(I do)", "現在形"),
		("現在進行形(I am doing)", "現在進行形"),
		("be動詞(I am~, I was~)", "be動詞"),
		("過去形(I did)", "過去形"),
		("過去進行形(I was doing)", "過去進行形"),
		("不定詞","不定詞"),
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
		("現在形を使った未来形(I am doing/I do)", "現在形を使った未来形"),
		("can", "can"),
		("When (I do)", "When_I_do"),
		("must", "must"),
		("mustとhave toの違い","must,have_to"),
		("might", "might"),
		("may", "may"),
		("should", "should"),
		("would", "would"),
		("If (I do)", "If_I_do"),
		("could", "could"),
		("受動態 (is done)", "受動態"),
		("There (is)", "there_is"),
		("some, any","some,any"),
		("no, none", "no,none"),
		("数や量を表す代名詞","数や量を表す代名詞"),
		# ("all,every,whole,each",""),
		# ("another,other",""),
		("both, neither, either","both,neither,either"),
		("名詞節","名詞節"),
		("ingとedで終わる形容詞","ingとedで終わる形容詞"),
		("形容詞節（関係代名詞）","形容詞節"),
		("形容詞節２","形容詞節２"),
		("形容詞節３","形容詞節３"),
		("形容詞節４","形容詞節４"),
		("動詞の形容詞的活用","動詞の形容詞的活用"),
		("比較級","比較級"),
		("比較級２","比較級２"),
		("最上級","最上級"),
		("動名詞","動名詞"),
		# ("",""),					
		# ("",""),					
		# ("",""),					
		# ("",""),					
	]
	return render_template('grammar.html', posts=posts)

@app.route('/pronunciation')
def pronunciation():
	posts = [
		("発音 - イントロダクション","イントロダクション"),
		# ("",""),
		# ("",""),
		# ("",""),
	]

	vowels = [
		("[i]","i"),
		("[ɪ]","ɪ"),
		("[eɪ]","eɪ"),
		("[ɛ]","ɛ"),
		("[æ]","æ"),
		("[a]","a"),
		("[ɔ]","ɔ"),
		("[u]","u"),
		("[ʊ]","ʊ"),
		("[oʊ]","oʊ"),
		("[ə]","ə"),
		("[aɪ]","aɪ"),
		("[aʊ]","aʊ"),
		("[ɔɪ]","ɔɪ"),	
		("[ər]","ər"),
	]

	consonants = [
		("[m]の発音","m"),
		("[n]の発音","n"),
		("[ŋ]の発音","ŋ"),
		("[l]の発音","l"),
		("[r]の発音","r"),
		("[w]の発音","w"),	
		("[j]の発音","j"),
		("[h]の発音","h"),
		("[p]の発音","p"),
		("[b]の発音","b"),
		("[k]の発音","k"),
		("[g]の発音","g"),
		("[f]の発音","f"),
		("[v]の発音","v"),
		("[s]の発音","s"),
		("[z]の発音","z"),
		("[θ]の発音","θ"),
		("[ð]の発音","ð"),	
		("[ʃ]の発音","ʃ"),
		("[ʒ]の発音","ʒ"),
		("[tʃ]の発音","tʃ"),
		("[dʒ]の発音","dʒ"),
		("[t]の発音","t"),
		("[d]の発音","d"),
	]

	return render_template('pronunciation.html', posts=posts, vowels=vowels, consonants=consonants)


@app.route('/post/<name>')
def post(name):
	return render_template('posts/' + name + '.html')

@app.route('/pronunciation/<name>')
def pronunciationPost(name):
	return render_template('posts/発音/' + name + '.html')

@app.route('/pronunciation/vowels/<name>')
def vowels(name):
	return render_template('posts/発音/vowels/' + name + '.html')

@app.route('/pronunciation/consonants/<name>')
def consonants(name):
	return render_template('posts/発音/consonants/' + name + '.html')



# @app.context_processor
# def inject_user():
#     return {
# 		"posts": [
# 			("名詞", "名詞"),
# 			("動詞", "動詞"), 
# 			("名詞２ - 冠詞", "名詞２"),
# 			("形容詞", "形容詞"),
# 			("動詞２ - 状態を表す動詞", "動詞２"), 
# 			("副詞", "副詞"),
# 			("前置詞", "前置詞"),
# 			("現在形(I do)", "現在形"),
# 			("現在進行形(I am doing)", "現在進行形"),
# 			("be動詞(I am~, I was~)", "be動詞"),
# 			("過去形(I did)", "過去形"),
# 			("過去進行形(I was doing)", "過去進行形"),
# 			("不定詞","不定詞"),
# 			("命令形", "命令形"),
# 			("接続詞", "接続詞"),
# 			("名詞３", "名詞３"),
# 			("現在完了形１(I have done)", "現在完了形１"),
# 			("現在完了形２(I have done)", "現在完了形２"),
# 			("現在完了進行形(I have been doing)", "現在完了進行形"),
# 			("過去完了形(I had done)", "過去完了形"),
# 			("過去完了進行形(I had been doing)", "過去完了進行形"),
# 			("used to (do)", "used_to"),
# 			("(I'm) going to (do)", "going_to"),
# 			("will", "will"),
# 			("現在形を使った未来形(I am doing/I do)", "現在形を使った未来形"),
# 			("can", "can"),
# 			("When (I do)", "When_I_do"),
# 			("must", "must"),
# 			("mustとhave toの違い","must,have_to"),
# 			("might", "might"),
# 			("may", "may"),
# 			("should", "should"),
# 			("would", "would"),
# 			("If (I do)", "If_I_do"),
# 			("could", "could"),
# 			("受動態 (is done)", "受動態"),
# 			("There (is)", "there_is"),
# 			("some, any","some,any"),
# 			("no, none", "no,none"),
# 			("数や量を表す代名詞","数や量を表す代名詞"),
# 			# ("all,every,whole,each",""),
# 			# ("another,other",""),
# 			("both, neither, either","both,neither,either"),
# 			("名詞節","名詞節"),
# 			("ingとedで終わる形容詞","ingとedで終わる形容詞"),
# 			("形容詞節（関係代名詞）","形容詞節"),
# 			("形容詞節２","形容詞節２"),
# 			("形容詞節３","形容詞節３"),
# 			("形容詞節４","形容詞節４"),
# 			("動詞の形容詞的活用","動詞の形容詞的活用"),
# 			("比較級","比較級"),
# 			("比較級２","比較級２"),
# 			("最上級","最上級"),
# 			("動名詞","動名詞"),
# 			# ("",""),					
# 			# ("",""),					
# 			# ("",""),					
# 			# ("",""),					
# 		]
#     }

if __name__ == '__main__':
	app.run()
    # app.run(host='0.0.0.0')
