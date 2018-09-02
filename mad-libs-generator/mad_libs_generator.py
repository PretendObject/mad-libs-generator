story = '''
O say can you {} by the dawn's early {},
What so {} we {} at the twilight's last gleaming,
Whose broad {} and bright {} through the {} fight,
O'er the {} we watched, were so gallantly {}!
And the rockets' {} glare, the {} bursting in {},
Gave proof through the night that our {} was still there;
{} does the {} banner yet {},
O'er the land of the {} and the home of the {}!
'''

def main():
    verb = []
    noun = []
    adjective = []

    verb.append(input('Enter a verb: '))
    noun.append(input('Enter a noun: '))
    adverb = input('Enter an adverb: ')
    verb.append(input('Enter a past tense verb: '))
    noun.append(input('Enter a plural noun: '))
    noun.append(input('Enter a plural noun: '))
    adjective.append(input('Enter an adjective: '))
    noun.append(input('Enter a plural noun: '))
    verb.append(input('Enter a verb ending in -ing: '))
    color = input('Enter a color: ')
    noun.append(input('Enter a plural noun: '))
    noun.append(input('Enter a noun: '))
    noun.append(input('Enter a noun: '))
    interjection = input('Enter an interjection: ')
    adjective.append(input('Enter an adjective: '))
    verb.append(input('Enter a verb: '))
    adjective.append(input('Enter an adjective: '))
    adjective.append(input('Enter an adjective: '))

    mad_lib = story.format(verb[0],
                           noun[0],
                           adverb,
                           verb[1],
                           noun[1],
                           noun[2],
                           adjective[0],
                           noun[3],
                           verb[2],
                           color,
                           noun[4],
                           noun[5],
                           noun[6],
                           interjection,
                           adjective[1],
                           verb[3],
                           adjective[2],
                           adjective[3])

    print(mad_lib)

main()

