'''
You created a game that is more popular than Angry Birds.
You rank players in the game from highest to lowest score. So far you're using an
algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that their rankings
aren't updated fast enough. You need a faster sorting algorithm.

Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.
'''

def sort_score(unsorted_score,highest_possible_score):
    scores_to_counts = [0]*(highest_possible_score+1)
    for i in range(len(unsorted_score)):
        scores_to_counts[unsorted_score[i]] += 1
    k = 0
    for i in range(highest_possible_score,-1,-1):
        for j in range(scores_to_counts[i]):
            unsorted_score[k] = i
            k += 1
    return unsorted_score

# def sort_score(unordered_scores, highest_possible_score):
#
#     # list of 0s at indices 0..highest_possible_score
#     scores_to_counts = [0] * (highest_possible_score+1)
#
#     # populate scores_to_counts
#     for score in unordered_scores:
#         scores_to_counts[score] += 1
#
#     # populate the final sorted list
#     sorted_scores = []
#
#     # for each item in scores_to_counts
#     for score, count in enumerate(scores_to_counts):
#
#         # for the number of times the item occurs
#         for time in range(count):
#
#             # add it to the sorted list
#             sorted_scores.append(score)
#
#     return sorted_scores
# run your function through some test cases here
# remember: debugging is half the battle!
unsorted_score = [7,9,6,4,7,9,4,3,2,1,4,5,6,10]
highest_possible_score=10
print sort_score(unsorted_score,highest_possible_score)
