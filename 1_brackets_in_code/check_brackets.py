# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    """For convenience, the text editor should not only inform the user that there is an error in the usageof brackets, but also point to the exact place in the code with the problematic bracket.
    
     First priority is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it,like ] in ] (), or closes the wrong opening bracket, like } in () [}. 
     
     If there are no such mistakes, then it should find the first unmatched opening bracket without the corresponding closing bracket after it, like ( in {}([]. If there are no mistakes, text editor should inform the user that the usage of bracketsis correct. 
     
     Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks. More formally, all brackets in the code should be divided into pairs of matching brackets, such that in each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either one of them is nested inside another one as in (foo[bar]) or they are separate as inf(a,b)-g[c].The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).
     
     Input Format
     Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation marks and brackets from the set [] {} ().
     
     Constraints
     The length of 𝑆 is at least1and at most 10^5.
     
     Output Format
     If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket."""


    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, i+1))

        elif next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i+1

            last_open_bracket = opening_brackets_stack.pop()

            if not are_matching(last_open_bracket[0], next):
                return i+1

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0][1]
    else:
        return 'Success'
                


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here

    print(mismatch)
if __name__ == "__main__":
    main()
