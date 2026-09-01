# # 개인 지출 관리 프로그램

# ## 요구사항

# 1. 날짜, 카테고리, 내용, 금액을 입력한다.
# 2. 여러 지출 내역을 목록으로 확인한다.
# 3. 전체 지출과 카테고리별 지출을 계산한다.
# 4. CSV 파일로 저장하고 다시 불러온다.
# 5. 잘못된 입력으로 프로그램이 종료되지 않게 한다.

# ## 제외 범위

# - GUI
# - 데이터베이스
# - 웹 서버
# - 로그인
# - 복잡한 클래스 설계

import csv

file_path = "expenses.csv"

# 지출 추가
def add_expense(expenses):
    date = input("날짜를 입력하세요: ").strip()
    category = input("카테고리를 입력하세요: ").strip()
    description = input("사용 내용을 입력하세요: ").strip()

    # 빈칸 검사
    if not date or not category or not description:
        print("날짜, 카테고리, 내용은 비워 둘 수 없습니다.")
        return

    # 금액 문자 검사
    try:
        amount = int(input("금액을 입력하세요: "))
    except ValueError:
        print("금액은 숫자로 입력해 주세요.")
        return

    # 0원과 음수 검사
    if amount <= 0:
        print("금액은 0보다 큰 값으로 입력해 주세요.")
        return

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("지출이 추가되었습니다.")


# 지출 목록 출력
def show_expenses(expenses):
    if not expenses:
        print("등록된 지출이 없습니다.")
        return

    for expense in expenses:
        print(
            expense["date"],
            expense["category"],
            expense["description"],
            f'{expense["amount"]:,}원'
        )


# 전체 합계 계산
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"전체 지출: {total:,}원")


# 카테고리별 합계 계산
def calculate_by_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


# CSV 저장
def save_expenses(file_path, expenses):
    with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
        fieldnames = ["date", "category", "description", "amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

    print("CSV 파일에 저장되었습니다.")


# CSV 불러오기
def load_expenses(file_path):
    loaded_expenses = []

    try:
        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row["amount"] = int(row["amount"])
                except ValueError:
                    print("금액이 올바르지 않은 행은 건너뜁니다:", row)
                    continue

                loaded_expenses.append(row)

        print("CSV 파일을 불러왔습니다.")

    except FileNotFoundError:
        print("저장된 CSV 파일이 없습니다.")

    return loaded_expenses

# 프로그램이 시작될 때 기존 CSV 불러오기
expenses = load_expenses(file_path)

while True:
    print("\n개인 지출 관리 프로그램")
    print("1. 지출 추가")
    print("2. 지출 목록 보기")
    print("3. 전체·카테고리별 합계 보기")
    print("4. CSV 저장")
    print("5. CSV 불러오기")
    print("0. 종료")

    choice = input("메뉴 선택: ").strip()

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        show_expenses(expenses)

    elif choice == "3":
        calculate_total(expenses)
        print("카테고리별 지출:", calculate_by_category(expenses))

    elif choice == "4":
        save_expenses(file_path, expenses)

    elif choice == "5":
        expenses = load_expenses(file_path)

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("메뉴 번호를 다시 입력해 주세요.")