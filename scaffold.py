print("BT에 체온, cough에 기침여부, LAD에 림프절종대여부, exudate에 삼출물여부, tonsil에 편도비대여부, age에 연령을 입력하시오.")
BT=input("BT에 체온을 입력하시오.",)
BT=float(BT)
cough=input()
"boolean형으로 typecasting하기"
LAD=input()
"boolean형으로 typecasting하기"
exudate=input()
"boolean형으로 typecasting하기"
tonsil=input()
"boolean형으로 typecasting하기"
age=input()
age=int(age)


centor=0 'centor변수 선언 및 초기값 0'
str output '최종 출력 결과물 str형으로 선언'

'이하 알고리즘 시작'
centor=if(BT>38,1,0)+if(cough==FALSE,1,0)+if(LAD==TRUE,1,0)+if(if(exudate==TRUE,TRUE,FALSE)&if(tonsill==TRUE,TRUE,FALSE),1,0)

if(age>=3&&age<=14) centor=centor+1
elif(age>44) centor=centor-1

if(centor>=3) if()

else output="Symptomatic Tx"

print(output)

if