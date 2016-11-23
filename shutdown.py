import sys
import subprocess
import time

if __name__ == "__main__":
	try:
		time = sys.argv[1]
	except IndexError:
		time = "3000"
	subprocess.call(["shutdown.exe", "-f", "-s", "-t", time])
	print("Computer will shutdown in {} seconds({} minutes).".format(time, int(time)/60))
