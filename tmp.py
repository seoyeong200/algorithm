str = """
## 3장. 함수

- Better way 19 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹하지 말라 134
- Better way 20 None을 반환하기보다는 예외를 발생시켜라 138
- Better way 21 변수 영역과 클로저의 상호작용 방식을 이해하라 142
- Better way 22 변수 위치 인자를 사용해 시각적인 잡음을 줄여라 147
- Better way 23 키워드 인자로 선택적인 기능을 제공하라 151
- Better way 24 None과 독스트링을 사용해 동적인 디폴트 인자를 지정하라 157
- Better way 25 위치로만 인자를 지정하게 하거나 키워드로만 인자를 지정하게 해서 함수 호출을 명확하게 만들라 162
- Better way 26 functools. wrap을 사용해 함수 데코레이터를 정의하라

## 4장. 컴프리헨션과 제너레이터

- Better way 27 map과 filter 대신 컴프리헨션을 사용하라 176
- Better way 28 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라 178
- Better way 29 대입식을 사용해 컴프리헨션 안에서 반복 작업을 피하라 181
- Better way 30 리스트를 반환하기보다는 제너레이터를 사용하라 186
- Better way 31 인자에 대해 이터레이션할 때는 방어적이 돼라 189
- Better way 32 긴 리스트 컴프리헨션보다는 제너레이터 식을 사용하라 197
- Better way 33 yield from을 사용해 여러 제너레이터를 합성하라 199
- Better way 34 send로 제너레이터에 데이터를 주입하지 말라 203
- Better way 35 제너레이터 안에서 throw로 상태를 변화시키지 말라 212
- Better way 36 이터레이터나 제너레이터를 다룰 때는 itertools를 사용하라 217

## 5장. 클래스와 인터페이스

- Better way 37 내장 타입을 여러 단계로 내포시키기보다는 클래스를 합성하라 228
- Better way 38 간단한 인터페이스의 경우 클래스 대신 함수를 받아라 236
- Better way 39 객체를 제너리하게 구성하려면 @classmethod를 통한 다형성을 활용하라 242
- Better way 40 super로 부모 클래스를 초기화하라 250
- Better way 41 기능을 합성할 때는 믹스인 클래스를 사용하라 256
- Better way 42 비공개 애트리뷰트보다는 공개 애트리뷰트를 사용하라 263
- Better way 43 커스텀 컨테이너 타입은 collections.abc를 상속하라 270

## 6장. 메타클래스와 애트리뷰트

- Better way 44세터와 게터 메서드 대신 평범한 애트리뷰트를 사용하라 278
- Better way 45 애트리뷰트를 리팩터링하는 대신 @property를 사용하라 284
- Better way 46 재사용 가능한 @property 메서드를 만들려면 디스크립터를 사용하라 290
- Better way 47 지연 계산 애트리뷰트가 필요하면 *getattr__*, *getattribute__*, _*setattr__*을 사용하라 298
- Better way 48 *init subclass*를 사용해 하위 클래스를 검증하라 306
- Better way 49 *init subelass__*를 사용해 클래스 확장을 등록하라 316
- Better way 50 *set_name* 으로 클래스 애트리뷰트를 표시하라 324
- Better way 51 합성 가능한 클래스 확장이 필요하면 메타클래스보다는 클래스 데코레이터를 사용하라

## 7장. 동시성과 병렬성

- Better way 52 자식 프로세스를 관리하기 위해 subprocess를 사용하라 340
- Better way 53 블로킹 1/O의 경우 스레드를 사용하고 병렬성을 피하라 347
- Better way 54 스레드에서 데이터 경합을 피하기 위해 Tock을 사용하라 354
- Better way 55 Queue를 사용해 스레드 사이의 작업을 조율하라 359
- Better way 56 언제 동시성이 필요할지 인식하는 방법을 알아두라 372
- Better way 57 요구에 따라 팬아웃을 진행하려면 새로운 스레드를 생성하지 말라 378
- Better way 58 동시성과 Queue를 사용하기 위해 코드를 어떻게 리팩터링해야 하는지 이해하라 384
- Better way 59 동시성을 위해 스레드가 필요한 경우에는 ThreadpoolExecutor를 사용하라 393
- Better way 60 1/0를 할 때는 코루틴을 사용해 동시성을 높여라 397
- Better way 61 스레드를 사용한 1/O를 어떻게 asyncio로 포팅할 수 있는지 알아두라 403
- Better way 62 asyncio로 쉽게 옮겨갈 수 있도록 스레드와 코루틴을 함께 사용하라 417
- Better way 63 응답성을 최대로 높이려면 asyncio 이벤트 루프를 블록하지 말라 427
- Better way 64 진정한 병렬성을 살리려면 concurrent.futures를 사용하라

## 8장. 강건성과 성능

- Better way 65 try/except/else/finally의 각 블록을 잘 활용하라 440
- Better way 66 재사용 가능한 try/finally 동작을 원한다면 contextlib과 with 문을 사용하라 447
- Better way 67 지역 시간에는 time보다는 datetime을 사용하라 452
- Better way 68 copyreg를 사용해 pickle을 더 신뢰성 있게 만들라 459
- Better way 69 정확도가 매우 중요한 경우에는 decimal을 사용하라 468
- Better way 70 최적화하기 전에 프로파일링을 하라 473
- Better way 71 생산자-소비자 큐로 deque를 사용하라 480
- Betterway 72 정렬된 시퀀스를 검색할 때는 bisect를 사용하라 491
- Better way 73 우선순위 큐로 heapg를 사용하는 방법을 알아두라 496
- Better way 74 bytes를 복사하지 않고 다루려면 memoryview와 bytearray를 사용하라

## 9장. 테스트와 디버깅

- Better way 75 디버깅 출력에는 repr 문자열을 사용하라 519
- Better way 76 TestCase 하위 클래스를 사용해 프로그램에서 연관된 행동 방식을 검증하라 524
- Better way 77 setUp, tearDown, setUpModule, tear DownModule & 사용해 각각의 테스트를 격리하라 533
- Better way 78 목을 사용해 의존 관계가 복잡한 코드를 테스트하라 537
- Better way 79 의존 관계를 캡슐화해 모킹과 테스트를 쉽게 만들라 549
- Better way 80 pdb를 사용해 대화형으로 디버깅하라 554
- Better way 81 프로그램이 메모리를 사용하는 방식과 메모리 누수를 이해하기 위해 tracemalloc을 사용하라

## 10장. 협업

- Better way 82 커뮤니티에서 만든 모듈을 어디서 찾을 수 있는지 알아두라 568
- Better way 83 가상 환경을 사용해 의존 관계를 격리하고 반복 생성할 수 있게 하라 569
- Better way 84 모든 함수, 클래스, 모듈에 독스트링을 작성하라 578
- Better way 85 패키지를 사용해 모듈을 체계화하고 안정적인 API를 제공하라 585
- Better way 86 배포 환경을 설정하기 위해 모듈 영역의 코드를 사용하라 592
- Better way 87 호출자를 API로부터 보호하기 위해 최상위 Exception을 정의하라 595
- Better way 88 순환 의존성을 깨는 방법을 알아두라 601
- Better way 89 리팩터링과 마이그레이션 방법을 알려주기 위해 warning을 사용하라 609
- Better way 90 typing과 정적 분석을 통해 버그를 없애라 619"""

l = str.split('\n')
changed = ''
print(l[34])
for line in l:
    strs = line.split(' ')
    if len(strs) < 5: 
        changed += line + '\n'
        continue
    tmpline = []
    for i, s in enumerate(strs):
        if i == 1 or i ==4 : tmpline.append('`')
        if i == len(strs)-1: 
            tmpline.append('[')
        tmpline.append(s)
    tmpline.append(']()')
    changed += ' '.join(tmpline) + '\n'
print(changed)



