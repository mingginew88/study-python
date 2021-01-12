
## 첫글자 대문자로 수정
def capitalize_every_word(s):
    return s.title()

# print(capitalize_every_word('hello test python'))


## 주어진 횟수만큼 문자열 출력
def n_times_string(s, n):
    return s * n

# print(n_times_string('py', 3))


## 문자열 역순
def reverse_string(s):
    return s[::-1]

# print(reverse_string('python'))


## 여러줄의 문자열을 리스트 구성
def split_lines(s):
    return s.split('\n')

print(split_lines('This\nis\na \nmultiline\nstring.\n'))