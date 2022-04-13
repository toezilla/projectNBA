import schedule
import time
import sys

if __name__ == "__main__":
    def message():
        print("test schedule...")

    def exit():
        print("schedule ends...")
        sys.exit()
    schedule.every(1).seconds.do(message)
    schedule.every().day.at("03:26").do(exit)

    while True:
        schedule.run_pending()
        time.sleep(1)
