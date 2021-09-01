class DiscLog():
    def __init__(self, x, start_end):
        self.x = x
        self.start_end = start_end


def solution(input):
    disc_history = []
    for i in range(len(input)):
        # NOTE getting the start position is the center position (index) - radius (value)
        disc_history.append(DiscLog(i - input[i], 1))
        # NOTE getting the end position is the center position (index) + radius (value)
        disc_history.append(DiscLog(i + input[i], -1))
    # NOTE sort in asc by x position, then by start end indicator
    disc_history.sort(key=lambda d: (d.x, -d.start_end))
    
    intersections = 0
    active_intersections = 0

    for log in disc_history:
        active_intersections += log.start_end
        if log.start_end > 0:
            # NOTE The number of overlapped discs (intersections) is the value on Y axis -1
            intersections += active_intersections -1

    return intersections


if __name__ == "__main__":
    print(solution([1,5,2,1,4,0]))