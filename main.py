# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
# from flask.ext.script import Manager

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'

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
		("名詞１", "名詞１"),
		("動詞１", "動詞１"), 
		("名詞２(a, an, the)", "名詞２"),
		("形容詞", "形容詞"),
		("動詞２ - 状態を表す動詞", "動詞２"), 
		("副詞", "副詞"),
		("前置詞", "前置詞"),
		("現在形(I do)", "現在形"),
		("現在進行形(I am doing)", "現在進行形"),
		("be動詞(I am~, I was~)", "be動詞"),
		("過去形(I did)", "過去形"),
		("過去進行形(I was doing)", "過去進行形"),
		("不定詞(to do)","不定詞"),
		("命令形", "命令形"),
		("接続詞", "接続詞"),
		("名詞３(mine, myself)", "名詞３"),
		("現在完了形１(I have done)", "現在完了形１"),
		("現在完了形２(I have done)", "現在完了形２"),
		("現在完了進行形(I have been doing)", "現在完了進行形"),
		("used to (do)", "used_to"),
		("(I'm) going to (do)", "going_to"),
		("will", "will"),
		("現在形を使った未来形(I am doing/I do)", "現在形を使った未来形"),
		("When (I do)", "When_I_do"),
		("過去完了形(I had done)", "過去完了形"),
		("過去完了進行形(I had been doing)", "過去完了進行形"),
		("can", "can"),
		("must", "must"),
		("mustとhave toの違い","must,have_to"),
		("might", "might"),
		("may", "may"),
		("should", "should"),
		("would", "would"),
		("If (I do)", "If_I_do"),
		("could", "could"),
		("There (is)", "there_is"),
		("some, any","some,any"),
		("受動態 (is done)", "受動態"),
		("no, none", "no,none"),
		("数や量を表す代名詞","数や量を表す代名詞"),
		# ("all,every,whole,each",""),
		# ("another,other",""),
		("both, neither, either","both,neither,either"),
		("名詞節","名詞節"),
		("ingとedで終わる形容詞","ingとedで終わる形容詞"),
		("形容詞節１（関係代名詞）","形容詞節１"),
		("形容詞節２","形容詞節２"),
		("形容詞節３","形容詞節３"),
		("形容詞節４","形容詞節４"),
		("動詞の形容詞的活用","動詞の形容詞的活用"),
		("比較級１","比較級１"),
		("比較級２","比較級２"),
		("最上級","最上級"),
		("動名詞(doing)","動名詞"),
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
		("[i]の発音","i"),
		("[ɪ]の発音","ɪ"),
		("[eɪ]の発音","eɪ"),
		("[ɛ]の発音","ɛ"),
		("[æ]の発音","æ"),
		("[a]の発音","a"),
		("[ɔ]の発音","ɔ"),
		("[u]の発音","u"),
		("[ʊ]の発音","ʊ"),
		("[oʊ]の発音","oʊ"),
		("[ə]の発音","ə"),
		("[aɪ]の発音","aɪ"),
		("[aʊ]の発音","aʊ"),
		("[ɔɪ]の発音","ɔɪ"),	
		("[ər]の発音","ər"),
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

@app.route('/article/<name>')
def articlePost(name):
	return render_template('posts/article/' + name + '.html')	

@app.route('/pronunciation/vowels/<name>')
def vowels(name):
	return render_template('posts/発音/vowels/' + name + '.html')

@app.route('/pronunciation/consonants/<name>')
def consonants(name):
	return render_template('posts/発音/consonants/' + name + '.html')

@app.route('/resources')
def resources():
	return render_template('resources.html')

@app.route('/writing/<name>')
def writingPost(name):
	return render_template('posts/writing/' + name + '.html')	

@app.route('/writing')
def writing():
	posts = [
		("Poor and traumatized at Harvard","poor_and_traumatized_at_harvard"),
		("31 Things I’d Have Told Myself Before College","a-few-more-things-i-learned-in-college")
	]
	return render_template('writing.html', posts=posts)

@app.route('/article')
def article():
	posts = [
		("英文を構築するプロセス","英文を構築するプロセス")
	]
	return render_template('article.html', posts=posts)



if __name__ == '__main__':
	app.run()
    # app.run(host='0.0.0.0')
