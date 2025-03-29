import requests
import json

ASSEMBLY_API_KEY = "열린국회정보 api 키"  
ASSEMBLY_URL = f"https://open.assembly.go.kr/portal/openapi/TVBPMBILL11?Key={ASSEMBLY_API_KEY}&Type=json&pIndex=1&pSize=5"

def fetch_bills():
    response = requests.get(ASSEMBLY_URL)
    
    if response.status_code == 200:
        try:
            data = response.json() 
            
            print("응답 데이터:", json.dumps(data, indent=4, ensure_ascii=False))
            
            if "TVBPMBILL11" in data:
                bills = data["TVBPMBILL11"]
                if isinstance(bills, list) and len(bills) > 1:
                    row_data = bills[1].get("row", [])
                    if row_data:
                        return row_data
                    else:
                        print("법안 데이터가 포함되지 않은 'row' 키가 없습니다.")
                        return []
                else:
                    print("법안 데이터가 없습니다.")
                    return []
            else:
                print("'TVBPMBILL11' 키가 없습니다.")
                return []
        except json.JSONDecodeError:
            print("응답 데이터가 JSON 형식이 아닙니다. 응답 본문:", response.text)
            return []
    else:
        print("API 요청 실패:", response.status_code)
        return []

if __name__ == "__main__":
    print("법안 데이터를 가져오고 있습니다...")
    bills = fetch_bills()

    if bills:
        print("\n법안 분류 결과:")
        for bill in bills:
            print(f"법안: {bill.get('BILL_NAME', '제목 없음')}")
            print(f"제안자: {bill.get('PROPOSER', '제안자 없음')}")
            print(f"제안일: {bill.get('PROPOSE_DT', '제안일 없음')}")
            print(f"링크: {bill.get('LINK_URL', '링크 없음')}")
            print("-" * 50)
    else:
        print("가져올 법안 데이터가 없습니다.")
