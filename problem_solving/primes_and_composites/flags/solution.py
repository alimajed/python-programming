def solution(input):
    peaks = [0] * len(input)
    next_peak = len(input)
    peaks[len(input)-1] = next_peak
    for i in range(len(input)-2, 0, -1):
        if input[i-1] < input[i] and input[i+1] < input[i]:
            next_peak = i
        peaks[i] = next_peak
    peaks[0] = next_peak

    current_guess = 0
    next_guess = 0
    while can_place_flags(peaks, next_guess):
        current_guess = next_guess
        next_guess += 1
    return current_guess


def can_place_flags(peaks, flags):
    current_pos = 1 - flags
    for i in range(flags):
        if current_pos + flags > len(peaks) - 1:
            return False
        current_pos = peaks[current_pos+flags]
    return current_pos < len(peaks)


if __name__ == "__main__":
    print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))