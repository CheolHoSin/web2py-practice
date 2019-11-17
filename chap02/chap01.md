# 데이터 타입

## 숫자

숫자(int, float, ...)를 표현. +, -, /, * 등 연산자를 사용.

## 문자열

문자열을 표현. `''`, `""` 을 사용

### Escape

`\` 로 문자열 escape

**ex**
```python
print("Hell'o' \"W\"orld")
```

### Newline 을 표현하는 세가지 방법

1. 줄마다 print
   ```python
   print("Hello")
   print("World")
   ```
1. `\n` 사용
   ```python
   print("Hello\nWorld")
   ```
1. `Doc String` 사용
   ```python
   print('''Hello
   World''')
   ```

### length

`len()` 는 문자열 길이를 리턴

**ex**
```python
print(len("Hello World"))
```

### Indexing and Slicing

문자열 인덱싱은 [] 로 가능하며, `:` 을 사용하면 슬라이싱 가능

**indexing**
```python
a = "Hello world"
print(a[1])
```

**Slicing**
```python
a = "Hello world"
print(a[2:5])
```

### Repeating

`*` 로 연산하면 문자열을 반복

**ex**
```python
print("Hello World" * 2)
```

### Formatting

- Positioning Formatting
  ```python
  print("My name is {}. I'm {} years old".format('Joker', 31))
  ```
- Named Placeholder
  ```python
  print("My name is {name}. I'm {age:d} years old".format(name='Joker' , age=31))
  ```

# CGI

**CGI(Common Gateway Interface)**

Browser <==> HTTPD <==> CGI Application

- Browser: Client
- HTTPD: HTTP 프로토콜 상에서 Client 요청을 받아 응답해주는 서버
- CGI Application: Server Side Script 을 실행시켜 html 등과 같은 문서를 생성