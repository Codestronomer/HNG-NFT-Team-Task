#!/usr/bin/env python3
"""
This module converts a csv file to CHIP-0007 JSON representation
"""
import csv
import json
import sys


def func(csvfilepath):
    # read csv file
    with open(csvfilepath, encoding='utf-8') as csv_file:
        nftReader = csv.DictReader(csv_file)
        for row in nftReader:
            nft_dict = {}
            if row["Filename"] == "":
                # save team name
                # create team json file
                team = row["Series Number"]
            else:
                # fill nft dictionary with details from csvfile rows
                nft_dict["format"] = "CHIP-0007"
                nft_dict["name"] = row["Filename"]
                nft_dict["description"] = row["Description"]
                nft_dict["minting tool"] = team
                nft_dict["sensitive_content"] = False
                nft_dict["series_number"] = row["Series Number"]
                nft_dict["series_total"] = 420
                nft_dict["attributes"] = []
                # parse attributes from row
                kv = parse_attr(
                    row["Attributes- Hair. Eyes. Teeth. Clothing. Accessories. Expression. Strength. Weakness"])
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
            with open(f"{team}.json", "a", encoding='utf-8') as json_file:
                json.dump(nft_dict, json_file)


def parse_attr(strs):
    # parse attributes column from csv
    strr = strs.replace(".", ",").replace(" ", "")
    strl = [i for i in strr.split(",")]

    kv_list = [kv.split(":") for kv in strl if len(kv) > 1]
    return kv_list


# Driver code
if sys.argv[1]:
    # call the main function if file name is supplied
    func(sys.argv[1])
