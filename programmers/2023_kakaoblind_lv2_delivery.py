def solution(cap, n, deliveries, pickups):
    distance = 0
    
    deliver_sum = 0
    deliveriey_distance = []
    pickups_distance = []
    for i in range(deliveries.__len__()):
        if deliveries[i] != 0:
            deliveriey_distance.append(i)
            deliver_sum += deliveries[i]
    for i in range(pickups.__len__()):
        if pickups[i] != 0:
            pickups_distance.append(i)
    
    print(deliveries.__len__(), pickups.__len__(), deliver_sum)
    while(deliveriey_distance or pickups_distance):
        # deliveries.pop()
        
        cur_cap = min(cap, deliver_sum)
        try:
            delivery_dist = deliveriey_distance[-1] + 1
        except:
            delivery_dist = 0
        
        try:
            pickups_dist = pickups_distance[-1] + 1
        except:
            pickups_dist = 0
            
        cur_distance = max(delivery_dist, pickups_dist)
        distance += cur_distance*2
        while(cur_cap and deliveriey_distance):
            if cur_cap >= deliveries[deliveriey_distance[-1]]:
                deliver_sum = deliver_sum - deliveries[deliveriey_distance[-1]]
                cur_cap = cur_cap - deliveries[deliveriey_distance[-1]]
                deliveriey_distance.pop()
            else:
                deliver_sum = deliver_sum - cur_cap
                deliveries[deliveriey_distance[-1]] = deliveries[deliveriey_distance[-1]] - cur_cap
                cur_cap = 0
        
        while((cur_cap != cap) and pickups_distance):
            if cur_cap + pickups[pickups_distance[-1]] <= cap:
                cur_cap = cur_cap + pickups[pickups_distance[-1]]
                pickups_distance.pop()
            else:
                pickups[pickups_distance[-1]] = pickups[pickups_distance[-1]] - (cap - cur_cap)
                cur_cap = cap
        
        # while(deliveries[-1] == 0):
        #     deliveries.pop()
        # while(pickups[-1] == 0):
        #     pickups.pop()
        
    answer = distance
    return answer