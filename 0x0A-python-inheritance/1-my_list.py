#!/usr/bin/python3
'''
prints a sorted list
'''


class MyList(list):
    '''
    prints a list in sorted order
    '''
    def print_sorted(self):
        '''
        prints sorted list using the inherited list
        '''
        print(sorted(self))
