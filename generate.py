import re, json, requests

unfilteredThesaraus = requests.get("https://raw.githubusercontent.com/words/moby/master/words.txt").text

filteredThesaraus = [i for i in unfilteredThesaraus.split("\n") if re.match("^([\w-]+),", i)]
words = {}
for i in filteredThesaraus:
    words[re.match("^([\w-]+),", i)[1]] = i.replace(re.match("^([\w-]+),", i)[0], "").split(",")
open("words.json", "w+").write(json.dumps(words))
