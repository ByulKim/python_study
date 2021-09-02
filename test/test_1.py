
import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r") #가져온 데이터

html = BeautifulSoup(raw.text, "html.parser") #html 형식으로 파싱한 데이터

clips = html.select("div.inner")
bottom_clips = html.select("div.cds")

text = " aaa "
text.strip()

for clip in clips:
    title = clip.select_one("dt.title")
    chn = clip.select_one("dd.chn")
    hit = clip.select_one("span.hit")
    like = clip.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())

for b_clip in bottom_clips:
    title = b_clip.select_one("dt.title")
    chn = b_clip.select_one("dd.chn")
    hit = b_clip.select_one("span.hit")
    like = b_clip.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())


