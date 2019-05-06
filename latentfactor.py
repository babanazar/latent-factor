import numpy as np
import platform
import multiprocessing as mp
from operator import itemgetter
from multiprocessing import Process


def readDataset(fileName, userSongRating):
    print(f'reading file {fileName}')

    # userSongRating.append([11, 12, 13])
    with open(fileName, 'r') as f:
        i = 0
        for line in f:
            # print(f'i ---> {i} ')
            a = line.split()
            # userSongRating.append(line.split())
            # lines = line.rstrip('\n')
            user_id, song_id, rating = line.split()
            user_id = int(user_id)
            song_id = int(song_id)
            rating = int(rating) * 1.0
            userSongRating.append([user_id, song_id, rating])
            # userSongRating.append((user_id, song_id, rating))
            # userSongRating.append([lines[0], lines[1], lines[2]])
            # print(f'user song rating for {i} ---> {userSongRating[i][0]} {userSongRating[i][1]} {userSongRating[i][2]}')
            i += 1
            if i == 1000:
                break

        # print(lines.__class__)
        # print(lines)
        # lines = lines.split('\t')
        # print(lines)
        # print(lines[0])
        # print(lines[1])
        # print(lines[2])
    # print(lines)


def main():
    # print(f'platform is {platform.architecture()}')
    trains = ['train_0.txt', 'train_1.txt', 'train_2.txt', 'train_3.txt', 'train_4.txt', 'train_5.txt', 'train_6.txt',
              'train_7.txt', 'train_8.txt', 'train_9.txt']
    tests = ['test_0.txt', 'test_1.txt', 'test_2.txt', 'test_3.txt', 'test_4.txt', 'test_5.txt', 'test_6.txt',
             'test_7.txt', 'test_8.txt', 'test_9.txt']
    manager = mp.Manager()
    userSongRating = manager.list()
    print(userSongRating)
    p0 = mp.Process(target=readDataset, args=(tests[0], userSongRating))
    # p1 = mp.Process(target=readDataset, args=(tests[1], userSongRating))
    # p2 = mp.Process(target=readDataset, args=(tests[2], userSongRating))
    # p3 = mp.Process(target=readDataset, args=(tests[3], userSongRating))
    # p4 = mp.Process(target=readDataset, args=(tests[4], userSongRating))
    # p5 = mp.Process(target=readDataset, args=(tests[5], userSongRating))
    # p6 = mp.Process(target=readDataset, args=(tests[6], userSongRating))
    # p7 = mp.Process(target=readDataset, args=(tests[7], userSongRating))
    # p8 = mp.Process(target=readDataset, args=(tests[8], userSongRating))
    # p9 = mp.Process(target=readDataset, args=(tests[9], userSongRating))

    p0.start()
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
    # p7.start()
    # p8.start()
    # p9.start()

    p0.join()
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    # p6.join()
    # p7.join()
    # p8.join()
    # p9.join()

    print('after all ---> ')

    print(np.__file__)
    #this line sorts given matrix according to userIds
    print(f'-{userSongRating}-')

    userSongRating = np.array(userSongRating)  # convert list to numpy array
    startIndex = 0  # start index of user
    sumUser = list()  # sum of the ratings of a user

    now = 0
    count = 0

    sumUser.insert(0, [0, 0])

    # this loop sums all users' ratings

    for i in range(len(userSongRating)):
        if userSongRating[i][0] != userSongRating[i-1][0]:
            now = 0
            count = 0

        now += userSongRating[i][2]
        count += 1
        sumUser.insert(int(userSongRating[i][0]), [now, count])

    print('sumUser')
    print(sumUser)

    for i in range(len(userSongRating)):
        print(f'total rating {sumUser[int(userSongRating[i][0])][0]}')
        print(f'total count {sumUser[int(userSongRating[i][0])][1]}')
        userSongRating[i][2] -= sumUser[int(userSongRating[i][0])][0] / sumUser[int(userSongRating[i][0])][1]

    print('after normalization')
    print(userSongRating)

    print('----------------after normalization----------------')
    for i in range(len(userSongRating)):
        print(f'{userSongRating[i][0]}, {userSongRating[i][1]}, {userSongRating[i][2]}')


if __name__ == '__main__':
    main()
