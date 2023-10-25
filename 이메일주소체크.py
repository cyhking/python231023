# 이메일주소체크.py

import re

# 이메일 주소를 체크하기 위한 정규 표현식 패턴을 정의합니다.
# 이 패턴은 "@" 다음에 문자가 와야 하며, ".com"과 같이 "." 다음에 문자가 있어야 합니다.
# r(raw string notation)
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[a-zA-Z]*$'

# 다섯 살 아이들을 위한 샘플 이메일 주소 목록을 만듭니다.
sample_emails = [
    'john.doe@example.com',         # 유효한 이메일 주소
    'jane_doe123@email.co.uk',      # 유효한 이메일 주소
    'user@domain.com',             # 유효한 이메일 주소
    'admin@sub.domain.co',          # 유효한 이메일 주소
    'support@my-website.net',      # 유효한 이메일 주소
    'user@example',                # 유효하지 않은 이메일 주소 - "@" 다음에 문자가 없음
    'invalid.email@.com',          # 유효하지 않은 이메일 주소 - "." 다음에 문자가 없음
    'user@.domain.com',            # 유효하지 않은 이메일 주소 - "@" 다음에 문자가 없음
    'user@domain.',                # 유효하지 않은 이메일 주소 - "." 다음에 문자가 없음
    'no_at_symbol.com'             # 유효하지 않은 이메일 주소 - "@" 기호가 없음
]

# 각 샘플 이메일 주소를 패턴과 비교하여 유효성을 확인합니다.
for email in sample_emails:
    if re.search(email_pattern, email):
        print(f'{email} 는 유효한 이메일 주소입니다')
    else:
        print(f'{email} 는 유효한 이메일 주소가 아닙니다')
