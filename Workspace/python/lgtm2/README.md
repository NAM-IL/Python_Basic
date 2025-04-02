# lgtm

LGTM 이미지를 생성하는 `lgtm` 명령어입니다.
Python 3.8.1 기반으로 macOS, Windows, Ubuntu에서 동작합니다.

## 설치하기

```shell
$ pip install git+https://github.com/yeonsookim-wt/lgtm#egg=lgtm
```

## 사용법

* `lgtm` 명령어에 다음 중 하나를 KEYWORD로 전달하면, 그 KEYWORD를 기반으로 얻은 이미지에 'LGTM' 문자열을 표시합니다
    * 로컬 이미지 경로
    * 이미지 URL
    * 그 외 KEYWORD인 경우에는 https://loremflickr.com/ 에서 입력한 KEYWORD로 검색합니다.

```shell
# 다음은 https://loremflickr.com/ 에서 얻은 이미지를 이용해 output.png을 만듭니다.
$ lgtm book
```

* `--message` 또는 `-m` 옵셥을 이용해 이미지에 표시할 문자열을 변경할 수 있습니다.

```shell
$ lgtm dog -m dog
```

* 도움말 표시

```shell
$ lgtm --help
Usage: lgtm [OPTIONS] KEYWORD

  LGTM 이미지 생성 도구

Options:
  -m, --message TEXT  이미지에 표시할 문자열 [default: LGTM]
  --help              Show this message and exit.
```
