# 문제 32 : 문자열 만들기
# 취업 준비생인 혜림이는 자기 소개서를 쓰고 있다. 열심히 자기소개서를 작성하는 도중 혜림이는 자기가 지금까지
# 단어를 얼마나 적었는지 궁금하게 된다.
# 혜림이를 위해 문자열을 입력받으면 단어의 갯수를 출력하는 프로그램을 작성해 주세요.

"""
입출력

입력 : 안녕하세요. 저는 제주대학교 컴퓨터공학전공 혜림입니다.
출력 : 5
"""

n = input()
l = list(n.strip().split())
print(len(l))


"""
lstrip : 문자열에 왼쪽 공백이나 인자가된 문자열의 모든 조합을 제거
' apple'.lstrip()  # 인자가 없을 경우 왼쪽 공백 제거
----------------------
'apple'

'apple'.lstrip('ap')  # 왼쪽으로 a, p의 문자열의 모든 조합을 제거
----------------------
'le'


rstrip : 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
'apple '.rstrip()  # 인자가 없을 경우 오른쪽 공백 제거
----------------------
'apple'

'apple'.rstrip('lep')  # 오른쪽으로 l, e, p의 문자열의 모든 조합을 제거
----------------------
'a'


strip : 양쪽 문자열에 공백이나 인자가된 문자열의 모든 조합을 제거
' apple '.strip()  # 인자가 없을 경우 왼쪽 공백 제거
----------------------
'apple'

'apple'.strip('ae')  # 양쪽끝에 a, e의 문자열의 모든 조합을 제거
----------------------
'ppl'
"""
