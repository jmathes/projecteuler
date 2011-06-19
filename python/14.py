known_answers = {1: 1}

def collatzcount(n, known_answers):
    try:
        return known_answers[n]
    except KeyError:
        pass

    if n%2 == 0:
        answer = 1 + collatzcount(n/2, known_answers)
    else:
        answer = 1 + collatzcount(3 * n + 1, known_answers)
    known_answers[n] = answer
    return answer


longest_chain = 1
answer = 1

for i in xrange(2, 1000000):
    chain_length = collatzcount(i, known_answers)
    known_answers[i] = chain_length
    if chain_length > longest_chain:
        answer = i
        longest_chain = chain_length
        
print answer