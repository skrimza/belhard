def bouncing_ball(h, bounce, window):
    i = 0
    h /= bounce
    if h >= window:
        i += 1
    return i
        
res = bouncing_ball(3, 0.6, 1)
print(res)