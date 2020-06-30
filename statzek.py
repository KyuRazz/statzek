import requests,re 
from multiprocessing import Pool
import os, sys


def banner():
	print("""
███████ ████████  █████  ████████ ███████ ███████ ██   ██ 
██         ██    ██   ██    ██       ███  ██      ██  ██  
███████    ██    ███████    ██      ███   █████   █████   
     ██    ██    ██   ██    ██     ███    ██      ██  ██  
███████    ██    ██   ██    ██    ███████ ███████ ██   ██ 
Serizawa - Zekkel AR
	""")

def markow(anjing):
	s = 'https://www.statshow.com/www/{}' .format(anjing)
	try:
		a = requests.get(s, timeout=10).text
		#print(a)
		dong = re.findall('<span class="red_bold">(.*?)</span>', a)
		dong2 = re.findall('<span class="red_bold">(.*?)</span>', a)
		dong3 = re.findall('<span class="green_bold">(.*?)</span>', a)
		print()
		print(anjing)
		print('\t[+] Daily PageViews   : '+dong[0])
		print('\t[+] Daily Visitors    : '+dong2[1])
		print('\t[+] Daily Ads Revenue : '+dong3[2])

		tol = '[+] Daily PageViews    : '+dong[0]
		tol2 = '[+] Daily Visitors    : '+dong2[1]
		tol3 = '[+] Daily Ads Revenue : '+dong3[2]
		open('statshow.txt', 'a').write(anjing+'\n'+tol+'\n'+tol2+'\n'+tol3+'\n'+'============='+'\n\n')
	except Exception as e:
		print('{} --> Not Found Daily pler, web busuk ' .format(anjing))
		open('error_stat.txt', 'a').write(anjing)



if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	mmc = input(' LIST : ')

	a = open(mmc, 'r').read().splitlines()
	p = Pool(50)
	p.map(markow, a)
	p.close()
	p.join()
	print('')
	print('saved in statshow.txt')
	
