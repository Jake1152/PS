def solution(today, terms, privacies):
    answer = []
    today_number_of_days = int(today[:4])*12*28 + int(today[5:7])*28 + int(today[8:10])
    terms_dict = {}
    for term in terms:
        term_type, expiration_period_by_month = term.split()
        terms_dict[term_type] = int(expiration_period_by_month)*28

    for idx, privacy in enumerate(privacies):
        agree_date, terms_type = privacy.split()
        agree_date_number_of_days = int(agree_date[:4])*12*28 + int(agree_date[5:7])*28 + int(agree_date[8:10]) + terms_dict[terms_type]
        if today_number_of_days >= agree_date_number_of_days:
            answer.append(idx + 1)    
    return answer


# today	terms	privacies	result
# "2022.05.19"	["A 6", "B 12", "C 3"]	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	[1, 3]
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# [1, 3]
print(f"{solution(today, terms, privacies)=}")