from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import Select
from datetime import datetime
import random

now = datetime.now()

def block(document_, blocking, rev) :
    if blocking not in blocked :
        driver.get('https://haneul.wiki/aclgroup?group=차단된 사용자')
        option1 = driver.find_element(By.XPATH,'//*[@id="modeSelect"]') #ACLGroup 창의 아이피, 사용자 이름 여부 선택란
        dropdown1 = Select(option1)
        dropdown1.select_by_value("username")
        option2 = driver.find_element(By.XPATH,'//*[@id="usernameInput"]') #ACLGroup 창의 사용자 이름 입력란
        option2.send_keys(blocking)
        option3 = driver.find_element(By.XPATH,'//*[@id="noteInput"]') #ACLGroup 창의 메모 입력란
        option3.send_keys("%s r%d 긴급차단 | 자동 차단 (잘못된 경우 \'하늘위키:차단 소명 게시판\'에 토론 발제 바랍니다. 오작동 시 오작동 시 \'사용자:jeongjo13/긴급 정지\'에 토론 발제 바랍니다.)" % (block_memo(document_), rev))
        option4 = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div[3]/form[1]/div[3]/select') #ACLGroup 창의 아이피, 사용자 이름 여부 선택란
        dropdown2 = Select(option4)
        dropdown2.select_by_value("0")
        time.sleep(0.05)
        add_block = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/form[1]/div[4]/button') #ACLGroup 창의 추가 버튼
        add_block.click()
        blocked.append(blocking)

def get_doc_text() :
    doc_text_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/textarea')
    doc_text = doc_text_field.text
    return doc_text

def block_memo(name) : #차단 사유에 문서명을 문서:~~~, 하늘위키:~~~과 같이 들어갈 것을 지정해줌
    if "하늘위키" not in name :
        if "틀" not in name :
            if "분류" not in name :
                if "파일" not in name :
                    if "휴지통" not in name :
                        if "사용자" not in name :
                            name = "문서:" + name
    return(name)
def revert(doc, rev) :
    rev = rev - 1
    driver.get(f"https://haneul.wiki/revert/{doc}?rev={rev:d}")
    try :
        time.sleep(0.5)
        revert_reason = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/form/input')
        revert_reason.send_keys("반달 복구: 반달을 멈추시고 하늘위키에 정상적으로 기여해 주시기 바랍니다. | 자동 되돌리기 (잘못된 경우 \'하늘위키:문의 게시판\'에 토론 발제 바랍니다. 오작동 시 \'사용자:jeongjo13/긴급 정지\'에 토론 발제 바랍니다.")
        revert_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/form/div/button')
        revert_button.click()
    except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"Error in revert function: {e}")


def trash(doc) : #반달성 문서 휴지통화시키는 함수
    if "사용자" not in doc :
        driver.get('https://haneul.wiki/delete/%s' % doc)
        try :
            delete_reason = driver.find_element(By.XPATH,'//*[@id="logInput"]') # 문서 삭제 시 편집 요약
            delete_reason.send_keys("반달 복구: 반달을 멈추시고 하늘위키에 정상적으로 기여해 주시기 바랍니다. | 자동 휴지통화 (잘못된 경우 \'하늘위키:문의 게시판\'에 토론 발제 바랍니다. 오작동 시 \'사용자:jeongjo13/긴급 정지\'에 토론 발제 바랍니다.)")
            delete_check = driver.find_element(By.XPATH,'//*[@id="agreeCheckbox"]')
            delete_check.click()
            delete_button = driver.find_element(By.XPATH, '//*[@id="submitBtn"]')
            delete_button.click()
            driver.get('https://haneul.wiki/move/%s' % doc)
            move_document = driver.find_element(By.XPATH,'//*[@id="titleInput"]') #문서 이동 시 사용할 휴지통 문서명
            move_document.send_keys('휴지통:%s' % trashname())
            move_document_memo = driver.find_element(By.XPATH,'//*[@id="logInput"]')
            move_document_memo.send_keys("반달 복구: 반달을 멈추시고 하늘위키에 정상적으로 기여해 주시기 바랍니다. | 자동 휴지통화 (잘못된 경우 \'하늘위키:문의 게시판\'에 토론 발제 바랍니다. 오작동 시 \'사용자:jeongjo13/긴급 정지\'에 토론 발제 바랍니다.)")
            move_button = driver.find_element(By.XPATH,'//*[@id="moveForm"]/div[4]/button')
            move_button.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Error in trash function: {e}")

