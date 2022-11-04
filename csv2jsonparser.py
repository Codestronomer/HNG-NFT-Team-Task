#!/usr/bin/env python3
"""
This module converts a csv file to CHIP-0007 JSON representation
"""
import csv
import json
import sys
import hashlib


team_list = ["TEAM AXE", "TEAM AXLE", "TEAM BEVEL", "TEAM BOOT", "TEAM BRAINBOX",
             "TEAM CHISEL", "TEAM CLUTCH", "TEAM CRANKSHAFT", "TEAM ENGINE", "TEAM GEAR", "TEAM GRIT",
             "TEAM HEADLIGHT", "TEAM HYDRAULICS", "TEAM PLUG", "TEAM POWERDRILL", "TEAM PRYBAR", "TEAM RULER",
             "TEAM SANDPAPER", "TEAM SCALE", "TEAM TAPE", "TEAM VBELT"]


def func(csvfilepath):
    # read csv file
    with open(csvfilepath, encoding='utf-8') as csv_file:
        nftReader = csv.DictReader(csv_file)
        for row in nftReader:
            nft_dict = {}
            if row["Filename"] == "":
                # save team name
                # create team json file
                team = row["TEAM NAMES"]
            else:
                # fill nft dictionary with details from csvfile rows
                nft_dict["format"] = "CHIP-0007"
                nft_dict["name"] = row["Filename"]
                nft_dict["description"] = row["Description"]
                nft_dict["minting tool"] = row["TEAM NAMES"]
                nft_dict["sensitive_content"] = False
                nft_dict["series_number"] = row["Series Number"]
                nft_dict["series_total"] = 420
                nft_dict["attributes"] = []
                # parse attributes from row
                kv = parse_attr(
                    row["Attributes"])
                for i in kv:
                    attr_dict = {}
                    if len(i) > 1:
                        attr_dict["trait_type"] = i[0]
                        attr_dict["value"] = i[1]
                        nft_dict["attributes"].append(attr_dict)
                nft_dict["collections"] = {}
                nft_dict["collections"]["name"] = "Zuri NFT Tickets for Free Lunch"
                nft_dict["collections"]["id"] = row["UUID"]
                # add nft to team json file
                team = row["TEAM NAMES"]
                with open(f"{team}.json", "a", encoding='utf-8') as json_file:
                    json.dump(nft_dict, json_file)


def parse_attr(strs):
    # parse attributes column from csv
    strr = strs.replace(".", ",").replace(" ", "")
    strl = [i for i in strr.split(",")]

    kv_list = [kv.split(":") for kv in strl if len(kv) > 1]
    return kv_list


def hash_jsonfile():
    # hash team json files
    team_dict = {}

    hasher = hashlib.sha256()
    for team in team_list:
        with open(f"{team}.json", 'rb') as f:
            buf = f.read()
            hasher.update(buf)
            team_dict[team] = hasher.hexdigest()

    return team_dict


def add_hash_to_csv():
    # Map hash of team json files with to a csv file
    dict_list = []
    with open("csv/HNGi9 CSV FILE - Sheet1.csv", 'r') as file:

        reader = csv.DictReader(file)

        for row in reader:
            if row["TEAM NAMES"] in team_list:
                new_team = team_dict[row["TEAM NAMES"]]
                row["HASH"] = team_dict[row["TEAM NAMES"]]
            else:
                row["HASH"] = new_team
            new_dict = row
            dict_list.append(new_dict)

    with open("csv/sample.output.csv", 'w', newline='') as file:
        fieldlist = [
            'TEAM NAMES', 'Series Number',
            'Filename', 'Name', 'Description',
            'Gender', 'Attributes', 'UUID', 'HASH'
        ]
        writer = csv.writer(file)
        writer.writerow(fieldlist)
        for dicts in dict_list:
            values = []
            for k, v in dicts.items():
                values.append(v)
            writer.writerow(values)


# Driver Code
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./csv2jsonparser.py <pathtocsvfile>")
    elif sys.argv[1]:
        # call the main function if file name is supplied
        func(sys.argv[1])
        team_dict = hash_jsonfile()
        add_hash_to_csv()

