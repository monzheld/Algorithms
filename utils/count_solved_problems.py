from collections import defaultdict
import os
import re


def count_solved_problems():
    """사이트별 해결한 문제 개수 카운트

    코딩테스트 사이트별로 해결한 문제의 개수를 세는 함수입니다.

    name_list (list): 디렉토리명이자 코딩테스트 사이트명
    code_dict (collections.defaultdict): 사이트별로 해결한 문제의 ipynb 파일명 (default: list)
    code_cnt_info (collections.defaultdict): 사이트별로 해결한 문제의 개수 (default: 0)
    total_code_num (int): 해결한 문제의 총개수 

    Returns:
        total_code_num (int): 해결한 문제의 총개수 
        code_cnt_info (collections.defaultdict): 사이트별로 해결한 문제의 개수 (default: 0)
    """    
    r = [re.findall(r"^[A-Z]+", dirctory) for dirctory in os.listdir("./")]
    name_list = [dir_name[0].replace("[", "").replace("]", "") for dir_name in r if len(dir_name) > 0]
    name_list.remove("README")

    solved_problem_list = []
    code_dict = defaultdict(list) 
    code_cnt_info = defaultdict(lambda:0) 

    for name in name_list:
        # 사이트별 전체 ipynb 파일 리스트
        file_list = [file for file in os.listdir(f"./{name}") if file.endswith(".ipynb")] 
        # 중복된 파일 제거 
        code_list = [] # 중복 제거된 ipynb 파일 리스트
        for file in file_list:
            if file not in code_list:
                code_list.append(file)
        code_dict[name] = code_list 
        code_cnt_info[name] = len(code_list) 
        solved_problem_list += code_list 

    total_code_num = len(solved_problem_list) 

    return total_code_num, code_cnt_info


def make_count_info(total_code_num, code_cnt_info):
    """사이트별 해결한 문제 개수 정보 작성

    코딩테스트 사이트별로 해결한 문제의 개수 정보를 작성하는 함수입니다.

    Arguments:
        total_code_num (int): 해결한 문제의 총개수 
        code_cnt_info (collections.defaultdict): 사이트별로 해결한 문제의 개수 (default: 0)

    Returns:
        count_info (str): 사이트별 해결한 문제 개수 정보 작성
    """   
    count_info = f"### 해결한 총 문제 수 : {total_code_num}개\n"

    for k,v in code_cnt_info.items():
        temp = f"- {k} - {v}개\n"
        count_info += temp
    
    return count_info


def make_read_me(count_info):
    """README.md 파일 작성

    README.md 파일을 작성하는 함수입니다.

    Arguments:
        count_info (str): 사이트별 해결한 문제 개수 정보 작성

    Returns:
        README.md 파일에 작성될 출력문
    """   

    return f"""# Algorithms
파이썬 알고리즘 문제 풀이
### Since 2022.12.13 ~
{count_info}
[알고리즘 문제 풀이 블로그](https://monzheld.tistory.com/category/%E2%8C%A8%EF%B8%8F%20Algorithms)
#### 모든 문제는 Python3 로 해결했습니다.
"""


def update_readme_md():
    """README.md 파일 업데이트

    README.md 파일을 업데이트하는 함수입니다.

    Returns:
        README.md 파일에 작성될 출력문
    """   
    total_code_num, code_cnt_info = count_solved_problems()

    count_info = make_count_info(total_code_num=total_code_num, code_cnt_info=code_cnt_info)

    readme = make_read_me(count_info=count_info)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)