def trashname() :
    return("%s%s%s%s%s%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second))
# 차단하지 않을 사용자(또는 이미 차단한 사용자(중복 차단 방지)) 리스트
blocked = ["Vanilla","jeongjo13","Cordelia","soupcake27"]

# Chrome WebDriver 초기화
driver = webdriver.Chrome()

# 크롬 드라이버에 URL 주소 넣고 실행
driver.get('https://haneul.wiki/member/login?redirect=%2Faclgroup')
time.sleep(2.5)  # 페이지가 완전히 로딩되도록 2.5초 동안 기다림

# 아이디 입력
username = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/form/div[1]/input')
username.send_keys('')
time.sleep(0.5)

# 비밀번호 입력
password = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/form/div[2]/input')
password.send_keys('')
time.sleep(0.5)

# 로그인 버튼 클릭
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/form/button')
login_button.click()
time.sleep(1)

document_names = []
while True :
    # RecentChanges 페이지로 이동
    driver.get('https://haneul.wiki/RecentChanges?logtype=create')
    time.sleep(0.4)

    # 페이지 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = bs(page_source, 'html.parser')

    # 최근 변경된 문서 목록 추출
    links = soup.find_all('a', href=True)

    # 문서명 추출
    for link in links:
        href = link.get('href')
        if href.startswith('/w/') and link.text.strip():
            document_names.append(link.text.strip())

    document_names.remove("내 사용자 문서")
    print(document_names)

    edited_document = []
    edited_user = []

    vandalism = ["사퇴하세요", "뒤져라", "정좆", "jeongjot","Fuck_","사퇴 기원","sibal_","No_","FUCK_","satoehaseyo","must resign","해웃돈","혁명본부 만세","wikiRevolution","wikirevolution"]

    for index, value in enumerate(document_names):
        if index % 2 == 0:
            edited_document.append(value)
        else:
            edited_user.append(value)

    print(edited_document)
    print(edited_user)

    for i,j in zip(edited_document,edited_user) :
        if any(v in i for v in vandalism):
            block(i, j, 1)
            trash(i)

    #문서 변경사항 검토
    # RecentChanges 페이지로 이동
    driver.get('https://haneul.wiki/RecentChanges')
    time.sleep(0.4)

    # 페이지 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup을 사용하여 페이지 소스를 파싱
    soup = bs(page_source, 'html.parser')

    # 최근 변경된 문서 목록 추출
    links = soup.find_all('a', href=True)

    # 문서명 추출
    document_names.clear()
    for link in links:
        href = link.get('href')
        if href.startswith('/w/') and link.text.strip():
            document_names.append(link.text.strip())
    num = 0
    for i,j in zip(edited_document,edited_user) :
        driver.get('https://haneul.wiki/history/%s' % i)
        time.sleep(0.5)
        version = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/ul/li[1]/strong[1]')
        lastest_version = version.text  #해당 문서의 최신 리비전
        lastest_version = lastest_version[1:]
        lastest_version = int(lastest_version)
        if lastest_version > 1 :
            driver.get("https://haneul.wiki/raw/%s?rev=%d" % (i, lastest_version))
            time.sleep(0.5)
            lastest_doc = get_doc_text()
            driver.get("https://haneul.wiki/raw/%s?rev=%d" % (i, lastest_version-1))
            time.sleep(0.5)
            prev_doc = get_doc_text()
            for k in vandalism :
                if k in lastest_doc :
                    if k not in prev_doc :
                        block(i, j, lastest_version)
                        revert(i, lastest_version)
                        break
        num += 1;
        if num >= 11 :
            num = 0
            break
        time.sleep(0.1)



    #사용자 토론을 통한 긴급 정지 여부 확인
    driver.get('https://haneul.wiki/discuss/%EC%82%AC%EC%9A%A9%EC%9E%90%3Ajeongjo13%2F%EA%B8%B4%EA%B8%89%20%EC%A0%95%EC%A7%80')
    try:
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[3]/div[4]/div/div')
        break
    except NoSuchElementException:
        time.sleep(0.05)
