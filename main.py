import argparse, os

from scrap import ScraperBot



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Url", "-u",  help="Please paste PSA website Url like: -u URL")
    args = parser.parse_args()
    Url = args.Url
    if not Url :
        print("Please include URL using the -u in the cammand section of this script.")
        quit()
    else:
        try:
            ScraperBot(Url)
        except Exception:
            print("Please send a valid URL in param-->")



if __name__ == "__main__":
    main()


