from service import api
from .views import (PhotoView, ArticleView, QuestionView)

api.add_resource(PhotoView, '/photo')
api.add_resource(ArticleView, '/article')
api.add_resource(QuestionView, '/question')
