import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

def find_word(string_list):
    """ Return a list of words that contain three digit numbers in the middle. """

    # initialize an empty list
    dict=[]
    # define the regular expression
    regex = r'\b[A-Qa-z]+\d{3}[A-Qa-z]+'
    # loop through each line of the string list 
    for line in string_list:
        line = line.rstrip()
        
    # find all the words that match the regular expression in each line
        words = re.findall(regex,line)
        # print(words)
    # loop through the found words and add the words to your empty list 
        for word in words:
            dict.append(word)

    #return the list of all words that start with the letter B, E, or T
    # print(dict)
    return dict
# （return）
# (?: grouping)
# xxxx(?:pattern){5}xxx

def find_days(string_list):
    """ Return a list of days from the list of strings the dates format in the text are MM/DD/YYYY. """  

    # initialize an empty list
    dict2=[]
    # define the regular expression
    regex= r'\d+\/(\d+)\/\d{4}'
    # loop through each line of the string list
    for line in string_list:
        line = line.rstrip()
    # find all the dates that match the regular expression in each line
        dates= re.findall(regex,line)
    # loop through the found dates and only add the days to your empty list 
        for date in dates:
            dict2.append(date)
    #return the list of days
    return dict2

def find_domains(string_list):
    """ Return a list of web address domains from the list of strings the domains of a wbsite are after www. """

    # initialize an empty list
    dict=[]
    # define the regular expression
    regex= r'\bhttps?:\/\/(?:www.)?(.+)\/'
    # loop through each line of the string list
    for line in string_list:
        line = line.rstrip()
    # find all the domains that match the regular expression in each line
        domains= re.findall(regex,line)
    # loop through the found domains
        for domain in domains:
           
    # get the domain name by splitting the (//) after the https or http to get the website name
    # then strip the www. to get only the domain name

    # add the domains to your empty list
            dict.append(domain)
    #return the list of domains
    return dict

class TestAllMethods(unittest.TestCase):


    def test_find_word(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        word_list = find_word(string_list)
        self.assertEqual(len(word_list),4)
    
    def test_find_days(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        days_list = find_days(string_list)
        self.assertEqual(days_list,['23', '12', '31', '4', '1', '4'])
    
    def test_domains(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_ch_1.txt')
        domain_list = find_domains(string_list)
        self.assertEqual(domain_list,['pythex.org', 'si.umich.edu', 'sabapivot.com', 'stars.chromeexperiments.com', 'theofficestaremachine.com', 'regex101.com'])


def main():
	# Use main to test your function. 
    # string_list = read_file('alice_ch_1.txt')
    # word_list = find_word(string_list)
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()