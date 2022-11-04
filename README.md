# NFT CHIP PROJECT
> Converts data in a CSV file to a CHIP-0007 JSON Representation of it
> Hashes the JSON file and stores the hashes with the csv data in a new file<!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Tested On](#tested-on)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Example](#example)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Purpose: To convert NFT details in a CSV file to CHIP-0007 compatible JSON files 
- Done as a team task for the HNGI9 Internship
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Python - version 3.10

## Tested On
- Ubuntu - version 20.10


## Features
- Convert data in CSV File to CHIP-0007 compatible JSON files
- Hash JSOn files with SHA256 Cryptography algorithm
- Same hashes and NFT data in a csv file


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
Install python if you don't have it installed
https://www.python.org/downloads/
or if you're running Ubuntu, In terminal enter
`
$ sudo apt-get update
$ sudo apt-get install python3
`
Clone Repository
`$ git clone https://github.com/Codestronomer/HNG-NFT-Team-Task`


## Usage
Run the python script while passing the relative path to the csv file as argument

`./csv2jsonparser.py <pathtocsvfile>`

## Example

```bash
./csv2jsonparser.py "csv/HNGi9 CSV FILE - Sheet1.csv"
```

Here is the json file with the default values:

```jsonc
{
    "format": "CHIP-0007",
    "name": "Pikachu",
    "description": "Electric-type Pokémon with stretchy cheeks",
    "minting_tool": "SuperMinter/2.5.2",
    "sensitive_content": false,
    "series_number": 0,
    "series_total": 0,
    "attributes": [],
    "collection": {
        "name": "Example Pokémon Collection",
        "id": "e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57",
        "attributes": [
            {
                "type": "description",
                "value": "Example Pokémon Collection is the best Pokémon collection. Get yours today!"
            },
            {
                "type": "icon",
                "value": "https://examplepokemoncollection.com/image/icon.png"
            },
            {
                "type": "banner",
                "value": "https://examplepokemoncollection.com/image/banner.png"
            },
            {
                "type": "twitter",
                "value": "ExamplePokemonCollection"
            },
            {
                "type": "website",
                "value": "https://examplepokemoncollection.com/"
            }
        ]
    },
    "data": {}
}
```

**Below is a sample csv file**

| TEAM NAMES | Series Number | Filename          | Name              | Description                                 | Gender | Attributes                                                                                                                        | UUID                                 |
| ---------- | ------------- | ----------------- | ----------------- | ------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| TEAM BEVEL | 1             | adewale-the-amebo | adewale the amebo | Adewale likes to be in everyone's business. | Male   | hair: bald; eyes: black; teeth: none; clothing: red; accessories: mask; expression: none; strength: powerful; weakness: curiosity | cad316c3-37f8-4b27-9f53-9d803bfcfee7 |


## Project Status
Project is: _complete_


## Acknowledgements
Give credit here.
- This project was inspired by HNG I9 INTERNSHIP

## Contact
Created by [John Rumide](https://www.github.com/codestronomer/) - feel free to contact me!
Email: Johnrumide6@gmail.com
Twitter: @_codenaut


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
