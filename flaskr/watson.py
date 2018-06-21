# -*- coding: utf-8 -*-
from flask import (
    Blueprint, render_template, request
)
import json

# 'blog':blueprint名
# __name__:モジュール名
bp = Blueprint('watson', __name__)

# URLパス/への応答
@bp.route('/', methods=('GET', 'POST'))
def index():

    # POST要求の場合
    if request.method == 'POST':
        
        # サイズ値返却
        images = [{'filename': 'img/01_angry.jpg', 'width': 20, 'height': 20},
                 {'filename': 'img/02_disgust.jpg', 'width': 20, 'height': 20},
                 {'filename': 'img/03_fear.jpg', 'width': 20, 'height': 20},
                 {'filename': 'img/04_joy.jpg', 'width': 20, 'height': 20},
                 {'filename': 'img/05_sadness.jpg', 'width': 20, 'height': 20}]
        print("要求:", request)
        print("要求[form]:", request.form)
        # テキストボックス入力値
        comment = request.form['comment']
        print("コメント:", comment)
        if not request.form.getlist("language"):
            language = "en"
        else:
            language = "ja"
        print("言語:", language)

# Watson:Natural Language Understanding0
# 日本語か英語かを分析
#        from watson_developer_cloud import NaturalLanguageUnderstandingV1
#        from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions
#        from watson_developer_cloud.watson_service import WatsonApiException
#        natural_language_understanding = NaturalLanguageUnderstandingV1(
#          username='e6c17e9c-c00c-471b-8de0-ad5b33799eb3',
#          password='HAHE0X4ZWyhR',
#          version='2018-03-16')
#        language='error'
#        try:
#            response = natural_language_understanding.analyze(
#              text=comment,
#              features=Features(
#                  entities=EntitiesOptions(
#                  emotion=True,
#                  sentiment=True,
#                  limit=2),
#            ))
#            language = response['language']
#            print(json.dumps(language, indent=2))
#        except WatsonApiException:
#            print("NaturalLanguageUnderstanding error")
#            messages=('入力言語を判断できませんでした',)
#            print(language)

#        if(language != 'error'):

# Watson:Language Translater
# 翻訳処理(日本語->英語)：翻訳精度が悪い、Google翻訳を介した方が感情分析の精度は高い
        if(language == 'ja'):
            from watson_developer_cloud import LanguageTranslatorV3
            language_translator = LanguageTranslatorV3(
                    version='2018-05-01',
                    iam_api_key='YRH0vpBeJhjmqAKNeR2OqSlPGlZMgIVi8cRjs1L4doPS')
            translation = language_translator.translate(
                    text=comment,
                    model_id='ja-en')
            comment = translation['translations'][0]['translation']
            print("Watson Language Transfer(json):", json.dumps(translation, indent=2))
            print('翻訳後：', comment)

# Watson:Tone Analyzer    
# 感情分析
        # Watson問い合わせ用インスタンス生成
        from watson_developer_cloud import ToneAnalyzerV3
        tone_analyzer = ToneAnalyzerV3(
                version ='2017-09-21',
                username ='fa76b991-555e-43a8-a205-7ce82f7db28b',
                password ='qzLFvFo2LoTE')
        text = comment
        content_type = 'application/json'
        tone = tone_analyzer.tone({"text": text},content_type)
        print("Watson Tone Analyzer(json):", json.dumps(tone, indent=2))
        tones_data = tone['document_tone']['tones']

        if(len(tones_data) > 0):
            tone_data = tones_data[0]
            messages=(tone_data['tone_id'],
                      tone_data['score'])
        else:
            messages=('感情を含んだ文章を入力してください',)
        
        if(len(tones_data) > 0):
            tone_data = tones_data[0]
            if(tone_data['tone_id'] == 'anger'):
                images[0]['width'] = 100 * tone_data['score']
                images[0]['height'] = 100 * tone_data['score']
            elif(tone_data['tone_id'] == 'disgust'):
                images[1]['width'] = 100 * tone_data['score']
                images[1]['height'] = 100 * tone_data['score']
            elif(tone_data['tone_id'] == 'fear'):
                images[2]['width'] = 100 * tone_data['score']
                images[2]['height'] = 100 * tone_data['score']
            elif(tone_data['tone_id'] == 'joy'):
                images[3]['width'] = 100 * tone_data['score']
                images[3]['height'] = 100 * tone_data['score']
            elif(tone_data['tone_id'] == 'sadness'):
                images[4]['width'] = 100 * tone_data['score']
                images[4]['height'] = 100 * tone_data['score']
            
        return render_template('watson/watson.html', images=images, messages=messages)

    return render_template('watson/watson.html')
