class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)


class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        self.name = name
        self.posts = []
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """

    def add_post(self, date, content):
        new_post = Post(date, content)
        self.posts.append(new_post)
    # 새로운 게시글 추가

    def show_all_posts(self):
        for post in self.posts:
            print(post)

    # 블로그 유저의 모든 게시글 출력

    def __str__(self):
        return "안녕하세요 {}입니다.\n".format(self.name)

# 간단한 인사와 이름을 문자열로 리턴


# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
미안하다 이거 보여주려고 어그로끌었다.. 
나루토 사스케 싸움수준 ㄹㅇ실화냐? 
진짜 세계관최강자들의 싸움이다.. 
그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()