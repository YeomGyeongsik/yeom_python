data = input ('1주차, 2주차, 3주차, 4주차, 5주차, 6주차, 7주차, 8주차, 9주차, 10주차, 11주차, 12주차, 13주차, 14주차, 15주차 점수를 기입 해주세요.')

ME = int(input('중간 고사 성적을 기입해주세요.'))
FE = int(input('기말 고사 성적을 기입해주세요.'))

print(data.split())
g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13 ,g14, g15 = map(int,data.split())


sum_s=g1+g2+g3+g4+g5+g6+g7+g8+g9+g10+g11+g12+g13+g14+g15 
avg = sum_s/15     #평균=합계/15

avv = avg * 0.4    #비중 40%
MM = ME * 0.3     #비중 30%
FF = FE * 0.3     #비중 30%

score = avv + MM + FF
if 100 >= score >= 90:
    grade = "A"
elif 90 > score >= 80:
    grade = "B"
elif 80 > score >= 70:
    grade = "C"
elif 70 > score >= 60:
    grade = "D"
elif score < 60:
    grade = "F"





print(' %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | 평균값  %6.2f | 비중  %6.2f |'
      %(g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13 ,g14, g15, sum_s, avg,avv))


print('과제 평균(40%)' ,avv, '중간 평균(30%)' , MM, '중간 평균(30%)' , FF,  '총합 :',avv+MM+FF)

print("등급은" + grade + "입니다.")
