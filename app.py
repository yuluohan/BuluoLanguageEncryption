from flask import Flask
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators
from flask import render_template
from logging.config import dictConfig


import core



dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



app = Flask(__name__)
app.config['DEBUG'] = False
app.config["SECRET_KEY"] = "regju34783567@#$%@#Ddf42"



class NewPostForm(FlaskForm):

    text = TextAreaField('text', validators=[validators.DataRequired()])
    encode = SubmitField('加密') 
    decode = SubmitField('解密')




@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewPostForm()
    result = ''
    error = ''
    try:
        if form.data['decode']:
            app.logger.info('解密：%s',form.data['text'])
            result = core.decode_by_boluo(form.data['text'])
        elif form.data['encode']:
            app.logger.info('加密：%s', form.data['text'])
            result = core.encode_by_boluo(form.data['text'])
        else:
            app.logger.info('刷新')
    except:
        error = '解密失败'
        app.logger.info('失败')

    return render_template('index.html', form=form, result=result, error=error)



if __name__ == '__main__':
    app.run()
