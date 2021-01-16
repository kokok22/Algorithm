## RC카 움직인 거리계산

def start(cmds):
    distance = 0
    speed = 0
    for cmd in cmds:
        if cmd[0] == 0:
            distance += speed

        elif cmd[0] == 1:
            speed += cmd[1]
            distance += speed

        elif cmd[0] == 2:
            speed -= cmd[1]
            if speed < 0:
                speed = 0
            distance += speed

    return distance


T = int(input())

for t in range(T):
    num = int(input())
    cmd = []

    for i in range(num):
        cmd.append(list(map(int, input().strip(' ').split(' '))))

    print("#{} {}".format(t+1, start(cmd)))