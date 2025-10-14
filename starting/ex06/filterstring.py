from ft_filter import ft_filter
import sys


def main():
    try:
        ft_filter(sys.argv)
    except AssertionError:
        print("AssertionError: the arguments are bad")



if __name__ == "__main__":
    main()
