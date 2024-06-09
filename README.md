**경고! 이 프로그램 사용으로 발생하는 피해에 대해 책임지지 않습니다.**

**warning! We are not responsible for any damage resulting from the use of this program.**

# 프로그램 설명
하늘위키에서 jeongjo13이 사용하는 반달 자동 차단 봇 코드입니다. 하늘위키에서 사용되는 브랜치는 canary입니다.

imitated seed 엔진 위키에서의 반달을 자동 감지하고 차단합니다. 반달성 문서 삭제 및 휴지통화 등의 후속 조치도 자동으로 진행됩니다.

# 프로그램 기능
* 반달성 문서명을 가진 문서 생성 시 차단 및 삭제/휴지통화
* 반달성 내용이 문서에 추가될 경우 차단 및 자동 되돌리기
* 반달성 내용을 가진 문서가 생성되었을 경우 차단 및 삭제/휴지통화
* 반달성 주제를 가진 토론이 있으면 발제자 차단 및 토론 휴지통화

# 필요한 권한
어차피 예외 처리가 되어 있어 권한이 부족하면 해당 작업은 건너뛰기 때문에 권한 부족으로 오류가 발생할 일은 드뭅니다.

# 기본 사용 방법
코드 최상단에 wiki_username 변수, wiki_password 변수 정의하는 곳에 자신의 아이디와 비번 넣으시고 나서 main.py 실행하시면 됩니다.

# 추가 사용 방법
* 반달성 키워드 추가를 하고 싶으시면 코드 중간에 vandalism 리스트에 키워드 추가하시면 됩니다.
* 예외 처리되는 사용자를 수정하시려면 blocked 리스트에 사용자명을 추가하시면 됩니다.

# 주의사항
imitated seed 자체 기능으로 상단 공지 추가 시 이 프로그램은 제대로 동작하지 않습니다.

# 라이선스
CC BY-NC-ND 2.0 KR로 배포됩니다.

# 브랜치별 설명
* stable: 가장 안정적인 브랜치입니다. 오류가 없다고 판단된 기능들만 여기에 올라옵니다. 대신 기능 추가가 상당히 늦습니다. 올리기 전에 코드 전체에서 발생 가능한 오류를 검토하는 유일한 브랜치입니다. 그만큼 올리는 기준이 까다롭기 때문에 자주 업데이트되지 않습니다.
* beta: 어느 정도 안정적이면서 새 기능을 사용할 수 있는 브랜치입니다. 다만 완전히 안정적이라고 안심할 수 있는 수준은 아닙니다. 새 기능이 canary에 출시되면, 약 8~24시간 후 여기에 올라옵니다. 일반적으로 beta 브랜치는 수정된 부분과 이와 연관된 부분에서 오류가 발생할 수 있는 가능성을 검토했으며 몇 시간 동안 아무 문제 없이 프로그램이 동작한 경우에만 올라옵니다.
* dev: 이 브랜치는 안정적이지 못하지만, 새 기능이 canary에 올라왔을 때, 수정된 부분와 이와 연관된 부분에서 오류가 발생할 수 있는 가능성을 검토했으며 수정된 부분에 대한 기능이 정상 작동하고 while True 부분에서 문제 없이 5~15분 간 실행이 되는 경우 바로 dev로 merge됩니다. 그만큼 canary와 같이 가는 브랜치라서 **불안정하므로 사용하지 말 것을 권장합니다.**
* canary: 이 브랜치는 매우 불안정하며, 개발이 완료되었고 수정된 부분에 대한 기능이 1회 정상 작동하기만 하면 바로 코드가 올라옵니다. 하늘위키에서 사용하는 봇은 이 브랜치의 코드를 사용합니다. **4개 브랜치 중 가장 불안정한 브랜치이며, 사용하지 말 것을 매우 권장합니다.**
