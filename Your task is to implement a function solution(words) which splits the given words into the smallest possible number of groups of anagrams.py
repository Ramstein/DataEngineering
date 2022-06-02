'''
Let's define a group of anagrams as a list of words, where for each pair of words w1 and w2, w1 is an anagram of w2.

Your task is to implement a function solution(words) which splits the given words into the smallest possible number of groups of anagrams and returns these groups as the answer.

Note: The groups of anagrams and the anagrams within a single groups can be returned in any order.

Example

For words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"], the output can be
solution(words) = [["tea", "eat", "ate"], ["apple"], ["vaja", "java"], ["cut", "utc"]].

Note: Any other set of 4 groups of anagrams would be also considered correct. Some other correct sets are:

[["tea", "ate", "eat"], ["apple"], ["vaja", "java"], ["utc", "cut"]];
[["apple"], ["java", "vaja"], ["eat", "tea", "ate"], ["cut", "utc"]];
[["apple"], ["ate", "eat", "tea"], ["cut", "utc"], ["java", "vaja"]].
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string words

A list of words, each containing only lowercase English letters.

Guaranteed constraints:
1 ≤ words.length ≤ 104,
1 ≤ words[i].length ≤ 100.

[output] array.array.string

The set that contains the smallest possible number of groups of anagrams. If there are several possible answers, return any of them.


'''
    # Input
    #  words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"], 
    # Output
    # [["tea", "eat", "ate"], ["apple"], ["vaja", "java"], ["cut", "utc"]].
    # Note: Any other set of 4 groups of anagrams would be also considered correct. Some other correct sets are:
    # [["tea", "ate", "eat"], ["apple"], ["vaja", "java"], ["utc", "cut"]];
    # [["apple"], ["java", "vaja"], ["eat", "tea", "ate"], ["cut", "utc"]];
    # [["apple"], ["ate", "eat", "tea"], ["cut", "utc"], ["java", "vaja"]].

    # 1. Create a dictionary of words and their counts
    # 2. Sort the dictionary by the counts
    # 3. Create a list of lists of words

    # 4. Return the list of lists


    #     anagramLists, currentAnagramList = [], []
    # words_anagrams = lambda x, y: str(sorted(x.lower())) == str(sorted(y.lower()))

    # for i in range(len(words)-1):
    #     for j in range(0, len(words)-i-1):
            
    #         if(words_anagrams(words[j], words[j+1])):
    #             if(words[j] not in currentAnagramList):
    #                 currentAnagramList.append(words[j])
    #             if(words[j+1] not in currentAnagramList):
    #                 currentAnagramList.append(words[j+1])

    #         anagramLists.append(currentAnagramList)
    #         currentAnagramList = []

    # return anagramLists


def findAnagrams(words):
    # Create a dictionary of words and their counts
    wordCounts = {}
    for word in words:
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    # Sort the dictionary by the counts
    sortedWordCounts = sorted(wordCounts.items(), key=lambda x: x[1])
    # Create a list of lists of words
    anagramLists = []
    currentAnagramList = []
    for word, count in sortedWordCounts:
        currentAnagramList.append(word)
        if len(currentAnagramList) == count:
            anagramLists.append(currentAnagramList)
            currentAnagramList = []
    return anagramLists