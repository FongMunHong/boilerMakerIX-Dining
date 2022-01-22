import requests, json, datetime

locations = ["Wiley", "Ford", "Hillenbrand", "The Gathering Place", "Earhart", "Windsor"]
url = "http://api.hfs.purdue.edu/menus/v2/locations/"
header={"Accept":"application/json"}

def fetch_menu(location):

    time = datetime.datetime.now()
    ftime = time.strftime("%m-%d-%Y")
    try:
        r =  requests.get(url+location+"/"+ftime+"/", headers=header)
        return r.json()
    except requests.ConnectionError:
        print("Failed to connect!")



def print_menu(location_json):
    # print(location_json["Location"])
    mealjson = location_json["Meals"]

    with open("dining.json", "w") as outfile:
        json.dump(mealjson, outfile)

    # for x in list(range(len(mealjson))):
    #     print("--"+mealjson[x]["Name"].encode('ascii', 'ignore'))
    #     for y in list(range(len(mealjson[x]["Stations"]))):
    #         print("-------")
    #         print("----"+mealjson[x]["Stations"][y]["Name"].encode('ascii', 'ignore') + "| font=HelveticaNeue-Bold")
    #         for z in list(range(len(mealjson[x]["Stations"][y]["Items"]))):
    #             print("----"+mealjson[x]["Stations"][y]["Items"][z]["Name"].encode('ascii', 'ignore'))
    #         print(" ")


def bitbar_main():
    print("🍴")
    print("---")
    for location in locations:
        print(location)
        print_menu(fetch_menu(location))
        break


bitbar_main()