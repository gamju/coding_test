def solution(today, terms, privacies):
    year, month, day = today.split(".")
    terms_dict = {}
    for term_idx in terms:
        term_type, term_range = term_idx.split(" ")
        
        terms_dict[term_type] = int(term_range)*30
    print(terms_dict)
    answer_list = []
    for idx, privacies_idx in enumerate(privacies):
        pri_date, pri_type = privacies_idx.split(" ")
        pri_year, pri_month, pri_day = pri_date.split(".")
        year_diff = int(year) - int(pri_year)
        month_diff = int(month) - int(pri_month)
        day_diff = int(day) - int(pri_day)
        year_diff_day = year_diff*360
        year_diff_month = month_diff*30
        
        diff = year_diff_day + year_diff_month + day_diff
        # print(year_diff_day, year_diff_month, day_diff, terms_dict[pri_type], diff, pri_type)
        if terms_dict[pri_type] <= diff:
            answer_list.append(idx + 1)
            
    print(answer_list)
        
    
    terms_dict
    answer = answer_list
    return answer