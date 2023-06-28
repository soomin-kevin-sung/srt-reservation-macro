from webController import webControllerOption
from webController import webController


def main():
    op = webControllerOption('20230628', '140000', '수서', '부산')
    wc = webController(op)

    # 로그인
    if not wc.login('ssm0725@gmail.com', 'soomin0725@'):
        print("로그인 실패")
        return

    # 매크로 실행
    wc.run_macro()


if __name__ == '__main__':
    main()
