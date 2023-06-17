def solution(cap, n, deliveries, pickups):
    distance = 0
    while(deliveries.__len__() or pickups.__len__()):
        deliver_sum = 0
        for i in deliveries:
            deliver_sum += i
        cur_cap = min(cap, deliver_sum)
        deliver_distance = deliveries.__len__()
        pickup_distance = pickups.__len__()
        cur_distance = max(deliver_distance, pickup_distance)
        distance += cur_distance*2
        for deliveries_idx in range(deliveries.__len__())[::-1]:
            if cur_cap > deliveries[deliveries_idx]:
                cur_cap = cur_cap - deliveries[deliveries_idx]
                deliveries[deliveries_idx] = 0
            else:
                deliveries[deliveries_idx] = deliveries[deliveries_idx] - cur_cap
                cur_cap = 0
                break
        
        for pickup_idx in range(pickups.__len__())[::-1]:
            if cur_cap + pickups[pickup_idx] < cap:
                cur_cap = cur_cap + pickups[pickup_idx] 
                pickups[pickup_idx] = 0
            else:
                pickups[pickup_idx] = pickups[pickup_idx] - (cap - cur_cap)
                break
        # print(distance, deliver_distance, pickup_distance)
            
        while(deliver_distance > 0):
            deliver_distance -= 1
            if deliveries[-1] == 0:
                deliveries = deliveries[:-1]
        while(pickup_distance > 0):
            pickup_distance -= 1
            if pickups[-1] == 0:
                pickups = pickups[:-1]
                # pickups.pop()
        
            
        
    answer = distance
    return answer