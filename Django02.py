## Survey ##


# models.py
from django.db import models

class Survey( models.Model ) :                              # survey_survey
    Survey_idx = models.AutoField( primary_key=True )       # 설문문항번호
    question = models.TextField( null=False )               # 설문문항
    ans1 = models.TextField( null=False )                   # 1번 보기
    ans2 = models.TextField( null=False )                   # 2번 보기
    ans3 = models.TextField( null=False )                   # 3번 보기
    ans4 = models.TextField( null=False )                   # 4번 보기
    status = models.CharField( max_length=1, default="y" )  # 진행상태 y진행중

class Answer( models.Model ) :                              # survey_answer
    answer_idx = models.AutoField( primary_key=True )       # 응답 고유번호
    survey_idx = models.IntegerField( null= False )         # 설문 번호
    num = models.IntegerField( null=False )                 # 응답 번호


# admin.py
from django.contrib import admin
from survey.models import Survey

class SurveyAdmin( admin.ModelAdmin ):
    list_display = ( "question", "ans1", "ans2", "ans3", "ans4", "status" )
admin.site.register( Survey, SurveyAdmin )


# urls.py
from django.urls.conf import re_path, path
from survey import views

urlpatterns = [
    re_path( r"^$", views.main, name="main" ),
    # http://localhost:8000/survey/
    re_path( r"^save$", views.save, name="save" ),
    # http://localhost:8000/survey/save
    re_path( r"^result$", views.result, name="result" )
    # http://localhost:8000/survey/result
]


# views.py
from django.shortcuts import render
from survey.models import Survey, Answer
from django.template import loader
from django.http.response import HttpResponse
from djandgo.views.decorators.csrf import csrf_exempt

def main( request ):
    Survey = Survey.objects.filter( status="y" ).order_by( "-survey_idx" )[0]
    # select * from survey_survey where status='y' order by survey_idx desc
    template = loader.get_template( "main.html" )
    print( "main" )
    return HttpResponse( template.render( { "survey" : survey }, request ) )

@csrf_exempt
def save( request ):
    survey_idx = request.POST["survey_idx"]
    num = request.POST["num"]
    dto = Answer( survey_idx=survey_idx, num=num )
    dto.save()
    # insert into survey_answer ( survey_idx, num ) values( survey_idx, num )
    template = loader.get_template( "save.html" )
    return HttpResponse( template.render( {}, request ) )

def result( request ):
    survey_idx = request.GET["survey_idx"]
    surveylist = Survey.objects.raw(
        """
        select survey_idx, num, count( num ) sum_cum, round(
            ( select count(*) from survey_answer where survey_idx=sa.survey_idx and num=sa.num ) * 100
            / ( select count(*) from survey_answer where survey_idx=sa.survey_idx )
        , 1) rate
        from survey_answer sa
        where survey_idx=%s
        group by survey_idx, num
        """, survey_idx )
    ans = Survey.objects.get( survey_idx=survey_idx )
    answer = [ ans.ans1, ans.ans2, ans.ans3, ans.ans4 ]
    surveylist = zip( surveylist, answer )
    context = {
        "question" : ans.question,
        "surveylist" : surveylist
        }
    template = loader.get_template( "result.html" )
    return HttpResponse( template.render( context, request ) )


# templates

# main.html
# <!DOCTYPE html>
# 	<html>
# 	<head>
# 		<meta charset="UTF-8">
# 		<title> Survey </title>
# 	</head>
# 	<body>
# 		<h2> 설문조사 </h2>
# 		<br><br>		
# 		<!-- localhost:8000/survey/save -->
# 		<form method="post" action="save">	
# 			{% csrf_token %}
# 			<input type="hidden" name="survey_idx" value="{{survey.survey_idx}}">
# 			<table border="1">
# 				<tr>
# 					<th colspan="2">
# 						{{ survey.question }}
# 					</th>
# 				</tr>
# 				<tr>
# 					<th> 항목 </th>
# 					<td>
# 						<input type="radio" name="num" value="1"> {{ survey.ans1 }} <br>
# 						<input type="radio" name="num" value="2"> {{ survey.ans2 }} <br>
# 						<input type="radio" name="num" value="3"> {{ survey.ans3 }} <br>
# 						<input type="radio" name="num" value="4"> {{ survey.ans4 }} <br>
# 					</td>
# 				</tr>
# 				<tr>
# 					<th colspan="2">
# 						<input type="submit" value="선택">
# 						<input type="button" value="결과확인"
# 							onclick="location='result?survey_idx={{survey.survey_idx}}'">
# 					</th>
# 				</tr>
# 			</table>			
# 		</form>
# 	</body>
# </html>

# result.html
# <!DOCTYPE html>
# <html>
# 	<head>
# 		<meta charset="UTF-8">
# 		<title> Survey </title>
# 	</head>
# 	<body>
# 		<h2> 결과확인 </h2>
# 		<br><br>
# 		<h3> {{ question }} </h3>
# 		<br>
# 		<table border="1">
# 			<tr>
# 				<th> 항목 </th>
# 				<th> 응답수 </th>
# 				<th> 응답률 </th>
# 			</tr>
# 			{% for row, ans in surveylist %}
# 				<tr align="center">
# 					<td> {{ ans }} </td>
# 					<td> {{ row.sum_cum }} </td>
# 					<td> {{ row.rate }} </td>
# 				</tr>
# 			{% endfor %}
# 		</table>
# 	</body>
# </html>

# save.html
# <!DOCTYPE html>
# <html>
# 	<head>
# 		<meta charset="UTF-8">
# 		<title> Survey </title>
# 	</head>
# 	<body>
# 		<h2> 설문완료 </h2>
# 		<br><br>
# 		설문조사를 완료했습니다. <br>
# 		<br>
# 		<a href="http://localhost:8000/survey"> 메인 </a>	
# 	</body>
# </html>