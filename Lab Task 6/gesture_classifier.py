def count_fingers(landmarks):
    tip_ids = [4, 8, 12, 16, 20]
    dip_ids = [3, 6, 10, 14, 18]
    count = 0

    # Thumb
    if landmarks[tip_ids[0]].x > landmarks[dip_ids[0]].x:
        count += 1

    # Other fingers
    for i in range(1, 5):
        if landmarks[tip_ids[i]].y < landmarks[dip_ids[i]].y:
            count += 1

    return count

def classify_gesture(landmarks):
    tip_ids = [4, 8, 12, 16, 20]
    dip_ids = [3, 6, 10, 14, 18]

    def is_finger_extended(finger_index):
        tip_y = landmarks[tip_ids[finger_index]].y
        dip_y = landmarks[dip_ids[finger_index]].y
        if finger_index == 0:  # thumb
            tip_x = landmarks[tip_ids[0]].x
            ip_x = landmarks[dip_ids[0]].x
            return tip_x > ip_x   # right hand assumption
        else:
            return tip_y < dip_y

    thumb = is_finger_extended(0)
    index = is_finger_extended(1)
    middle = is_finger_extended(2)
    ring = is_finger_extended(3)
    pinky = is_finger_extended(4)

    if thumb and not index and not middle and not ring and not pinky:
        return "Thumbs Up"
    elif index and middle and not ring and not pinky and not thumb:
        return "Peace / Victory"
    elif index and not middle and not ring and not pinky and not thumb:
        return "Pointing"
    elif index and middle and ring and not pinky and not thumb:
        return "Three"
    elif index and middle and ring and pinky and not thumb:
        return "Four"
    elif index and middle and ring and pinky and thumb:
        return "Open Hand / Five"
    elif not thumb and not index and not middle and not ring and not pinky:
        return "Fist"
    elif thumb and pinky and not index and not middle and not ring:
        return "Call Me"
    elif index and thumb and not middle and not ring and not pinky:
        return "OK / Pinch"
    else:
        cnt = sum([thumb, index, middle, ring, pinky])
        return f"{cnt} fingers"