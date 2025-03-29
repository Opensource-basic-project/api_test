import openai

openai.api_key = 'openai api키' 

bill_content = """
상속세 및 증여세법 일부개정법률안(박충권의원 등 13인)
현행법은 상속세에 누진세율을 적용하여 높은 상속세율을 적용하는 대신 각종 공제제도를 통하여 상속세를 감면하여 주고 있음.
현재 우리나라의 상속세 최고 세율은 50%로 OECD 회원국 중 두 번째로 높아 다른 나라에 비해 상속세율이 지나치게 높다는 비판이 제기되고 있음.
또한, 인적공제 제도 중 배우자에 대하여는 최소 5억원에서 최대 30억원을 한도로 공제하여 주는 배우자 상속공제 제도를 시행하고 있으나, 배우자에 대한 상속세 부과는 부부가 함께 일구어낸 자산이라는 점과 부의 대물림이라는 수직이동이 아니라 수평이동이라는 점을 감안할 때 배우자에 대한 상속세 부과를 폐지하여야 한다는 의견이 있음.
이에 배우자가 상속받는 재산에 대하여는 상속세를 폐지하고, 상속세 최고 세율도 50%에서 40%으로 10%p 하향 조정하려는 것임(안 제19조 및 제26조).
"""

def classify_bill(bill_text):
    prompt = f"법안 내용: {bill_text}\n이 법안의 카테고리는 무엇인가요?"

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo", 
            prompt=prompt,
            max_tokens=5,  
            temperature=0  
        )
        classification = response['choices'][0]['text'].strip() 
        return classification
    except openai.error.RateLimitError:
        print("API 호출 한도를 초과했습니다. 잠시 후 다시 시도합니다.")
        return None  

classification = classify_bill(bill_content)
if classification:
    print("법안 분류 결과:", classification)
else:
    print("분류할 수 없습니다.")
