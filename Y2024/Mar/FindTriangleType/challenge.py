def find_triangle_type(leg1, leg2, hypo):
    msg = "This triangle is a {} triangle"
    ans = (leg1 ** 2 + leg2 ** 2) ** 0.5
    t_type = "Right"
    match ans:
        case x if x < hypo:
            t_type = "Obtuse"
        case x if x > hypo:
            t_type = "Acute"
    return msg.format(t_type)
