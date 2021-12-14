
def solution(arr):
    count = 0
    start_idx = 1

    # while start_idx < len(arr) - 1:
        for i in range(start_idx, len(arr) - 1):
            if i < start_idx:
                continue

            # for j in range(i, len(arr) - 1):
            #     start_idx = j
            #
            #     if arr[0] > arr[1]:
            #         continue
            #
            #     prev = arr[j-1]

            #     curr = arr[j]
            #     next = arr[j+1]
            #
            #     if prev >= curr and curr <= next:
            #         count += 1
            #         break


            a_count, start_idx = find_a(arr, start_idx)
            count += a_count
            break
            print("ing...")


    # return count % (int(pow(10, 9)) + 7)
    return count

def find_a(arr, idx):
    count = 0
    start_idx = 0
    for j in range(idx, len(arr) - 1):
        start_idx = j

        if arr[0] > arr[1]:
            continue

        prev = arr[j-1]
        curr = arr[j]
        next = arr[j+1]

        if prev >= curr and curr <= next:
            break

        count += 1

    return count, start_idx


def main():
    arr = [0, 1, 2, 5, 3, 7]
    # arr = [1, 2, 3, 2, 1, 4, 3, 2, 2, 1]
    print(solution(arr))

if __name__ == "__main__":
    main()




'''
문제 설명
주어진 배열 안에 A자 모양 부분 배열이 몇 개 있는지 알아보려고 합니다. 부분 배열은 어떤 배열 내부에 존재하는 또 다른 배열로, 원래 배열의 연속적인 부분입니다. 예를 들어 배열 [1, 2, 3]의 비어 있지 않은 부분 배열은 [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]으로, 6개가 있습니다.

배열 arr이 다음과 같은 조건을 모두 만족할 경우 A자 모양이라고 합니다.

arr의 길이 ≥ 3
arr 내 어떤 인덱스 i가 다음과 같은 조건을 모두 만족합니다.
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr의 마지막 원소
0 < i < arr의 길이 - 1
예를 들어 배열 [0, 1, 2, 5, 3, 7]의 부분 배열 [1, 2, 5, 3]은 1부터 5까지 줄곧 값이 증가하다가 5부터 마지막 원소까지 줄곧 값이 감소합니다. 따라서 부분 배열 [1, 2, 5, 3]은 A자 모양 배열입니다.

배열 [0, 1, 2, 5, 3, 7]의 부분 배열 중 A자 모양 배열인 것은 [2, 5, 3], [1, 2, 5, 3], [0, 1, 2, 5, 3]으로, 3개가 있습니다.

1차원 정수 배열 arr이 매개변수로 주어집니다. arr의 부분 배열 중 A자 모양 배열의 수를 return 하도록 solution 함수를 완성해주세요. 단, 결괏값이 매우 커질 수 있으므로 10^9 + 7로 나눈 나머지를 return 해주세요.

제한사항
3 ≤ arr의 길이 ≤ 100,000
0 ≤ arr의 원소 ≤ 1,000,000,000
입출력 예
arr	result
[0, 1, 2, 5, 3, 7]	3
[1, 2, 3, 2, 1]	4
[1, 2, 3, 2, 1, 4, 3, 2, 2, 1]	6
[1, 2, 1, 2, 1]	2
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

arr의 부분 배열 중 A자 모양 배열인 것은, [1, 2, 3, 2], [1, 2, 3, 2, 1], [2, 3, 2], [2, 3, 2, 1]로 4개가 있습니다. 따라서 4를 return 합니다.

입출력 예 #3

arr의 부분 배열 중 A자 모양 배열인 것은, [1, 2, 3, 2], [1, 2, 3, 2, 1], [2, 3, 2], [2, 3, 2, 1], [1, 4, 3], [1, 4, 3, 2]로 6개가 있습니다. 부분 배열 [1, 4, 3, 2, 2, 1]은 정점인 원소 4부터 마지막 원소 1까지 줄곧 값이 감소하지 않기 때문에 A자 모양 배열이 아닙니다. 따라서 6을 return 합니다.

입출력 예 #4

arr의 부분 배열 중 A자 모양 배열인 것은, 인덱스 0부터 2까지 [1, 2, 1] 배열과 인덱스 2부터 4까지 [1, 2, 1] 배열이 있습니다. 두 배열의 원소와 순서가 같더라도 위치가 다르므로 따로 세어야 합니다. 따라서 2를 return 합니다.
'''
