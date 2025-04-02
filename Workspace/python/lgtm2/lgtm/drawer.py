import os
from PIL import Image, ImageDraw, ImageFont

# 이미지 전체 크기 대비 메시지 표시 가능한 영역 비율
MAX_RATIO = 0.8

# 폰트 관련 상수
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24

# 폰트 저장 위치는 실행 환경에 따라 달라짐
FONT_NAME = os.path.dirname(__file__) + '/data/ipaexg.ttf'
FONT_COLOR_WHITE = (255, 255, 255, 0)

# 아웃풋 관련 상수
OUTPUT_NAME = "output.png"
OUTPUT_FORMAT = "PNG"


def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)
    # 메시지를 그릴 수 있는 영역 크기
    # 튜플 엘리먼트 별로 계산함
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    # 1 포인트씩 줄이면서 최적 폰트 크기를 구함
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)
        # 그리기에 필요한 크기
        text_width, text_height = draw.textsize(message, font=font)
        w = message_area_width - text_width
        h = message_area_height - text_height

        # 폭, 높이 모두가 영역 안에 들어가는 값을 선택
        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2, (image_height - text_height) / 2)
            # 메시지 표시
            draw.text(position, message, fill=FONT_COLOR_WHITE, font=font)
            break

    # 이미지 저장
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
