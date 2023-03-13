def fn(p, q, r):
    return not p or (q or r)

def main():
    print("p q r\tp->(q v r)")
    print("------------------")

    # Вивід таблиці істинності
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                result = int(fn(p, q, r))
                print(int(p),int(q), int(r), "    \t", result)

if __name__ == "__main__":
    main()
