# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:04:12 2024

@author: axeve

Alexis Evans
CS120
Prof Harris
February 23, 2024
Text Adventure Game

"""
import json
 
def main():
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            keepGoing = False
        elif menuChoice == "1":
            print("Load default game")
            game = getDefaultGame()
        elif menuChoice == "2":
            print("Load game file")
            game = loadGame()
        elif menuChoice == "3":
            print("Saved game")
            saveGame(game)
        elif menuChoice == "4":
            print("Edit or add a node")
            game = editNode(game)
        elif menuChoice == "5":
            print("The game will now begin.")
            playGame(game)
        else:
            print("Please select one option from 0-5")
            
def getMenuChoice():
    keepGoing = True
    while keepGoing:
        print(""" 
            0) Exit
            1) Load default game
            2) Load game file
            3) Save current game
            4) Edit or add node
            5) Play current game""")
        menuChoice = input("What will you choose?: ")
        if menuChoice in ("0", "1", "2", "3", "4", "5"):
            keepGoing = False
        else:
            print("Please choose a number from 0-5.")
    return menuChoice
        
def getDefaultGame():
    game = {
        "start": ["You may start over or quit the game.", "Start over", "start", "Quit", "quit"]}
    return game
    
def playNode(game, currentGame):
    (description, menuA, nodeA, menuB, nodeB) = game[currentGame]
    keepGoing = True
    while keepGoing:
        print(f""" 
              {description}
              1) {menuA}
                2) {menuB}
                """)
        response = input("What will you choose?: ")
        if response == "1":
            nextNode = nodeA
            keepGoing = False
        elif response == "2":
            nextNode = nodeB
            keepGoing = False
        else:
            print("Invalid. Please try again.")
        return nextNode
def playGame(game):
    currentGame = "start"
    keepGoing = True
    while keepGoing:
        currentGame = playNode(game, currentGame)
        if currentGame == "quit":
            keepGoing = False
        
def saveGame(game):
    fileName = "game.json"
    saveFile = open(fileName, "w")
    json.dump(game, saveFile, indent = 2)
    saveFile.close()
    print(json.dumps(game, indent = 2))


def loadGame():
    fileName = "game.json"
    loadFile = open(fileName, "r")
    game = json.load(loadFile)
    loadFile.close()
    return game

def editNode(game):
    print("These are the current node names.")
    print(json.dumps(game, indent=2))
    for nodeName in game.keys():
        print(f"{nodeName}")
    newNodeName = input("Input a new name. If the name already exists, no new node will be added.: ")
    if newNodeName in game.keys():
        newNode = game[newNodeName]
    else:
        newNode = ["", "", "", "", ""]
    (description, menuA, nodeA, menuB, nodeB) = newNode
    newDescription = getField("description", description)
    newMenuA = getField("Menu A", menuA)
    newNodeA = getField("Node A", nodeA)
    newMenuB = getField("Menu B", menuB)
    newNodeB = getField("Node B", nodeB)
    
    game[newNodeName] = {newDescription, newMenuA, newNodeA, newMenuB, newNodeB}
    return game
def getField(prompt, currentValue):
    newVal = input(f"{prompt} ({currentValue}): ")
    if newVal == "":
        newVal = currentValue
    return newVal

main()
            