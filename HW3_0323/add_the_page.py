def fine_page(n):
    page, total_page = 1, 0
    while True:
        total_page += page
        if total_page > n:
            break
        page += 1
    return page, total_page-n

if __name__ == '__main__':
    num_of_input = int(input())
    for i in range(num_of_input):
        page, loss_page = fine_page(int(input()))
        print(page, loss_page)
