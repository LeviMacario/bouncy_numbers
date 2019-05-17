class BouncyNumber(object):
    '''
    Responsible for manipulating bouncy numbers.

    Ex.:
    proportion = 0.6
    obj = BouncyNumber(proportion)
    '''
    def __init__(self, proportion):
        self.first_number = 99
        self.proportion = proportion
    
    def _is_bouncy(self, number):
        '''
        Simple method responsible for 
        figuring out whether the number is bouncy.
        '''
        greater_than = False
        less_than = False
        # Returns the remainder of the division 
        # by 10 to get the last digit to the right
        right_digit = number % 10
        # Returns the division of floor by discarding
        # the fractional part in order to get the number 
        # excluded from the last digit on the right.
        number = number // 10

        while number > 0:
            left_digit = number % 10
            if left_digit < right_digit:
                greater_than = True
            elif left_digit > right_digit:
                less_than = True
            right_digit = left_digit
            number = number // 10
            if greater_than and less_than:
                return True
        return False

    def find_first_with_proportion(self):
        '''
        # Iterate through numbers until the 
        # bouncy count is proportion of the total count.
        '''
        count = 0
        i = self.first_number
        while count < self.proportion * i:
            i = i + 1
            if self._is_bouncy(i):
                count = count + 1
        return i


if __name__ == '__main__':
    bouncy_obj = BouncyNumber(0.99)
    print(bouncy_obj.find_first_with_proportion())