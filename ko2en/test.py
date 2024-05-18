
import re


sent = '안녕하세요! 저는 한국인입니다. I am a Korean.'

sent = re.sub(r"[^a-zA-Z!.?ㄱ-ㅎ가-힣]+", r" ", sent)

print(sent)
