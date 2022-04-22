def separate_by_commas(string):
    '''
    This function takes in a string argument called 'string' The function takes the string and
    splits it at the commas. It also ignores commas if they are surrounded by "".
    It returns a list created when the string is split.
    '''
    results = []
    group = ""
    check = 0
    for char in string:
        if char == '"' and check == 0:
            check = 1
        elif char == '"' and check == 1:
            check = 0
        if char == "," and check == 0:
            results.append(group)
            group = ""
        else:
            if char != '"':
                group = group + char
    if group != "":
        results.append(group)
    if "," == string[len(string)-1]:
        results.append("")
    return results
def create_comma_separated_string(list_of_strings):
    '''
    This function takes in a list of strings as an argument called "list_of_strings". It takes the list
    and puts it into one string and seperates the index's with a comma. It returns this string.

    '''
    results = ""
    for index in range(len(list_of_strings)):
        string = list_of_strings[index]
        if len(string) > 1:
            results = results + '"'
            results = results + string
            results = results + '"'
        else:
            results = results + string
        if index != len(list_of_strings)-1:
            results = results + ","
    return results
def csv_file_to_list_of_lists(filename):
    '''
    This functions reads each line of of a csv file argument and returns a list in a list.
    where each inner list is based off of each line in the csv file. It breaks up the string
    by the seperate_by_commas function. It returns this 2d list
    '''
    count = len(open(filename).readlines())
    results = []
    file = open(filename,"r")
    for index in range(count):
        line = [file.readline().replace("\n","")]
        results.append(separate_by_commas(line))
        #results.append(file.readline().split("\n"))
    return results
def list_of_lists_to_csv_file(filename, list_of_lists):
    '''
    This function takes a list of lists called 'list_of_lists' argument and creates a csv file based on the lists
    This is done by writing to the csv file using each inner list for each line.
    Each inner list is turned into a string beforehand using the'create_comma_seperated_string' function
    It counts how many times a line is written in an interger called 'lines'
    this function also returns lines
    '''
    lines = 0
    file = open(filename,"w")
    for list in list_of_lists:
        file.write(create_comma_separated_string(list))
        if list != list_of_lists[len(list_of_lists)-1]:
            file.write("\n")
        lines = lines + 1
    return lines
def csv_file_to_list_of_dictionaries(filename):
    '''
    This function takes in a file name argument and It reads this file and creates a list of dictionaries called 'results'
    The first line of the file sets the keys n the dictionaries. each line is then placed in the dictionaries
    in the same order as the keys. This function returns results
    '''
    count = len(open(filename).readlines())
    results = []
    file = open(filename,'r')
    temp = file.readline().replace("\n","")
    keys = temp.split(",")
    for index in range(1,count):
        temp2 = file.readline().replace("\n","")
        line = temp2.split(",")
        dict = {}
        for endex in range(len(line)):
            if endex < len(keys):
                key = keys[endex]
                dict[key] = line[endex]
        results.append(dict)
    return results
def list_of_dictionaries_to_csv_file(filename, list_of_dictionaries):
    '''
    This function takes a list of dictionaries argument called 'list_of_dictionaries'
    It then uses the dictionaries to write to a csv file from the parameter 'filename'
    it takes the keys and writes it into the first line of the csv file.
    Then it uses each dictionary to write each line.
    The function keeps track of how many lines it writes in the interger 'lines'
    Then this function returns 'lines'
    '''
    file = open(filename,'w')
    starting_line = ""
    keys = []
    lines = 0
    for key in list_of_dictionaries[0]:
        keys.append(key)
    for index in keys:
        starting_line = starting_line + index
        if index != keys[len(keys)-1]:
            starting_line = starting_line + ","
    file.write(starting_line)
    file.write("\n")
    lines = lines + 1
    for dictionary in list_of_dictionaries:
        line = ""
        keys = []
        for index in dictionary:
            keys.append(index)
        for key in dictionary:
            line = line + dictionary[key]
            if key != keys[len(keys)-1]:
                line = line + ","
        if dictionary != list_of_dictionaries[len(list_of_dictionaries)-1]:
            file.write(line+"\n")
        lines = lines + 1
    return lines
