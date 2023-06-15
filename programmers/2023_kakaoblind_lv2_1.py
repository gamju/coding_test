import itertools
def solution(users, emoticons):
    def dot_amount(rate, list1, list2):
        return_amount = 0
        for i in range(list1.__len__()):
            if list1[i] >= rate:
                return_amount += (100 - list1[i])*list2[i]*0.01
        return return_amount
    sale_rate = [10,20,30,40]
    sale_rate_list = itertools.product(sale_rate, repeat = emoticons.__len__())
    max_membership_user = 0
    max_emoji_amount = 0
    emoji_list = []
    for sale_rate_idx in sale_rate_list:
        emoji_amount = 0
        membership_user = 0
        for rate, amount in users:
            sale_amount = dot_amount(rate, sale_rate_idx, emoticons)
            emoji_list.append(sale_amount)
            if sale_amount >= amount:
                membership_user += 1
            else:
                emoji_amount += sale_amount
            
        # print(sale_rate_idx, rate, membership_user, emoji_amount)
        # print(emoji_list)
        
        if membership_user > max_membership_user:
            max_membership_user = membership_user
            max_emoji_amount = emoji_amount
        if membership_user == max_membership_user and emoji_amount > max_emoji_amount:
            max_emoji_amount = emoji_amount
            
            
            
            
             
    
    
    answer = [max_membership_user, max_emoji_amount]
    return answer