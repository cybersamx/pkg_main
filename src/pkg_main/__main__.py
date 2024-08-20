import pkg_a.vars as a
import pkg_b.vars as b


def main():
    sample = [610, 450, 160, 420, 310]

    print(a.stddev(sample))
    print(b.variance(sample))


if __name__ == "__main__":
    main()
