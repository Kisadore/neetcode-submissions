class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # x record new score of integer x
        # + record score that is the sum o the previous two
        # D record new score that is the double of the previous
        # C invalidate the previous sccore by removing it 

        # Return the sum of all the scores on the record after applying opperations

        record = []
        total = 0
        for char in operations:
            if char == '+':
                prev_two_sum = record[-1] + record[-2]
                record.append(prev_two_sum)
                total += prev_two_sum
            elif char == 'C':
                removed_val = record.pop()
                total -= removed_val
            elif char == 'D':
                prev_score = record[-1]
                double_score = prev_score * 2
                record.append(double_score)
                total += double_score
            else:
                char_val = int(char)
                record.append(char_val)
                total += char_val
        return total
            
