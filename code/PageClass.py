class Page:  #클래스 정의
    # 생성자, 이니셜라이저
    def __init__(self, num, content):
        self.num = num # 페이지 번호
        self.content = content # 페이지 내용

    # 클래스 메서드
    def output(self):
        return f'{self.content}'
    
# 클래스 상속
class TitlePage(Page):
    # 메서드 오버라이드
    def output(self):
        # 베이스 클래스의 메서드는 자동으로 호출되지 않으므로
        # 명시적으로 호출함
        title = super().output()
        return title.upper()
    
    
if __name__ == "__main__":
    title = TitlePage(0, 'Python Practice Book')
    print(title.output())