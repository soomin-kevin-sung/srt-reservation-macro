from webController import webControllerOption
from webController import webController


def main():
    op = webControllerOption('20230627', '180000', '수서', '부산', True)
    wc = webController(op)

    if not wc.login('ssm0725@gmail.com', 'soomin0725@'):
        print("로그인 실패")

    wc.run_macro()


if __name__ == '__main__':
    main()
